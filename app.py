import streamlit as st
import pandas as pd
from llm_router import analyze_sarcasm
import time
import os
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="Sarcasm Detector", page_icon="🎭", layout="wide")

# Custom CSS for Glassmorphism and animations
st.markdown("""
<style>
    /* Main Background */
    .stApp {
        background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
        font-family: 'Inter', sans-serif;
    }
    
    /* Center aligning main content */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
    
    /* Header typography */
    h1 {
        color: #fff !important;
        font-weight: 800;
        text-align: center;
        margin-bottom: 0.5rem;
    }
    
    p.subtitle {
        color: #d1d5db;
        text-align: center;
        font-size: 1.1rem;
        margin-bottom: 2rem;
    }

    /* Glassmorphism Containers */
    .glass-container {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(10px);
        -webkit-backdrop-filter: blur(10px);
        border-radius: 15px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        padding: 2rem;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.3);
        margin-bottom: 1.5rem;
        color: #fff;
    }
    
    /* Text input styling overrides */
    div[data-baseweb="textarea"] > div {
        background-color: rgba(0,0,0,0.2) !important;
        border: 1px solid rgba(255,255,255,0.2) !important;
        color: white !important;
    }
    textarea {
        color: white !important;
    }
    
    /* Result styling */
    .sarcastic-result {
        color: #ff6b6b;
        font-weight: 700;
        font-size: 1.8rem;
    }
    
    .literal-result {
        color: #51cf66;
        font-weight: 700;
        font-size: 1.8rem;
    }
    
    .explanation {
        color: #f1f3f5;
        font-size: 1.1rem;
        margin-top: 15px;
        background: rgba(0, 0, 0, 0.2);
        padding: 15px;
        border-radius: 8px;
        border-left: 4px solid #4dabf7;
    }

    /* Style dataframe */
    .stDataFrame {
        border-radius: 10px !important;
        overflow: hidden !important;
    }
</style>
""", unsafe_allow_html=True)

st.markdown("<h1>🎭 Sarcasm Detection AI</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>Powered by Groq's model</p>", unsafe_allow_html=True)

if not os.environ.get("GROQ_API_KEY") or os.environ.get("GROQ_API_KEY") == "your_groq_api_key_here":
    st.warning("⚠️ Please provide your Groq API key in the `.env` file to use the application. After saving your key, restart the app or refresh the page.", icon="🔑")
    st.stop()

tab1, tab2 = st.tabs(["💬 Individual Analysis", "📂 Bulk Upload (CSV)"])

with tab1:
    st.markdown("<div class='glass-container'>", unsafe_allow_html=True)
    st.subheader("Analyze a single statement")
    user_input = st.text_area("Enter text here...", height=120, placeholder="e.g. Oh great, another meeting. Exactly what I needed!")
    
    if st.button("Detect Sarcasm", use_container_width=True, type="primary"):
        if user_input.strip():
            with st.spinner("Analyzing semantics via Groq..."):
                result = analyze_sarcasm(user_input)
                
            st.markdown("</div>", unsafe_allow_html=True) # close previous block
            st.markdown("<div class='glass-container'>", unsafe_allow_html=True)
            
            is_sarcastic = result.get("is_sarcastic", False)
            explanation = result.get("explanation", "No explanation provided.")
            
            # Simple error catching pattern from our llm_router
            if "Error during analysis" in explanation:
                st.error(explanation)
            else:
                if is_sarcastic:
                    st.markdown("<span class='sarcastic-result'>🎭 Sarcastic!</span>", unsafe_allow_html=True)
                else:
                    st.markdown("<span class='literal-result'>🤖 Literal</span>", unsafe_allow_html=True)
                    
                st.markdown(f"<div class='explanation'><strong>Explanation:</strong><br>{explanation}</div>", unsafe_allow_html=True)
                
            st.markdown("</div>", unsafe_allow_html=True)
        else:
            st.error("Please enter some text to analyze.")
    else:
        st.markdown("</div>", unsafe_allow_html=True)

with tab2:
    st.markdown("<div class='glass-container'>", unsafe_allow_html=True)
    st.subheader("Upload CSV for Bulk Analysis")
    st.markdown("Upload a CSV file containing a column named **'text'**.")
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
    
    if uploaded_file is not None:
        try:
            df = pd.read_csv(uploaded_file)
            if 'text' not in df.columns:
                st.error("CSV must contain a column named 'text'!")
            else:
                st.write(f"Loaded {len(df)} rows.")
                if st.button("Process Batch", use_container_width=True, type="primary"):
                    progress_bar = st.progress(0)
                    status_text = st.empty()
                    
                    results_sarcastic = []
                    results_explanation = []
                    
                    for idx, row in df.iterrows():
                        status_text.text(f"Processing row {idx + 1}/{len(df)}...")
                        
                        res = analyze_sarcasm(str(row['text']))
                        results_sarcastic.append(res.get("is_sarcastic", False))
                        results_explanation.append(res.get("explanation", ""))
                        
                        progress_bar.progress((idx + 1) / len(df))
                        time.sleep(0.1) # Small sleep to avoid instant rate limiting issues
                    
                    status_text.text("Finalizing results...")
                    df['is_sarcastic'] = results_sarcastic
                    df['explanation'] = results_explanation
                    
                    st.success("Batch Processing Complete!")
                    st.dataframe(df, use_container_width=True)
                    
                    csv = df.to_csv(index=False).encode('utf-8')
                    st.download_button(
                        label="Download Results as CSV",
                        data=csv,
                        file_name='sarcasm_results.csv',
                        mime='text/csv',
                    )
        except Exception as e:
            st.error(f"Error reading CSV: {e}")
            
    st.markdown("</div>", unsafe_allow_html=True)
