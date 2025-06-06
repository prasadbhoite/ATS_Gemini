import streamlit as st
import os
import google.generativeai as genai
from dotenv import load_dotenv, find_dotenv

# Load environment variable
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# Configure Gemini
genai.configure(api_key=api_key)

####################

# Check if the API key is set
if not api_key:
    st.error("❌ Please set the GEMINI_API_KEY environment variable in your .env file.")
    st.stop()



# Initialize Gemini Pro model- Choose model (you can switch between "gemini-1.5-pro" and "gemini-1.5-flash")
model = genai.GenerativeModel(model_name="gemini-1.5-flash")

# Set page config / # Streamlit UI setup
st.set_page_config(page_title="Gemini Chatbot with Memory", page_icon="🧠")
st.title("💬 Gemini Chatbot with Memory")

# Initialize session state for chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Input box
user_input = st.chat_input("Type your message here...")

if user_input:
    # Save user message
    st.session_state.chat_history.append({"role": "user", "text": user_input})

    # Display chat messages so far
    for message in st.session_state.chat_history:
        with st.chat_message(message["role"]):
            st.markdown(message["text"])

    # Generate response (streamed)
    with st.chat_message("assistant"):
        response_area = st.empty()
        full_response = ""
        try:
            response = model.generate_content(user_input, stream=True)
            for chunk in response:
                if chunk.text:
                    full_response += chunk.text
                    response_area.markdown(full_response)
        except Exception as e:
            st.error(f"❌ Error: {e}")
            full_response = "⚠️ There was an error generating a response."

        # Save assistant response to history
        st.session_state.chat_history.append({"role": "assistant", "text": full_response})
else:
    # Show previous chat messages when no input yet
    for message in st.session_state.chat_history:
        with st.chat_message(message["role"]):
            st.markdown(message["text"])





