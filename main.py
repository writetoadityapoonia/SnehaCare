import streamlit as st
from groq import Groq

# ==================================================
# CONFIG
# ==================================================
st.set_page_config(
    page_title="HealthCare (Groq)",
    page_icon="🩺",
    layout="centered"
)

# ==================================================
# API KEY
# Replace with your NEW Groq key
# ==================================================
api_key = "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".strip()

MODEL_NAME = "llama-3.3-70b-versatile"

if not api_key.startswith("gsk_"):
    st.error("Please add a valid Groq API key.")
    st.stop()

client = Groq(api_key=api_key)

# ==================================================
# PREMIUM ORIGINAL UI
# ==================================================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Fraunces:wght@600;700&family=Plus+Jakarta+Sans:wght@400;500;600&display=swap');

:root{
--teal-50:#f0fdfa;
--teal-100:#ccfbf1;
--teal-500:#0d9488;
--teal-600:#0f766e;
--teal-700:#115e59;
--ink-900:#0f172a;
--ink-700:#475569;
}

html, body{
background: radial-gradient(circle at 10% 10%, #f0fdfa 0%, #ffffff 50%, #f0fdfa 100%);
}

.stApp{
background: radial-gradient(circle at 10% 10%, #f0fdfa 0%, #ffffff 50%, #f0fdfa 100%);
font-family:'Plus Jakarta Sans', sans-serif;
color:var(--ink-900);
}

[data-testid="stHeader"],
[data-testid="stToolbar"],
footer,
header{
background:transparent;
}

[data-testid="stBottom"]{
background:#ffffff !important;
}

[data-testid="stChatInput"]{
background:#ffffff !important;
border:1px solid var(--teal-100) !important;
border-radius:16px !important;
box-shadow:0 -10px 40px rgba(0,0,0,0.02) !important;
}

[data-testid="stChatInput"] textarea{
font-family:'Plus Jakarta Sans', sans-serif !important;
color:var(--ink-900) !important;
}

.hero{
display:grid;
grid-template-columns:1.6fr 1fr;
gap:24px;
align-items:stretch;
margin-bottom:28px;
}

.eyebrow{
font-size:13px;
font-weight:700;
letter-spacing:1px;
color:var(--teal-600);
text-transform:uppercase;
}

.hero h1{
font-family:'Fraunces', serif;
font-size:52px;
line-height:1.05;
margin:10px 0;
}

.hero p{
font-size:16px;
line-height:1.7;
color:var(--ink-700);
}

.hero-card{
background:white;
padding:24px;
border-radius:22px;
box-shadow:0 14px 40px rgba(2,8,23,.06);
}

.chips{
display:flex;
gap:10px;
flex-wrap:wrap;
margin-top:18px;
}

.chip{
background:var(--teal-50);
color:var(--teal-700);
padding:8px 14px;
border-radius:999px;
font-size:13px;
font-weight:600;
}

.alert{
background:white;
padding:16px 18px;
border-radius:18px;
border:1px solid var(--teal-100);
margin-bottom:24px;
}

.section-title{
font-size:22px;
font-weight:700;
margin-bottom:14px;
}

.card-grid{
display:grid;
grid-template-columns:repeat(auto-fit,minmax(220px,1fr));
gap:14px;
margin-bottom:26px;
}

.mini-card{
background:white;
padding:18px;
border-radius:18px;
box-shadow:0 10px 24px rgba(2,8,23,.04);
}

@media (max-width:900px){
.hero{
grid-template-columns:1fr;
}
.hero h1{
font-size:42px;
}
}
</style>
""", unsafe_allow_html=True)

# ==================================================
# HERO SECTION
# ==================================================
st.markdown(f"""
<div class="hero">
<div>
<div class="eyebrow">HealthCare Assistant</div>
<h1>HealthCare Bot</h1>

<p>
Share your symptoms, age, and how long you have felt them.
I’ll offer possible next steps, self-care tips,
and when to seek urgent help.
</p>

<div class="chips">
<span class="chip">Model: {MODEL_NAME}</span>
<span class="chip">Fast Responses</span>
<span class="chip">Medical Guidance</span>
</div>
</div>

<div class="hero-card">
<h3>Before we start</h3>
<ul>
<li>Include your age</li>
<li>Mention country</li>
<li>Describe symptoms clearly</li>
<li>Sudden or gradual?</li>
<li>Any medicines?</li>
</ul>
</div>
</div>
""", unsafe_allow_html=True)

# ==================================================
# ALERT
# ==================================================
st.markdown("""
<div class="alert">
<strong>Safety note:</strong>
This chatbot is informational only.
If you have chest pain, breathing trouble,
stroke signs, or heavy bleeding,
seek emergency care immediately.
</div>
""", unsafe_allow_html=True)

# ==================================================
# FEATURE CARDS
# ==================================================
st.markdown("""
<div class="section-title">How I can help</div>

<div class="card-grid">
<div class="mini-card">Explain likely causes and what to watch for.</div>
<div class="mini-card">Suggest safe self-care for 24–48 hours.</div>
<div class="mini-card">Flag urgent symptoms needing doctor help.</div>
</div>
""", unsafe_allow_html=True)

# ==================================================
# CHAT MEMORY
# ==================================================
if "messages" not in st.session_state:
    st.session_state.messages = []

# ==================================================
# SHOW HISTORY
# ==================================================
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# ==================================================
# AI FUNCTION
# ==================================================
def get_reply(messages):
    system_prompt = {
        "role": "system",
        "content": """
You are HealthCare, a careful healthcare assistant.

Rules:
- Do not claim final diagnosis.
- Give likely causes only.
- Mention warning signs.
- Suggest self-care if safe.
- Keep answers clear and concise.
"""
    }

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[system_prompt] + messages,
        temperature=0.4,
        max_completion_tokens=900
    )

    return response.choices[0].message.content

# ==================================================
# INPUT
# ==================================================
prompt = st.chat_input("Describe symptoms, age, duration...")

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
                reply = get_reply(st.session_state.messages)
                st.markdown(reply)

        st.session_state.messages.append({
            "role": "assistant",
            "content": reply
        })

    except Exception as e:
        st.error(f"Error: {e}")
[data-testid="stChatInput"] textarea {
    font-family: 'Plus Jakarta Sans', sans-serif !important;
    background-color: transparent !important;
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
    display:grid;
    grid-template-columns:1.6fr 1fr;
    gap:24px;
    align-items:stretch;
    margin-bottom:28px;
}

.eyebrow {
    font-size:13px;
    font-weight:700;
    letter-spacing:1px;
    color:var(--teal-600);
    text-transform:uppercase;
}

.hero h1 {
    font-family:'Fraunces', serif;
    font-size:52px;
    line-height:1.05;
    margin:10px 0;
}

.hero p {
    color:var(--ink-700);
    font-size:16px;
    line-height:1.7;
}

.hero-card {
    background:white;
    border-radius:22px;
    padding:24px;
    box-shadow:0 14px 40px rgba(2,8,23,.06);
}

.chips {
    display:flex;
    gap:10px;
    flex-wrap:wrap;
    margin-top:18px;
}

.chip {
    background:var(--teal-50);
    color:var(--teal-700);
    padding:8px 14px;
    border-radius:999px;
    font-size:13px;
    font-weight:600;
}

.alert {
    background:white;
    border:1px solid var(--teal-100);
    border-radius:18px;
    padding:16px 18px;
    margin-bottom:24px;
}

.section-title {
    font-size:22px;
    font-weight:700;
    margin-bottom:14px;
}

.card-grid {
    display:grid;
    grid-template-columns:repeat(auto-fit,minmax(220px,1fr));
    gap:14px;
    margin-bottom:26px;
}

.mini-card {
    background:white;
    border-radius:18px;
    padding:18px;
    box-shadow:0 10px 24px rgba(2,8,23,.04);
}

@media (max-width:900px){
.hero{
grid-template-columns:1fr;
}
.hero h1{
font-size:42px;
}
}
</style>
""",
    unsafe_allow_html=True,
)

# ==================================================
# HERO SECTION
# ==================================================
st.markdown(
    f"""
<div class="hero">
    <div>
        <div class="eyebrow">HealthCare Assistant</div>
        <h1>HealthCare Bot</h1>
        <p>
            Share your symptoms, age, and how long you have felt them.
            I’ll offer possible next steps, self-care tips, and when to seek urgent help.
        </p>

        <div class="chips">
            <span class="chip">Model: {MODEL_NAME}</span>
            <span class="chip">Fast Responses</span>
            <span class="chip">Clean Guidance</span>
        </div>
    </div>

    <div class="hero-card">
        <h3>Before we start</h3>
        <ul>
            <li>Include your age</li>
            <li>Mention country</li>
            <li>Describe symptoms clearly</li>
            <li>Sudden or gradual?</li>
            <li>Any medicines?</li>
        </ul>
    </div>
</div>
""",
    unsafe_allow_html=True,
)

# ==================================================
# ALERT
# ==================================================
st.markdown(
    """
<div class="alert">
<strong>Safety note:</strong> Informational only. If you have chest pain,
breathing trouble, stroke signs, or heavy bleeding, seek emergency care immediately.
</div>
""",
    unsafe_allow_html=True,
)

# ==================================================
# FEATURE SECTION
# ==================================================
st.markdown(
    """
<div class="section-title">How I can help</div>

<div class="card-grid">
    <div class="mini-card">Explain possible causes and what to watch for.</div>
    <div class="mini-card">Suggest safe self-care steps for 24–48 hours.</div>
    <div class="mini-card">Flag symptoms needing urgent medical help.</div>
</div>
""",
    unsafe_allow_html=True,
)

# ==================================================
# CHAT HISTORY
# ==================================================
if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# ==================================================
# AI RESPONSE
# ==================================================
def get_reply(messages):
    system_prompt = {
        "role": "system",
        "content": """
You are HealthCare, a careful medical information assistant.

Rules:
- Give practical health guidance
- Mention likely causes, not final diagnosis
- Mention warning signs
- Keep concise and structured
"""
    }

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[system_prompt] + messages,
        temperature=0.4,
        max_completion_tokens=900
    )

    return response.choices[0].message.content

# ==================================================
# INPUT
# ==================================================
prompt = st.chat_input("Describe symptoms, age, duration...")

if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.markdown(prompt)

    try:
        with st.chat_message("assistant"):
            with st.spinner("Analyzing..."):
                reply = get_reply(st.session_state.messages)
                st.markdown(reply)

        st.session_state.messages.append({"role": "assistant", "content": reply})

    except Exception as e:
        st.error(f"Error: {e}")    border-radius: 18px;
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
