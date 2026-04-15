# 🎭 Sarcasm Detection AI
**A Lightning-Fast, AI-Powered Web Application to Detect Sarcasm in Text**

![Python](https://img.shields.io/badge/python-3.10+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat&logo=streamlit&logoColor=white)
![Groq](https://img.shields.io/badge/Groq-LPU-f55a3c.svg)
![Llama 3](https://img.shields.io/badge/Llama_3-70B-1877F2?style=flat)

---

## 📖 What is this?
Have you ever read a text message, an online review, or a frantic email and thought to yourself: *"Are they being serious right now, or are they joking?"* 

Sarcasm is notoriously difficult for computers (and sometimes people!) to understand because it relies on context, tone, and irony. 

**This project fixes that.** 

We built a beautiful, modern web application that uses an incredibly smart Artificial Intelligence (Llama 3, running on Groq's lightning-fast hardware) to read a sentence and determine if it's sarcastic. Not only does it give you a "Yes" or "No", but it also **explains exactly why** it thinks the phrase is sarcastic!

## 🌟 Key Features

* **💬 Single Statement Analysis**: Type or paste any phrase into the text box and get an instant AI judgment letting you know if the phrase was meant to be taken literally, or if it was steeped in heavy sarcasm.
* **📂 Bulk Data Upload (CSV)**: Have thousands of tweets, reviews, or emails you need to analyze? Upload a single Excel/CSV file and the AI will rapidly process every single line. It outputs a brand new file with the AI's verdicts and explanations attached!
* **🎨 Premium Glassmorphism UI**: A gorgeous, animated, and dark-themed design that looks and feels like a modern startup product. 
* **⚡ Blazing Fast Speeds**: Powered by the Groq API, the AI's processing doesn't bottleneck, handling massive context generation in mere milliseconds.

---

## 🛠️ How It Works (The Tech Stack)

Under the hood, this application uses a few incredibly powerful pieces of technology:
1. **[Streamlit](https://streamlit.io/):** The engine that builds the beautiful web interface you see and interact with. 
2. **[Groq API](https://groq.com/):** Instead of standard graphics cards (GPUs), Groq uses customized processor chips built specifically for AI math. This makes the AI "think" significantly faster than standard ChatGPT.
3. **Llama 3 (from Meta):** The actual Artificial Intelligence "brain". We engineered specific system prompts directing it to act as an expert linguist analyzing irony and internet figures of speech.

---

## 🚀 Getting Started (Run it yourself!)

### Prerequisites
You don't need a supercomputer to run this! You just need:
1. A computer with Python installed.
2. A free API key from [Groq Console](https://console.groq.com/keys).

### Installation Instructions

1. **Open a terminal/command prompt** and navigate to this folder.
2. **Install the required libraries** by running:
   ```bash
   pip install -r requirements.txt
   ```
3. **Add your API Key**: 
   - Open the `.env` file located in this folder.
   - Replace the placeholder text with your actual Groq API key:
     `GROQ_API_KEY=gsk_your_real_key_goes_here`
4. **Launch the application!**
   Run the following command in your terminal:
   ```bash
   streamlit run app.py
   ```
   *Your web browser will automatically open to the Sarcasm Detection dashboard!*

---

## 📈 CSV Upload Guide
If you want to use the "**Bulk Upload**" tab, your data must be inside a `.csv` file format. 
The only strict requirement is that your file **MUST** contain a column named `text` at the very top. 

Here is an example of what it should look like inside:
```csv
id,text
1,"Oh brilliant, another software update that will slow down my phone. Just what I needed today."
2,"The package was delivered exactly on time."
3,"I absolutely love waiting in line at the DMV for three hours."
```
Once uploaded, just click **Process Batch** and download your newly annotated file!

---
*Created by an AI Engineer blending modern linguistics with extreme inference speed architecture.*
