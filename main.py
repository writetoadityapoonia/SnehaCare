import os
import streamlit as st
from groq import Groq

# -----------------------------
# DIRECT API KEY IN CODE
# Replace with your NEW Groq key
# -----------------------------
api_key = "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".strip()

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
# Validate Key
# -----------------------------
if not api_key or not api_key.startswith("gsk_"):
    st.error("Invalid or missing Groq API key.")
    st.stop()

# -----------------------------
# Groq Client
# -----------------------------
client = Groq(api_key=api_key)

# -----------------------------
# Full Styling
# -----------------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Fraunces:wght@600;700&family=Plus+Jakarta+Sans:wght@400;500;600&display=swap');

:root {
    --teal-50: #f0fdfa;
    --teal-100: #ccfbf1;
    --teal-500: #0d9488;
    --teal-600: #0f766e;
    --ink-900: #0f172a;
}

html, body, .stApp {
    background: radial-gradient(circle at 10% 10%, #f0fdfa 0%, #ffffff 50%, #f0fdfa 100%);
    color: var(--ink-900);
    font-family: 'Plus Jakarta Sans', sans-serif;
}

h1 {
    font-family: 'Fraunces', serif;
    font-size: 48px;
}

.hero {
    display: grid;
    grid-template-columns: 2fr 1fr;
    gap: 25px;
    margin-bottom: 30px;
}

.hero-card, .mini-card, .alert {
    background: white;
    padding: 18px;
    border-radius: 18px;
    box-shadow: 0 8px 25px rgba(0,0,0,0.05);
}

.chips {
    display: flex;
    gap: 10px;
    flex-wrap: wrap;
}

.chip {
    background: #f0fdfa;
    color: #0f766e;
    padding: 6px 12px;
    border-radius: 999px;
    font-size: 13px;
}

.card-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit,minmax(200px,1fr));
    gap: 15px;
}

@media (max-width: 900px) {
    .hero {
        grid-template-columns: 1fr;
    }
}
</style>
""", unsafe_allow_html=True)

# -----------------------------
# Header
# -----------------------------
st.markdown(f"""
<div class="hero">
    <div>
        <h1>🩺 HealthCare Bot</h1>
        <p>Describe symptoms, age, and duration for quick health guidance.</p>

        <div class="chips">
            <span class="chip">{MODEL_NAME}</span>
            <span class="chip">Groq Powered</span>
            <span class="chip">Instant Answers</span>
        </div>
    </div>

    <div class="hero-card">
        <h3>Before you start</h3>
        <ul>
            <li>Mention age</li>
            <li>Tell symptoms clearly</li>
            <li>Say how long</li>
            <li>Any medicines?</li>
        </ul>
    </div>
</div>
""", unsafe_allow_html=True)

# -----------------------------
# Safety Note
# -----------------------------
st.markdown("""
<div class="alert">
⚠️ Informational only. For chest pain, breathing trouble, stroke signs, seek urgent medical help.
</div>
""", unsafe_allow_html=True)

# -----------------------------
# Help Cards
# -----------------------------
st.markdown("""
<div class="card-grid">
    <div class="mini-card">Possible causes</div>
    <div class="mini-card">Self-care tips</div>
    <div class="mini-card">When to see doctor</div>
</div>
""", unsafe_allow_html=True)

# -----------------------------
# Session Chat
# -----------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# -----------------------------
# AI Function
# -----------------------------
def ask_groq(messages):
    system_prompt = {
        "role": "system",
        "content": """
You are a careful healthcare assistant.

Rules:
- No final diagnosis.
- Give likely causes.
- Give self-care advice.
- Mention emergency signs.
- Keep concise and clear.
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
# Input
# -----------------------------
prompt = st.chat_input("Describe symptoms, age, duration...")

if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.markdown(prompt)

    try:
        with st.chat_message("assistant"):
            with st.spinner("Analyzing..."):
                reply = ask_groq(st.session_state.messages)
                st.markdown(reply)

        st.session_state.messages.append({"role": "assistant", "content": reply})

    except Exception as e:
        st.error(f"Error: {e}")
