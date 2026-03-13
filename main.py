import os

import streamlit as st
from dotenv import load_dotenv
from groq import Groq


load_dotenv()

MODEL_NAME = "llama-3.3-70b-versatile"

st.set_page_config(page_title="SnehaCare (Groq)", page_icon="🩺", layout="centered")

st.markdown(
	"""
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
			background: #ffffff;
		}

		.block-container {
			max-width: 1000px;
			padding-top: 3rem;
			padding-bottom: 8rem;
		}

		h1, h2, h3 {
			font-family: 'Fraunces', serif;
			letter-spacing: -0.03em;
		}

		.hero {
			display: grid;
			grid-template-columns: minmax(0, 1.3fr) minmax(0, 0.7fr);
			gap: 2.5rem;
			background: rgba(255, 255, 255, 0.85);
			border: 1px solid var(--teal-100);
			border-radius: 24px;
			padding: 2.5rem;
			box-shadow: 0 30px 60px rgba(13, 148, 136, 0.05);
			backdrop-filter: blur(12px);
			margin-bottom: 2rem;
		}

		.hero h1 {
			margin: 0.5rem 0 1rem;
			font-size: 2.75rem;
			line-height: 1.1;
		}

		.hero p {
			color: var(--ink-700);
			font-size: 1.1rem;
			line-height: 1.7;
		}

		.eyebrow {
			text-transform: uppercase;
			font-size: 0.75rem;
			letter-spacing: 0.2em;
			color: var(--teal-600);
			font-weight: 700;
		}

		.hero-card {
			background: #ffffff;
			border: 1px solid var(--teal-100);
			border-radius: 20px;
			padding: 1.75rem;
			box-shadow: 0 10px 30px rgba(13, 148, 136, 0.03);
		}

		.hero-card h3 {
			margin: 0 0 1rem;
			font-size: 1.25rem;
		}

		.hero-card ul {
			padding-left: 1.25rem;
			margin: 0;
			color: var(--ink-700);
			line-height: 1.6;
		}

		.chips {
			display: flex;
			gap: 0.75rem;
			flex-wrap: wrap;
			margin-top: 1.5rem;
		}

		.chip {
			border: 1px solid var(--teal-100);
			border-radius: 999px;
			padding: 0.4rem 1rem;
			font-size: 0.85rem;
			color: var(--teal-600);
			background: var(--teal-50);
			font-weight: 500;
		}

		.section {
			margin-top: 2rem;
			padding: 2rem;
			background: #ffffff;
			border: 1px solid var(--teal-100);
			border-radius: 20px;
			box-shadow: 0 10px 30px rgba(13, 148, 136, 0.03);
		}

		.section-title {
			font-weight: 600;
			font-family: 'Fraunces', serif;
			font-size: 1.5rem;
			color: var(--ink-900);
			margin-bottom: 1.25rem;
		}

		.card-grid {
			display: grid;
			grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
			gap: 1.25rem;
		}

		.mini-card {
			border: 1px solid var(--teal-50);
			border-radius: 16px;
			padding: 1.25rem;
			background: #fcfdfd;
			color: var(--ink-700);
			font-size: 1rem;
			line-height: 1.5;
			transition: all 0.2s ease;
		}

		.mini-card:hover {
			border-color: var(--teal-200);
			background: #ffffff;
			transform: translateY(-2px);
		}

		.alert {
			border-radius: 16px;
			border: 1px solid var(--teal-100);
			background: #f0fdfa;
			padding: 1.25rem 1.5rem;
			color: var(--ink-900);
			font-size: 1rem;
			line-height: 1.6;
			margin: 1.5rem 0;
		}

		[data-testid="stChatMessage"] {
			border: 1px solid var(--teal-100);
			background: #ffffff;
			border-radius: 18px;
			box-shadow: 0 15px 35px rgba(13, 148, 136, 0.04);
			padding: 1.25rem;
			margin-bottom: 1.25rem;
		}

		[data-testid="stChatInput"] {
			background: #ffffff;
			border: 1px solid var(--teal-100);
			border-radius: 16px;
			box-shadow: 0 -10px 40px rgba(0,0,0,0.02);
		}

		[data-testid="stChatInput"] textarea {
			font-family: 'Plus Jakarta Sans', sans-serif;
		}

		.stButton button,
		.stDownloadButton button,
		.stFormSubmitButton button {
			background: linear-gradient(135deg, var(--teal-500), var(--teal-600));
			color: white;
			border: none;
		}

		.stAlert {
			border-radius: 12px;
			border: 1px solid #99f6e4;
		}

		@media (max-width: 900px) {
			.hero {
				grid-template-columns: 1fr;
			}
		}
	</style>
	""",
	unsafe_allow_html=True,
)

st.markdown(
	"""
	<div class="hero">
		<div>
			<div class="eyebrow">SnehaCare Assistant</div>
			<h1>SnehaCare Bot</h1>
			<p>
				Share your symptoms, age, and how long you have felt them. I will offer possible next steps,
				self-care tips, and when to seek urgent help.
			</p>
			<div class="chips">
				<span class="chip">Model: """
	+ MODEL_NAME
	+ """</span>
				<span class="chip">Secure key from .env</span>
				<span class="chip">Clear, concise guidance</span>
			</div>
		</div>
		<div class="hero-card">
			<h3>Before we start</h3>
			<ul>
				<li>Include your age and location (country is enough).</li>
				<li>Mention chronic conditions or medications.</li>
				<li>Describe timing: sudden vs. gradual.</li>
			</ul>
		</div>
	</div>
	""",
	unsafe_allow_html=True,
)

st.markdown(
	"""
	<div class="alert">
		<strong>Safety note:</strong> This chatbot is informational only. If you have chest pain, breathing trouble,
		stroke signs, or heavy bleeding, seek emergency care immediately.
	</div>
	""",
	unsafe_allow_html=True,
)


def get_client(api_key: str) -> Groq:
	return Groq(api_key=api_key)


def get_assistant_reply(client: Groq, model: str, messages: list[dict[str, str]]) -> str:
	system_message = {
		"role": "system",
		"content": (
			"You are SnehaCare, a careful medical information assistant. Provide clear, practical guidance, ask follow-up questions "
			"when needed, and include warning signs that require urgent care. Do not claim to diagnose with certainty. "
			"Keep responses concise and structured."
		),
	}

	response = client.chat.completions.create(
		model=model,
		messages=[system_message, *messages],
		temperature=0.4,
		max_completion_tokens=900,
	)
	return response.choices[0].message.content or "I could not generate a response right now."


api_key = os.getenv("GROQ_API_KEY", "")

if not api_key:
	st.error("Missing GROQ_API_KEY in .env file. Add it and restart the app.")
	st.stop()

st.markdown(
	"""
	<div class="section">
		<div class="section-title">How I can help</div>
		<div class="card-grid">
			<div class="mini-card">Explain likely causes and what to watch for.</div>
			<div class="mini-card">Suggest safe self-care steps for the next 24–48 hours.</div>
			<div class="mini-card">Flag red-flag symptoms that need urgent care.</div>
		</div>
	</div>
	""",
	unsafe_allow_html=True,
)


if "messages" not in st.session_state:
	st.session_state.messages = []


for msg in st.session_state.messages:
	with st.chat_message(msg["role"]):
		st.markdown(msg["content"])


user_prompt = st.chat_input("Describe your symptoms, age, and duration...")

if user_prompt:
	st.session_state.messages.append({"role": "user", "content": user_prompt})
	with st.chat_message("user"):
		st.markdown(user_prompt)

	try:
		client = get_client(api_key)
		reply = get_assistant_reply(client, MODEL_NAME, st.session_state.messages)
		st.session_state.messages.append({"role": "assistant", "content": reply})
		with st.chat_message("assistant"):
			st.markdown(reply)
	except Exception as exc:
		with st.chat_message("assistant"):
			st.error(f"Error while calling Groq API: {exc}")
