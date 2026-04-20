import os
import streamlit as st
from dotenv import load_dotenv
from groq import Groq

# -----------------------------
# Load .env
# -----------------------------
load_dotenv(dotenv_path=".env")

MODEL_NAME = "llama-3.3-70b-versatile"

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(
    page_title="HealthCare (Groq)",
    page_icon="🩺",
    layout="centered"
)

# -----------------------------
# Load API Key
# -----------------------------
api_key = os.getenv("GROQ_API_KEY", "").strip()

if not api_key:
    st.error("Missing GROQ_API_KEY in .env file")
    st.stop()

# -----------------------------
# Groq Client
# -----------------------------
client = Groq(api_key=api_key)

# -----------------------------
# Full Original Styling
# -----------------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Fraunces:wght@600;700&family=Plus+Jakarta+Sans:wght@400;500;600&display=swap');

:root {
    --teal-50: #f0fdfa;
    --teal-100: #ccfbf1;
    --teal-200: #99f6e4;
    --teal-500: #0d9488;
    --teal-600: #0f766e;
    --teal-700: #115e59;
    --ink-900: #0f172a;
    --ink-700: #475569;
}

html, body {
    background: radial-gradient(circle at 10% 10%, #f0fdfa 0%, #ffffff 50%, #f0fdfa 100%);
}

.stApp {
    background: radial-gradient(circle at 10% 10%, #f0fdfa 0%, #ffffff 50%, #f0fdfa 100%);
    color: var(--ink-900);
    font-family: 'Plus Jakarta Sans', sans-serif;
}

[data-testid="stHeader"],
[data-testid="stToolbar"],
footer,
header {
    background: transparent;
}

[data-testid="stBottom"] {
    background-color: #ffffff !important;
}

[data-testid="stChatInput"] {
    background-color: #ffffff !important;
    border: 1px solid var(--teal-100) !important;
    border-radius: 16px !important;
    box-shadow: 0 -10px 40px rgba(0,0,0,0.02) !important;
}

[data-testid="stChatInput"] textarea {
    font-family: 'Plus Jakarta Sans', sans-serif !important;
    color: var(--ink-900) !important;
}

.stButton button,
.stDownloadButton button,
.stFormSubmitButton button {
    background: linear-gradient(135deg, var(--teal-500), var(--teal-600));
    color: white;
    border: none;
}

.hero {
    display: grid;
    grid-template-columns: 2fr 1fr;
    gap: 25px;
    margin-top: 20px;
    margin-bottom: 30px;
}

.hero-card {
    background: white;
    padding: 20px;
    border-radius: 18px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.05);
}

.eyebrow {
    color: var(--teal-600);
    font-weight: 700;
    font-size: 14px;
    text-transform: uppercase;
    letter-spacing: 1px;
}

h1 {
    font-family: 'Fraunces', serif;
    font-size: 48px;
    margin-bottom: 8px;
}

.chips {
    display: flex;
    gap: 10px;
    flex-wrap: wrap;
    margin-top: 12px;
}

.chip {
    background: var(--teal-50);
    color: var(--teal-700);
    padding: 6px 12px;
    border-radius: 999px;
    font-size: 13px;
}

.alert {
    background: white;
    border-left: 5px solid #0d9488;
    padding: 15px;
    border-radius: 12px;
    margin-bottom: 25px;
}

.section-title {
    font-size: 22px;
    font-weight: 700;
    margin-bottom: 14px;
}

.card-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit,minmax(200px,1fr));
    gap: 15px;
    margin-bottom: 25px;
}

.mini-card {
    background: white;
    padding: 16px;
    border-radius: 16px;
    box-shadow: 0 6px 18px rgba(0,0,0,0.04);
}

@media (max-width: 900px) {
    .hero {
        grid-template-columns: 1fr;
    }
}
</style>
""", unsafe_allow_html=True)

# -----------------------------
# Header Section
# -----------------------------
st.markdown(f"""
<div class="hero">
    <div>
        <div class="eyebrow">HealthCare Assistant</div>
        <h1>HealthCare Bot</h1>
        <p>
            Share your symptoms, age, and duration. I’ll provide possible causes,
            self-care tips, and when to seek urgent care.
        </p>
        <div class="chips">
            <span class="chip">Model: {MODEL_NAME}</span>
            <span class="chip">Secure API via .env</span>
            <span class="chip">Fast AI Guidance</span>
        </div>
    </div>

    <div class="hero-card">
        <h3>Before we start</h3>
        <ul>
            <li>Include age</li>
            <li>Mention country</li>
            <li>List symptoms clearly</li>
            <li>Say sudden or gradual</li>
        </ul>
    </div>
</div>
""", unsafe_allow_html=True)

# -----------------------------
# Safety Box
# -----------------------------
st.markdown("""
<div class="alert">
<strong>⚠️ Safety Note:</strong> This bot is informational only.
For chest pain, breathing trouble, stroke signs, heavy bleeding —
seek emergency medical care immediately.
</div>
""", unsafe_allow_html=True)

# -----------------------------
# Help Section
# -----------------------------
st.markdown("""
<div class="section-title">How I Can Help</div>

<div class="card-grid">
    <div class="mini-card">Explain likely causes</div>
    <div class="mini-card">Suggest home care steps</div>
    <div class="mini-card">Tell when to see doctor</div>
</div>
""", unsafe_allow_html=True)

# -----------------------------
# Chat Memory
# -----------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# -----------------------------
# Show Old Messages
# -----------------------------
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# -----------------------------
# Chat Input
# -----------------------------
prompt = st.chat_input("Describe your symptoms, age, and duration...")

# -----------------------------
# AI Response
# -----------------------------
def ask_groq(messages):
    system_prompt = {
        "role": "system",
        "content": """
You are a careful healthcare assistant.

Rules:
- Do not claim final diagnosis.
- Give possible causes.
- Give self-care tips.
- Mention warning signs.
- Be clear and concise.
"""
    }

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[system_prompt] + messages,
        temperature=0.4,
        max_completion_tokens=900
    )

    return response.choices[0].message.content

# -----------------------------
# Run Chat
# -----------------------------
if prompt:
    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })

    with st.chat_message("user"):
        st.markdown(prompt)

    try:
        with st.chat_message("assistant"):
            with st.spinner("Analyzing..."):
                reply = ask_groq(st.session_state.messages)
                st.markdown(reply)

        st.session_state.messages.append({
            "role": "assistant",
            "content": reply
        })

    except Exception as e:
        st.error(f"Error: {e}")
