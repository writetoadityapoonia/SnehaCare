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
css = """
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

* { box-sizing: border-box; margin: 0; padding: 0; }

html, body, .stApp {
    background: linear-gradient(135deg, #f0f9ff 0%, #f8fafc 40%, #f0fdf4 100%) !important;
    font-family: 'Outfit', sans-serif;
    color: var(--text);
}

[data-testid="stHeader"],
[data-testid="stToolbar"],
footer, header {
    background: transparent !important;
    display: none !important;
}

[data-testid="stBottom"] {
    background: rgba(255,255,255,0.9) !important;
    backdrop-filter: blur(20px) !important;
    border-top: 1px solid var(--border) !important;
    padding: 12px 20px !important;
}

[data-testid="stChatInput"] {
    background: white !important;
    border: 2px solid var(--border) !important;
    border-radius: 20px !important;
    box-shadow: 0 4px 24px rgba(14,165,233,0.08) !important;
    transition: all 0.3s ease !important;
}

[data-testid="stChatInput"]:focus-within {
    border-color: var(--primary) !important;
    box-shadow: 0 4px 32px rgba(14,165,233,0.18) !important;
}

[data-testid="stChatInput"] textarea {
    font-family: 'Outfit', sans-serif !important;
    font-size: 15px !important;
    color: var(--text) !important;
}

/* ── NAV BAR ── */
.navbar {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 18px 28px;
    background: rgba(255,255,255,0.85);
    backdrop-filter: blur(20px);
    border-radius: 24px;
    border: 1px solid var(--border);
    margin-bottom: 28px;
    box-shadow: 0 2px 20px rgba(0,0,0,0.04);
}

.nav-logo {
    display: flex;
    align-items: center;
    gap: 12px;
}

.nav-logo-icon {
    width: 42px;
    height: 42px;
    background: linear-gradient(135deg, var(--primary), var(--accent));
    border-radius: 14px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 20px;
    box-shadow: 0 4px 16px rgba(14,165,233,0.35);
}

.nav-logo-text {
    font-size: 20px;
    font-weight: 800;
    background: linear-gradient(135deg, var(--primary-dark), var(--accent));
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}

.nav-badge {
    background: linear-gradient(135deg, var(--primary-light), #cffafe);
    color: var(--primary-dark);
    padding: 6px 16px;
    border-radius: 999px;
    font-size: 12px;
    font-weight: 700;
    letter-spacing: 0.5px;
    border: 1px solid rgba(14,165,233,0.2);
}

/* ── HERO ── */
.hero-wrapper {
    background: linear-gradient(135deg, #0ea5e9 0%, #0284c7 50%, #06b6d4 100%);
    border-radius: 28px;
    padding: 44px 44px 48px;
    margin-bottom: 24px;
    position: relative;
    overflow: hidden;
    box-shadow: 0 20px 60px rgba(14,165,233,0.3);
}

.hero-wrapper::before {
    content: '';
    position: absolute;
    top: -80px; right: -80px;
    width: 300px; height: 300px;
    background: rgba(255,255,255,0.07);
    border-radius: 50%;
}

.hero-wrapper::after {
    content: '';
    position: absolute;
    bottom: -60px; left: -40px;
    width: 220px; height: 220px;
    background: rgba(255,255,255,0.05);
    border-radius: 50%;
}

.hero-tag {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    background: rgba(255,255,255,0.18);
    border: 1px solid rgba(255,255,255,0.3);
    color: white;
    padding: 6px 16px;
    border-radius: 999px;
    font-size: 12px;
    font-weight: 700;
    letter-spacing: 1px;
    text-transform: uppercase;
    margin-bottom: 18px;
    backdrop-filter: blur(10px);
}

.hero-title {
    font-family: 'Playfair Display', serif;
    font-size: 52px;
    font-weight: 800;
    color: white;
    line-height: 1.08;
    margin-bottom: 16px;
}

.hero-title span {
    color: #bae6fd;
}

.hero-sub {
    font-size: 16px;
    color: rgba(255,255,255,0.85);
    line-height: 1.75;
    max-width: 520px;
    margin-bottom: 30px;
    font-weight: 400;
}

.hero-chips {
    display: flex;
    gap: 10px;
    flex-wrap: wrap;
}

.hero-chip {
    background: rgba(255,255,255,0.18);
    border: 1px solid rgba(255,255,255,0.3);
    color: white;
    padding: 8px 18px;
    border-radius: 999px;
    font-size: 13px;
    font-weight: 600;
    backdrop-filter: blur(10px);
}

.hero-float {
    position: absolute;
    right: 40px;
    top: 50%;
    transform: translateY(-50%);
    background: rgba(255,255,255,0.12);
    border: 1px solid rgba(255,255,255,0.25);
    backdrop-filter: blur(20px);
    border-radius: 24px;
    padding: 24px 28px;
    min-width: 200px;
    z-index: 2;
}

.hero-float h4 {
    color: white;
    font-size: 14px;
    font-weight: 700;
    margin-bottom: 14px;
    letter-spacing: 0.3px;
}

.hero-float li {
    color: rgba(255,255,255,0.85);
    font-size: 13px;
    margin-bottom: 8px;
    padding-left: 4px;
    list-style: none;
    display: flex;
    align-items: center;
    gap: 8px;
}

.dot {
    width: 6px; height: 6px;
    background: #7dd3fc;
    border-radius: 50%;
    flex-shrink: 0;
}

/* ── ALERT ── */
.alert-box {
    display: flex;
    align-items: flex-start;
    gap: 14px;
    background: linear-gradient(135deg, #fff7ed, #fff);
    border: 1.5px solid #fed7aa;
    border-left: 4px solid var(--warning);
    border-radius: 20px;
    padding: 18px 22px;
    margin-bottom: 24px;
    box-shadow: 0 4px 16px rgba(245,158,11,0.08);
}

.alert-icon {
    font-size: 22px;
    flex-shrink: 0;
    margin-top: 2px;
}

.alert-text {
    font-size: 14px;
    color: #92400e;
    line-height: 1.65;
    font-weight: 500;
}

.alert-text strong {
    color: #78350f;
    font-weight: 700;
    font-size: 15px;
}

/* ── FEATURE CARDS ── */
.section-label {
    font-size: 13px;
    font-weight: 700;
    letter-spacing: 1.2px;
    text-transform: uppercase;
    color: var(--primary);
    margin-bottom: 8px;
}

.section-title {
    font-family: 'Playfair Display', serif;
    font-size: 28px;
    font-weight: 700;
    color: var(--text);
    margin-bottom: 20px;
}

.feat-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 16px;
    margin-bottom: 30px;
}

.feat-card {
    background: white;
    border-radius: 22px;
    padding: 24px 22px;
    border: 1.5px solid var(--border);
    box-shadow: 0 4px 20px rgba(0,0,0,0.03);
    transition: all 0.3s ease;
    position: relative;
    overflow: hidden;
}

.feat-card::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 3px;
    border-radius: 22px 22px 0 0;
}

.feat-card.blue::before { background: linear-gradient(90deg, var(--primary), var(--accent)); }
.feat-card.green::before { background: linear-gradient(90deg, var(--success), #34d399); }
.feat-card.orange::before { background: linear-gradient(90deg, var(--warning), #fbbf24); }

.feat-icon {
    font-size: 30px;
    margin-bottom: 12px;
    display: block;
}

.feat-title {
    font-size: 15px;
    font-weight: 700;
    color: var(--text);
    margin-bottom: 6px;
}

.feat-desc {
    font-size: 13px;
    color: var(--muted);
    line-height: 1.6;
    font-weight: 400;
}

/* ── STATS BAR ── */
.stats-bar {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 14px;
    margin-bottom: 28px;
}

.stat-item {
    background: white;
    border-radius: 18px;
    padding: 20px;
    text-align: center;
    border: 1.5px solid var(--border);
    box-shadow: 0 2px 12px rgba(0,0,0,0.02);
}

.stat-num {
    font-size: 28px;
    font-weight: 800;
    background: linear-gradient(135deg, var(--primary), var(--accent));
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    line-height: 1.1;
}

.stat-label {
    font-size: 12px;
    color: var(--muted);
    font-weight: 600;
    margin-top: 4px;
    text-transform: uppercase;
    letter-spacing: 0.5px;
}

/* ── DIVIDER ── */
.divider {
    display: flex;
    align-items: center;
    gap: 14px;
    margin: 28px 0 24px;
}

.divider-line {
    flex: 1;
    height: 1px;
    background: var(--border);
}

.divider-text {
    font-size: 12px;
    font-weight: 700;
    color: var(--muted);
    letter-spacing: 1px;
    text-transform: uppercase;
}

/* ── CHAT MESSAGES ── */
[data-testid="stChatMessage"] {
    background: white !important;
    border-radius: 20px !important;
    border: 1.5px solid var(--border) !important;
    padding: 18px !important;
    margin-bottom: 14px !important;
    box-shadow: 0 2px 12px rgba(0,0,0,0.03) !important;
}

[data-testid="stChatMessage"][data-testid*="user"] {
    background: linear-gradient(135deg, var(--primary-light), #e0f2fe) !important;
    border-color: rgba(14,165,233,0.2) !important;
}

/* ── RESPONSIVE ── */
@media (max-width: 900px) {
    .hero-title { font-size: 38px; }
    .hero-wrapper { padding: 32px 24px; }
    .hero-float { display: none; }
    .feat-grid { grid-template-columns: 1fr; }
    .stats-bar { grid-template-columns: 1fr; }
    .navbar { padding: 14px 18px; }
}
</style>
"""

st.markdown(css, unsafe_allow_html=True)

# ==================================================
# NAVBAR
# ==================================================
st.markdown(f"""
<div class="navbar">
    <div class="nav-logo">
        <div class="nav-logo-icon">🩺</div>
        <span class="nav-logo-text">MediAssist AI</span>
    </div>
    <div class="nav-badge">⚡ {MODEL_NAME}</div>
</div>
""", unsafe_allow_html=True)

# ==================================================
# HERO SECTION
# ==================================================
st.markdown("""
<div class="hero-wrapper">
    <div class="hero-tag">✦ AI-Powered Health Guidance</div>
    <div class="hero-title">Your Personal<br><span>Health Assistant</span></div>
    <div class="hero-sub">
        Share your symptoms and get smart, thoughtful guidance on possible causes,
        self-care steps, and when to seek professional medical help.
    </div>
    <div class="hero-chips">
        <span class="hero-chip">🔒 Private & Secure</span>
        <span class="hero-chip">⚡ Instant Responses</span>
        <span class="hero-chip">🌍 Global Coverage</span>
    </div>

    <div class="hero-float">
        <h4>📋 Include these details</h4>
        <ul>
            <li><span class="dot"></span> Your age & gender</li>
            <li><span class="dot"></span> Country / region</li>
            <li><span class="dot"></span> Clear symptoms</li>
            <li><span class="dot"></span> Sudden or gradual?</li>
            <li><span class="dot"></span> Current medicines</li>
            <li><span class="dot"></span> Duration of symptoms</li>
        </ul>
    </div>
</div>
""", unsafe_allow_html=True)

# ==================================================
# STATS BAR
# ==================================================
st.markdown("""
<div class="stats-bar">
    <div class="stat-item">
        <div class="stat-num">70B</div>
        <div class="stat-label">Parameter Model</div>
    </div>
    <div class="stat-item">
        <div class="stat-num">&lt;2s</div>
        <div class="stat-label">Avg Response Time</div>
    </div>
    <div class="stat-item">
        <div class="stat-num">24/7</div>
        <div class="stat-label">Always Available</div>
    </div>
</div>
""", unsafe_allow_html=True)

# ==================================================
# ALERT
# ==================================================
st.markdown("""
<div class="alert-box">
    <div class="alert-icon">⚠️</div>
    <div class="alert-text">
        <strong>Emergency Warning</strong><br>
        For chest pain, difficulty breathing, stroke symptoms, severe bleeding,
        or any life-threatening emergency — call emergency services or go to the
        nearest ER immediately. This AI does not replace professional medical advice.
    </div>
</div>
""", unsafe_allow_html=True)

# ==================================================
# FEATURE CARDS
# ==================================================
st.markdown("""
<div class="section-label">What I offer</div>
<div class="section-title">How I can help you today</div>

<div class="feat-grid">
    <div class="feat-card blue">
        <span class="feat-icon">🔍</span>
        <div class="feat-title">Symptom Analysis</div>
        <div class="feat-desc">Understand possible causes behind your symptoms with clear, evidence-based explanations.</div>
    </div>
    <div class="feat-card green">
        <span class="feat-icon">💊</span>
        <div class="feat-title">Self-Care Guidance</div>
        <div class="feat-desc">Get safe, practical home-care tips to manage mild conditions while monitoring progress.</div>
    </div>
    <div class="feat-card orange">
        <span class="feat-icon">🚨</span>
        <div class="feat-title">Urgent Flag System</div>
        <div class="feat-desc">I'll clearly flag warning signs that require immediate or professional medical attention.</div>
    </div>
</div>
""", unsafe_allow_html=True)

# ==================================================
# CHAT DIVIDER
# ==================================================
st.markdown("""
<div class="divider">
    <div class="divider-line"></div>
    <div class="divider-text">💬 Start Your Conversation</div>
    <div class="divider-line"></div>
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
        "content": """
You are MediAssist AI — a careful, empathetic, and knowledgeable healthcare assistant.

Guidelines:
- NEVER provide a definitive diagnosis.
- Always mention 2-4 possible causes clearly.
- Provide practical, safe self-care suggestions.
- Clearly flag any red-flag / emergency warning signs.
- Recommend seeing a doctor when appropriate.
- Be warm, professional, and easy to understand.
- Structure your response with clear sections using markdown.
- Keep responses concise but thorough (max ~300 words).
- End with a short disclaimer reminding users this is not medical advice.
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
        st.error(f"⚠️ Error: {e}")}

[data-testid="stChatInput"] textarea{
font-family:'Plus Jakarta Sans', sans-serif !important;
color:var(--ink-900) !important;
}

.hero{
display:grid;
grid-template-columns:1.6fr 1fr;
gap:24px;
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
margin:10px 0;
line-height:1.05;
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
padding:16px;
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
"""

st.markdown(css, unsafe_allow_html=True)

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
I’ll offer possible next steps, self-care tips, and when to seek urgent help.
</p>

<div class="chips">
<span class="chip">Model: {MODEL_NAME}</span>
<span class="chip">Fast Responses</span>
<span class="chip">Smart Guidance</span>
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
For chest pain, breathing trouble, stroke signs,
or heavy bleeding seek emergency care immediately.
</div>
""", unsafe_allow_html=True)

# ==================================================
# FEATURE SECTION
# ==================================================
st.markdown("""
<div class="section-title">How I can help</div>

<div class="card-grid">
<div class="mini-card">Explain likely causes.</div>
<div class="mini-card">Suggest self-care tips.</div>
<div class="mini-card">Flag urgent symptoms.</div>
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
        "content": """
You are a careful healthcare assistant.

Rules:
- No final diagnosis.
- Mention possible causes.
- Suggest safe care.
- Mention warning signs.
- Keep concise.
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
        st.error(f"Error: {e}")--teal-500:#0d9488;
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
