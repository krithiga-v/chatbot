import sys
import base64
import io
from PIL import Image
import streamlit as st
import google.generativeai as genai

# ---------------------------#
# 1. SYSTEM SETUP
# ---------------------------#
sys.stdout.reconfigure(encoding='utf-8')

# ---------------------------#
# 2. GEMINI CONFIGURATION
# ---------------------------#
GENERATION_CONFIG = {
    "temperature": 0.9,
    "top_p": 1,
    "top_k": 1,
    "max_output_tokens": 2048,
}

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=GENERATION_CONFIG,
)

# Chatbot persona initialization
chat_session = model.start_chat(history=[
    {
        "role": "user",
        "parts": ["You are Medusa, a witty mythological assistant specializing in haircare and skincare advice. \
                   Start the first two lines using playful metaphors like magical potions and elixirs, \
                   then give practical, science-backed solutions."]
    },
    {"role": "model", "parts": ["Understood! I'll act as Medusa."]}
])

# ---------------------------#
# 3. HELPER FUNCTIONS
# ---------------------------#
def get_gemini_response(user_input: str) -> str:
    """Fetch response from Gemini API."""
    response = chat_session.send_message(user_input)
    return response.text


def load_image_as_base64(path: str) -> str:
    """Convert image to base64 string for Streamlit display."""
    with open(path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()


def set_app_theme():
    """Apply app-wide styling."""
    st.markdown(
        """
        <style>
        .stApp {
            background-color: #f8f0ff;
            font-family: 'Poppins', sans-serif;
        }
        .title {
            font-size: 28px;
            font-weight: bold;
            color: #6a0dad;
        }
        .chat-message {
            padding: 12px;
            border-radius: 10px;
            margin-bottom: 10px;
        }
        .user-msg {
            background-color: #e0d7ff;
            text-align: right;
        }
        .medusa-msg {
            background-color: #f3e8ff;
            text-align: left;
        }
        </style>
        """,
        unsafe_allow_html=True
    )


def clear_chat_history():
    """Reset the chat history."""
    st.session_state.chat_history = []


# ---------------------------#
# 4. STREAMLIT PAGE SETUP
# ---------------------------#
st.set_page_config(page_title="Medusa Chatbot", page_icon="🧞‍♀️", layout="centered")
set_app_theme()

if "page" not in st.session_state:
    st.session_state.page = "welcome"

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# ---------------------------#
# 5. WELCOME PAGE
# ---------------------------#
def welcome_page():
    st.title("🧞‍♀️ Welcome to Medusa")
    st.markdown("Your mystical assistant for **haircare** & **skincare** ✨")
    st.image("medusa.png", width=300)  # Replace with your Medusa image path
    if st.button("Enter Chatbot 🚀"):
        st.session_state.page = "chat"


# ---------------------------#
# 6. CHATBOT PAGE
# ---------------------------#
def chatbot_page():
    st.markdown("<h2 class='title'>Chat with Medusa 🧞‍♀️</h2>", unsafe_allow_html=True)

    # Chat display
    for msg in st.session_state.chat_history:
        role, text = msg
        css_class = "user-msg" if role == "user" else "medusa-msg"
        st.markdown(f"<div class='chat-message {css_class}'>{text}</div>", unsafe_allow_html=True)

    # User input
    user_input = st.text_input("Ask Medusa something...", key="user_input")
    if st.button("Send"):
        if user_input.strip():
            # Add user message
            st.session_state.chat_history.append(("user", user_input))
            # Get Medusa response
            medusa_reply = get_gemini_response(user_input)
            st.session_state.chat_history.append(("medusa", medusa_reply))
            st.experimental_rerun()

    # Sidebar options
    with st.sidebar:
        st.header("⚙️ Options")
        if st.button("Clear Chat History"):
            clear_chat_history()
            st.experimental_rerun()


# ---------------------------#
# 7. NAVIGATION HANDLER
# ---------------------------#
if st.session_state.page == "welcome":
    welcome_page()
else:
    chatbot_page()
