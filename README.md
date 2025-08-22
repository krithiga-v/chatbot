# 🧞‍♀️ Medusa Chatbot

Medusa is an **AI-powered skincare and haircare assistant** built using **Streamlit** and **Google Gemini**.  
It provides **personalized advice** in a **playful mythological persona**, mixing magical metaphors with **science-backed solutions**.

---

## ✨ Features

- 🧴 **Haircare & Skincare Guidance** — Get tips on managing your skin and hair health.
- 🤖 **AI-Powered Conversations** — Uses **Google Gemini-1.5** for intelligent, contextual replies.
- 🎭 **Playful Medusa Persona** — Responds with mystical metaphors and witty remarks.
- 🌓 **Dark & Light Mode Themes** — Switch between two beautiful UI themes.
- 🗨️ **Persistent Chat History** — Remembers your conversation within the session.
- 🧹 **Clear Chat Option** — Start a fresh conversation anytime.

---

## 🛠️ Tech Stack

- **Frontend & UI** → [Streamlit](https://streamlit.io/)
- **AI Model** → [Google Gemini 1.5 Flash](https://ai.google.dev/)
- **Language** → Python 3.9+
- **Libraries**:
  - `streamlit`
  - `google-generativeai`
  - `Pillow`
  - `python-dotenv`

---

## 🚀 Getting Started

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/krithiga-v/chatbot.git
cd chatbot
2️⃣ Install Dependencies

Use the requirements.txt file:

pip install -r requirements.txt

3️⃣ Set Up Google Gemini API

Get your Google Generative AI API Key → Get Key

Create a .env file in the project root:

GOOGLE_API_KEY=your_api_key_here

4️⃣ Run the Chatbot
streamlit run Medusa.py
