import streamlit as st
from google import genai
from dotenv import load_dotenv
import os


# Load environment variables

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY not found in environment variables")


# Streamlit Page Config

st.set_page_config(
    page_title="M365 Whisperer",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 M365 Whisperer")
st.caption("Streamlit + Gemini (New SDK) + Conversation Memory")


# Initialize Conversation Memory (DATA ONLY)

PERSONA_PROMPT = """
You are an AI engineer working in an enterprise IT support role, handling Microsoft 365 administration, identity and access management, and device security. You regularly work with Microsoft 365, Exchange Online, Active Directory / Entra ID, HENNGE One device certification, MFA, FortiClient VPN, jump servers, and sync servers. Your core tasks include mailbox management, device certification registration and revocation, MFA management, email forwarding control, and user access administration. Respond with accurate, real-world, admin-level guidance.
"""

if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "user",
            "parts": [{"text": PERSONA_PROMPT}]
        }
    ]



v_msg = """
Hi, I’m Chetan — your friendly neighborhood Microsoft 365 wrangler 🙃
I reset mailboxes, wrestle MFA, approve devices, and say “no” to access issues all day so you can pretend nothing broke.
"""

# Display Chat History
for msg in st.session_state.messages:
    if msg["role"] in ["user", "assistant"]:
        with st.chat_message(msg["role"]):
            st.markdown(v_msg)

# --------------------------------
# User Input
# --------------------------------
user_input = st.chat_input("Ask something...")

if user_input:
    # Show user message
    with st.chat_message("user"):
        st.markdown(user_input)

    # Store user message
    st.session_state.messages.append(
        {
            "role": "user",
            "parts": [{"text": user_input}]
        }
    )

    # --------------------------------
    # Create client & chat (PER RUN)
    # --------------------------------
    client = genai.Client(api_key=api_key)

    chat = client.chats.create(
        model="gemini-3-flash-preview",
        history=st.session_state.messages[:-1]
    )

    # --------------------------------
    # Gemini Response with Loader
    # --------------------------------
    with st.chat_message("assistant"):
        with st.spinner("Gemini is thinking... 🤖"):
            response = chat.send_message(user_input)
            bot_reply = response.text

        st.markdown(bot_reply)

    # Store assistant message
    st.session_state.messages.append(
        {
            "role": "assistant",
            "parts": [{"text": bot_reply}]
        }
    )
