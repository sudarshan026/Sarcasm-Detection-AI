import os
import json
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

# Initialize Groq client
client = Groq(api_key=os.environ.get("GROQ_API_KEY", ""))

def analyze_sarcasm(text: str) -> dict:
    """
    Analyzes text to determine if it is sarcastic using Groq's Llama 3 model.
    Returns a dictionary with 'is_sarcastic' (boolean) and 'explanation' (string).
    """
    prompt = """
    You are an expert linguist and emotion analyzer. Your task is to detect whether the following text contains sarcasm.
    You must consider tone, context, irony, and common internet figures of speech.
    
    Return ONLY a JSON object with exactly two keys:
    - "is_sarcastic": boolean value (true or false)
    - "explanation": a 1 to 2 sentence explanation of why it is or isn't sarcastic.

    Text: "{text}"
    """
    
    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": "You are a specialized AI that outputs strictly valid JSON and nothing else."
                },
                {
                    "role": "user",
                    "content": prompt.format(text=text),
                }
            ],
            model="llama-3.3-70b-versatile",
            response_format={"type": "json_object"},
            temperature=0.1,
            max_tokens=256,
        )
        response_content = chat_completion.choices[0].message.content
        return json.loads(response_content)
    except Exception as e:
        return {"is_sarcastic": False, "explanation": f"Error during analysis: {str(e)}"}
