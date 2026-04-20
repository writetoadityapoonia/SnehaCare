import streamlit as st
from groq import Groq

# ==================================================
# PAGE CONFIG
# ==================================================
st.set_page_config(
    page_title="MediAssist AI",
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
# CSS
# ==================================================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800&family=Playfair+Display:wght@700;800&display=swap');

:root {
    --primary: #0ea5e9;
    --primary-dark: #0284c7;
    --primary-light: #e0f2fe;
    --accent: #06b6d4;
    --success: #10b981;
    --warning: #f59e0b;
    --danger: #ef4444;
    --bg: #f8fafc;
    --card: #ffffff;
    --text: #0f172a;
    --muted: #64748b;
    --border: #e2e8f0;
}

html, body, .stApp {
    background: linear-gradient(135deg, #f0f9ff 0%, #f8fafc 40%, #f0fdf4 100%) !important;
    font-family: 'Outfit', sans-serif !important;
    color: var(--text) !important;
}

[data-testid="stHeader"],
[data-testid="stToolbar"],
footer, header {
    display: none !important;
}

.main .block-container {
    padding-top: 24px !important;
    padding-bottom: 120px !important;
    max-width: 860px !important;
}

[data-testid="stBottom"] {
    background: rgba(255,255,255,0.95) !important;
    backdrop-filter: blur(20px) !important;
    border-top: 1px solid var(--border) !important;
}

[data-testid="stChatInput"] textarea {
    font-family: 'Outfit', sans-serif !important;
    font-size: 15px !important;
    border-radius: 16px !important;
    border: 2px solid var(--border) !important;
}

/* NAVBAR */
.navbar {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 16px 24px;
    background: rgba(255,255,255,0.9);
    backdrop-filter: blur(20px);
    border-radius: 20px;
    border: 1px solid var(--border);
    margin-bottom: 24px;
    box-shadow: 0 2px 16px rgba(0,0,0,0.04);
}

.nav-left {
    display: flex;
    align-items: center;
    gap: 12px;
}

.nav-icon {
    width: 40px;
    height: 40px;
    background: linear-gradient(135deg, #0ea5e9, #06b6d4);
    border-radius: 12px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 18px;
    box-shadow: 0 4px 12px rgba(14,165,233,0.3);
}

.nav-name {
    font-size: 18px;
    font-weight: 800;
    background: linear-gradient(135deg, #0284c7, #06b6d4);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}

.nav-badge {
    background: #e0f2fe;
    color: #0284c7;
    padding: 6px 14px;
    border-radius: 999px;
    font-size: 12px;
    font-weight: 700;
    border: 1px solid rgba(14,165,233,0.2);
}

/* HERO */
.hero-wrapper {
    background: linear-gradient(135deg, #0ea5e9 0%, #0284c7 60%, #06b6d4 100%);
    border-radius: 24px;
    padding: 40px 36px;
    margin-bottom: 20px;
    position: relative;
    overflow: hidden;
    box-shadow: 0 16px 48px rgba(14,165,233,0.28);
}

.hero-blob1 {
    position: absolute;
    top: -60px;
    right: -60px;
    width: 220px;
    height: 220px;
    background: rgba(255,255,255,0.07);
    border-radius: 50%;
    pointer-events: none;
}

.hero-blob2 {
    position: absolute;
    bottom: -50px;
    left: -30px;
    width: 180px;
    height: 180px;
    background: rgba(255,255,255,0.05);
    border-radius: 50%;
    pointer-events: none;
}

.hero-tag {
    display: inline-block;
    background: rgba(255,255,255,0.18);
    border: 1px solid rgba(255,255,255,0.3);
    color: white;
    padding: 5px 14px;
    border-radius: 999px;
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 1px;
    text-transform: uppercase;
    margin-bottom: 16px;
}

.hero-title {
    font-family: 'Playfair Display', serif;
    font-size: 46px;
    font-weight: 800;
    color: white;
    line-height: 1.1;
    margin-bottom: 14px;
}

.hero-title span {
    color: #bae6fd;
}

.hero-sub {
    font-size: 15px;
    color: rgba(255,255,255,0.85);
    line-height: 1.75;
    max-width: 500px;
    margin-bottom: 24px;
    font-weight: 400;
}

.hero-chips {
    display: flex;
    gap: 10px;
    flex-wrap: wrap;
}

.hero-chip {
    background: rgba(255,255,255,0.18);
    border: 1px solid rgba(255,255,255,0.28);
    color: white;
    padding: 7px 16px;
    border-radius: 999px;
    font-size: 12px;
    font-weight: 600;
}

/* INFO CARDS ROW */
.info-row {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 16px;
    margin-bottom: 20px;
}

.info-card {
    background: white;
    border-radius: 20px;
    padding: 22px;
    border: 1.5px solid var(--border);
    box-shadow: 0 4px 16px rgba(0,0,0,0.03);
}

.info-card-title {
    font-size: 14px;
    font-weight: 700;
    color: var(--text);
    margin-bottom: 12px;
    display: flex;
    align-items: center;
    gap: 8px;
}

.info-list {
    list-style: none;
    padding: 0;
    margin: 0;
}

.info-list li {
    font-size: 13px;
    color: var(--muted);
    padding: 5px 0;
    border-bottom: 1px solid #f1f5f9;
    display: flex;
    align-items: center;
    gap: 8px;
    font-weight: 500;
}

.info-list li:last-child {
    border-bottom: none;
}

.dot-blue  { color: #0ea5e9; font-size: 18px; line-height: 1; }
.dot-green { color: #10b981; font-size: 18px; line-height: 1; }

/* STATS */
.stats-row {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 14px;
    margin-bottom: 20px;
}

.stat-box {
    background: white;
    border-radius: 18px;
    padding: 20px 16px;
    text-align: center;
    border: 1.5px solid var(--border);
    box-shadow: 0 2px 10px rgba(0,0,0,0.02);
}

.stat-num {
    font-size: 26px;
    font-weight: 800;
    background: linear-gradient(135deg, #0ea5e9, #06b6d4);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}

.stat-lbl {
    font-size: 11px;
    color: var(--muted);
    font-weight: 600;
    margin-top: 4px;
    text-transform: uppercase;
    letter-spacing: 0.5px;
}

/* ALERT */
.alert-box {
    display: flex;
    align-items: flex-start;
    gap: 14px;
    background: #fffbeb;
    border: 1.5px solid #fde68a;
    border-left: 4px solid #f59e0b;
    border-radius: 18px;
    padding: 16px 20px;
    margin-bottom: 20px;
}

.alert-icon { font-size: 20px; margin-top: 2px; flex-shrink: 0; }

.alert-title {
    font-size: 14px;
    font-weight: 700;
    color: #78350f;
    margin-bottom: 4px;
}

.alert-text {
    font-size: 13px;
    color: #92400e;
    line-height: 1.6;
    font-weight: 400;
}

/* FEATURE CARDS */
.feat-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 14px;
    margin-bottom: 24px;
}

.feat-card {
    background: white;
    border-radius: 20px;
    padding: 22px 18px;
    border: 1.5px solid var(--border);
    box-shadow: 0 4px 16px rgba(0,0,0,0.03);
}

.feat-card-top {
    height: 3px;
    border-radius: 3px;
    margin: -22px -18px 18px;
    border-radius: 20px 20px 0 0;
}

.blue-bar  { background: linear-gradient(90deg, #0ea5e9, #06b6d4); }
.green-bar { background: linear-gradient(90deg, #10b981, #34d399); }
.orange-bar{ background: linear-gradient(90deg, #f59e0b, #fbbf24); }

.feat-icon  { font-size: 26px; margin-bottom: 10px; display: block; }
.feat-title { font-size: 14px; font-weight: 700; color: var(--text); margin-bottom: 6px; }
.feat-desc  { font-size: 12px; color: var(--muted); line-height: 1.6; }

/* DIVIDER */
.chat-divider {
    display: flex;
    align-items: center;
    gap: 12px;
    margin: 8px 0 20px;
}

.div-line { flex: 1; height: 1px; background: var(--border); }

.div-label {
    font-size: 11px;
    font-weight: 700;
    color: var(--muted);
    letter-spacing: 1px;
    text-transform: uppercase;
    white-space: nowrap;
}

/* CHAT */
[data-testid="stChatMessage"] {
    border-radius: 18px !important;
    padding: 14px !important;
    margin-bottom: 12px !important;
}
</style>
""", unsafe_allow_html=True)

# ==================================================
# NAVBAR
# ==================================================
st.markdown(f"""
<div class="navbar">
    <div class="nav-left">
        <div class="nav-icon">🩺</div>
        <span class="nav-name">MediAssist AI</span>
    </div>
    <div class="nav-badge">⚡ {MODEL_NAME}</div>
</div>
""", unsafe_allow_html=True)

# ==================================================
# HERO
# ==================================================
st.markdown("""
<div class="hero-wrapper">
    <div class="hero-blob1"></div>
    <div class="hero-blob2"></div>
    <div class="hero-tag">✦ AI-Powered Health Guidance</div>
    <div class="hero-title">Your Personal<br><span>Health Assistant</span></div>
    <div class="hero-sub">
        Share your symptoms and get smart, thoughtful guidance on possible
        causes, self-care steps, and when to seek professional medical help.
    </div>
    <div class="hero-chips">
        <span class="hero-chip">🔒 Private &amp; Secure</span>
        <span class="hero-chip">⚡ Instant Responses</span>
        <span class="hero-chip">🌍 Global Coverage</span>
    </div>
</div>
""", unsafe_allow_html=True)

# ==================================================
# STATS
# ==================================================
st.markdown("""
<div class="stats-row">
    <div class="stat-box">
        <div class="stat-num">70B</div>
        <div class="stat-lbl">Parameter Model</div>
    </div>
    <div class="stat-box">
        <div class="stat-num">&lt;2s</div>
        <div class="stat-lbl">Avg Response Time</div>
    </div>
    <div class="stat-box">
        <div class="stat-num">24/7</div>
        <div class="stat-lbl">Always Available</div>
    </div>
</div>
""", unsafe_allow_html=True)

# ==================================================
# INFO CARDS
# ==================================================
st.markdown("""
<div class="info-row">
    <div class="info-card">
        <div class="info-card-title">📋 Include these details</div>
        <ul class="info-list">
            <li><span class="dot-blue">•</span> Your age &amp; gender</li>
            <li><span class="dot-blue">•</span> Country or region</li>
            <li><span class="dot-blue">•</span> Describe symptoms clearly</li>
            <li><span class="dot-blue">•</span> Sudden or gradual onset?</li>
            <li><span class="dot-blue">•</span> Current medications</li>
            <li><span class="dot-blue">•</span> Duration of symptoms</li>
        </ul>
    </div>
    <div class="info-card">
        <div class="info-card-title">✅ What I can do</div>
        <ul class="info-list">
            <li><span class="dot-green">•</span> Explain possible causes</li>
            <li><span class="dot-green">•</span> Suggest safe self-care tips</li>
            <li><span class="dot-green">•</span> Flag urgent warning signs</li>
            <li><span class="dot-green">•</span> Guide when to see a doctor</li>
            <li><span class="dot-green">•</span> Provide clear explanations</li>
            <li><span class="dot-green">•</span> Answer follow-up questions</li>
        </ul>
    </div>
</div>
""", unsafe_allow_html=True)

# ==================================================
# ALERT
# ==================================================
st.markdown("""
<div class="alert-box">
    <div class="alert-icon">⚠️</div>
    <div>
        <div class="alert-title">Emergency Warning</div>
        <div class="alert-text">
            For chest pain, difficulty breathing, stroke symptoms, severe bleeding,
            or any life-threatening emergency — call emergency services or visit
            your nearest ER immediately. This AI does not replace professional medical advice.
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# ==================================================
# FEATURE CARDS
# ==================================================
st.markdown("""
<div class="feat-grid">
    <div class="feat-card">
        <div class="feat-card-top blue-bar"></div>
        <span class="feat-icon">🔍</span>
        <div class="feat-title">Symptom Analysis</div>
        <div class="feat-desc">Understand possible causes with clear, evidence-based explanations.</div>
    </div>
    <div class="feat-card">
        <div class="feat-card-top green-bar"></div>
        <span class="feat-icon">💊</span>
        <div class="feat-title">Self-Care Guidance</div>
        <div class="feat-desc">Safe, practical home-care tips to manage mild conditions.</div>
    </div>
    <div class="feat-card">
        <div class="feat-card-top orange-bar"></div>
        <span class="feat-icon">🚨</span>
        <div class="feat-title">Urgent Flag System</div>
        <div class="feat-desc">I clearly flag warning signs requiring immediate medical attention.</div>
    </div>
</div>
""", unsafe_allow_html=True)

# ==================================================
# CHAT DIVIDER
# ==================================================
st.markdown("""
<div class="chat-divider">
    <div class="div-line"></div>
    <div class="div-label">💬 Start Your Conversation</div>
    <div class="div-line"></div>
</div>
""", unsafe_allow_html=True)

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
            "You are MediAssist AI — a careful, empathetic, and knowledgeable healthcare assistant.\n\n"
            "Guidelines:\n"
            "- NEVER provide a definitive diagnosis.\n"
            "- Always mention 2-4 possible causes clearly.\n"
            "- Provide practical, safe self-care suggestions.\n"
            "- Clearly flag any red-flag or emergency warning signs.\n"
            "- Recommend seeing a doctor when appropriate.\n"
            "- Be warm, professional, and easy to understand.\n"
            "- Structure your response with clear sections using markdown.\n"
            "- Keep responses concise but thorough (max ~300 words).\n"
            "- End with a short disclaimer reminding users this is not medical advice."
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
prompt = st.chat_input("Describe your symptoms, age, and how long you've had them...")

if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.markdown(prompt)

    try:
        with st.chat_message("assistant"):
            with st.spinner("Analyzing your symptoms..."):
                reply = get_reply(st.session_state.messages)
                st.markdown(reply)

        st.session_state.messages.append({"role": "assistant", "content": reply})

    except Exception as e:
        st.error(f"Error: {e}")
