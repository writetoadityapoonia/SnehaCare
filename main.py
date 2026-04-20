import streamlit as st
from groq import Groq

# ==================================================
# PAGE CONFIG
# ==================================================
st.set_page_config(
    page_title="Health AI Chatbot",
    page_icon="🩺",
    layout="centered"
)

# ==================================================
# API KEY & MODEL
# ==================================================
api_key = "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"
MODEL_NAME = "llama-3.3-70b-versatile"
client = Groq(api_key=api_key)

# ==================================================
# CSS - MINIMAL
# ==================================================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

* {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}

html, body, .stApp {
    background: #fafafa !important;
    font-family: 'Inter', sans-serif !important;
    color: #111 !important;
}

[data-testid="stHeader"],
[data-testid="stToolbar"],
footer, header {
    display: none !important;
}

.main .block-container {
    padding-top: 32px !important;
    padding-bottom: 100px !important;
    max-width: 720px !important;
}

[data-testid="stBottom"] {
    background: #fafafa !important;
    border-top: 1px solid #ebebeb !important;
}

[data-testid="stChatInput"] textarea {
    font-family: 'Inter', sans-serif !important;
    font-size: 14px !important;
    color: #111 !important;
    background: #fff !important;
}

/* ── TOP BAR ── */
.topbar {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding-bottom: 24px;
    border-bottom: 1px solid #ebebeb;
    margin-bottom: 32px;
}

.topbar-left {
    display: flex;
    align-items: center;
    gap: 10px;
}

.topbar-dot {
    width: 10px;
    height: 10px;
    background: #22c55e;
    border-radius: 50%;
}

.topbar-name {
    font-size: 15px;
    font-weight: 600;
    color: #111;
    letter-spacing: -0.2px;
}

.topbar-model {
    font-size: 12px;
    color: #888;
    font-weight: 400;
    background: #f0f0f0;
    padding: 4px 10px;
    border-radius: 999px;
}

/* ── HERO ── */
.hero {
    margin-bottom: 36px;
}

.hero-label {
    font-size: 12px;
    font-weight: 600;
    color: #888;
    letter-spacing: 1px;
    text-transform: uppercase;
    margin-bottom: 10px;
}

.hero-title {
    font-size: 36px;
    font-weight: 700;
    color: #111;
    line-height: 1.15;
    letter-spacing: -0.8px;
    margin-bottom: 12px;
}

.hero-title span {
    color: #2563eb;
}

.hero-sub {
    font-size: 14px;
    color: #666;
    line-height: 1.75;
    max-width: 480px;
    font-weight: 400;
}

/* ── PILLS ── */
.pills {
    display: flex;
    gap: 8px;
    flex-wrap: wrap;
    margin-top: 18px;
}

.pill {
    background: #fff;
    border: 1px solid #e0e0e0;
    color: #444;
    padding: 6px 14px;
    border-radius: 999px;
    font-size: 12px;
    font-weight: 500;
}

/* ── DIVIDER ── */
.divider {
    height: 1px;
    background: #ebebeb;
    margin: 28px 0;
}

/* ── TIPS GRID ── */
.tips-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 12px;
    margin-bottom: 28px;
}

.tip-card {
    background: #fff;
    border: 1px solid #e8e8e8;
    border-radius: 14px;
    padding: 18px;
}

.tip-card-icon {
    font-size: 18px;
    margin-bottom: 8px;
}

.tip-card-title {
    font-size: 13px;
    font-weight: 600;
    color: #111;
    margin-bottom: 4px;
}

.tip-card-desc {
    font-size: 12px;
    color: #888;
    line-height: 1.6;
}

/* ── ALERT ── */
.alert {
    background: #fff;
    border: 1px solid #fca5a5;
    border-left: 3px solid #ef4444;
    border-radius: 12px;
    padding: 14px 16px;
    margin-bottom: 28px;
    display: flex;
    gap: 10px;
    align-items: flex-start;
}

.alert-icon {
    font-size: 15px;
    flex-shrink: 0;
    margin-top: 1px;
}

.alert-body {
    font-size: 12.5px;
    color: #555;
    line-height: 1.65;
}

.alert-body strong {
    color: #b91c1c;
    font-weight: 600;
    display: block;
    margin-bottom: 2px;
    font-size: 13px;
}

/* ── SECTION LABEL ── */
.section-label {
    font-size: 11px;
    font-weight: 700;
    color: #aaa;
    letter-spacing: 1.2px;
    text-transform: uppercase;
    margin-bottom: 16px;
}

/* ── CHAT MESSAGES ── */
[data-testid="stChatMessage"] {
    background: #fff !important;
    border: 1px solid #ebebeb !important;
    border-radius: 14px !important;
    padding: 16px !important;
    margin-bottom: 10px !important;
    box-shadow: none !important;
}

/* ── INCLUDE LIST ── */
.include-list {
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
    margin-bottom: 28px;
}

.include-item {
    background: #fff;
    border: 1px solid #e8e8e8;
    border-radius: 8px;
    padding: 7px 13px;
    font-size: 12px;
    color: #555;
    font-weight: 500;
    display: flex;
    align-items: center;
    gap: 6px;
}

@media (max-width: 640px) {
    .hero-title { font-size: 28px; }
    .tips-grid  { grid-template-columns: 1fr; }
}
</style>
""", unsafe_allow_html=True)

# ==================================================
# TOP BAR
# ==================================================
st.markdown(f"""
<div class="topbar">
    <div class="topbar-left">
        <div class="topbar-dot"></div>
        <span class="topbar-name">Health AI Chatbot</span>
    </div>
    <span class="topbar-model">{MODEL_NAME}</span>
</div>
""", unsafe_allow_html=True)

# ==================================================
# HERO
# ==================================================
st.markdown("""
<div class="hero">
    <div class="hero-label">🩺 Your health companion</div>
    <div class="hero-title">Ask anything about<br><span>your health</span></div>
    <div class="hero-sub">
        Describe your symptoms and get clear guidance on possible
        causes, self-care tips, and when to see a doctor.
    </div>
    <div class="pills">
        <span class="pill">🔒 Private</span>
        <span class="pill">⚡ Instant</span>
        <span class="pill">🤝 Empathetic</span>
        <span class="pill">🌍 Global</span>
    </div>
</div>
""", unsafe_allow_html=True)

# ==================================================
# DIVIDER
# ==================================================
st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# ==================================================
# TIPS CARDS
# ==================================================
st.markdown('<div class="section-label">How I can help</div>', unsafe_allow_html=True)

st.markdown("""
<div class="tips-grid">
    <div class="tip-card">
        <div class="tip-card-icon">🔍</div>
        <div class="tip-card-title">Symptom Analysis</div>
        <div class="tip-card-desc">Get possible causes explained in plain, simple language.</div>
    </div>
    <div class="tip-card">
        <div class="tip-card-icon">💊</div>
        <div class="tip-card-title">Self-Care Tips</div>
        <div class="tip-card-desc">Practical home-care advice to help manage mild conditions.</div>
    </div>
    <div class="tip-card">
        <div class="tip-card-icon">🚨</div>
        <div class="tip-card-title">Urgent Signs</div>
        <div class="tip-card-desc">I'll flag symptoms that need immediate medical attention.</div>
    </div>
    <div class="tip-card">
        <div class="tip-card-icon">🩻</div>
        <div class="tip-card-title">Doctor Guidance</div>
        <div class="tip-card-desc">Know when and which specialist to visit for your concern.</div>
    </div>
</div>
""", unsafe_allow_html=True)

# ==================================================
# INCLUDE LIST
# ==================================================
st.markdown('<div class="section-label">For best results, include</div>', unsafe_allow_html=True)

st.markdown("""
<div class="include-list">
    <span class="include-item">👤 Age &amp; gender</span>
    <span class="include-item">🌍 Country</span>
    <span class="include-item">📋 Symptoms</span>
    <span class="include-item">⏱ Duration</span>
    <span class="include-item">💊 Medications</span>
    <span class="include-item">📈 Sudden or gradual</span>
</div>
""", unsafe_allow_html=True)

# ==================================================
# ALERT
# ==================================================
st.markdown("""
<div class="alert">
    <div class="alert-icon">⚠️</div>
    <div class="alert-body">
        <strong>Emergency Warning</strong>
        For chest pain, trouble breathing, stroke symptoms, or severe bleeding —
        call emergency services immediately. This tool does not replace a real doctor.
    </div>
</div>
""", unsafe_allow_html=True)

# ==================================================
# CHAT DIVIDER
# ==================================================
st.markdown('<div class="section-label">💬 Conversation</div>', unsafe_allow_html=True)

# ==================================================
# CHAT MEMORY
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
        "content": (
            "You are Health AI Chatbot — a careful, empathetic, and knowledgeable healthcare assistant.\n\n"
            "Guidelines:\n"
            "- NEVER provide a definitive diagnosis.\n"
            "- Always mention 2-4 possible causes clearly.\n"
            "- Provide practical, safe self-care suggestions.\n"
            "- Clearly flag any red-flag or emergency warning signs.\n"
            "- Recommend seeing a doctor when appropriate.\n"
            "- Be warm, professional, and easy to understand.\n"
            "- Use markdown for clear structure (headers, bullets).\n"
            "- Keep responses concise but thorough.\n"
            "- End with a brief disclaimer that this is not medical advice."
        )
    }
    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[system_prompt] + messages,
        temperature=0.4,
        max_completion_tokens=900
    )
    return response.choices[0].message.content

# ==================================================
# CHAT INPUT
# ==================================================
prompt = st.chat_input("Describe your symptoms, age, and duration...")

if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.markdown(prompt)

    try:
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                reply = get_reply(st.session_state.messages)
                st.markdown(reply)

        st.session_state.messages.append({"role": "assistant", "content": reply})

    except Exception as e:
        st.error(f"Error: {e}")
