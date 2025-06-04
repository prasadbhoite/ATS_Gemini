import streamlit as st
import os
import google.generativeai as genai
from dotenv import load_dotenv, find_dotenv


# Load the environment variables
load_dotenv(find_dotenv()) # read local .env file
api_key = os.getenv("GEMINI_API_KEY")



# Configure Gemini
genai.configure(api_key=api_key)

# Check if the API key is set
if not api_key:
    st.error("❌ Please set the GEMINI_API_KEY environment variable in your .env file.")
    st.stop()


# Initialize Gemini Pro model
model = genai.GenerativeModel(model_name="gemini-1.5-flash")

# Streamlit UI setup
st.set_page_config(page_title="Gemini 1.5 Flash Chat", page_icon="🤖")
st.title("💬 Gemini Chatbot (Without Memory)")

# Input
user_input = st.text_input("Ask something:", key="input")

# Output
if user_input:
    st.markdown("### Response:")
    placeholder = st.empty()

    try:
        response = model.generate_content(user_input, stream=True)

        full_response = ""
        for chunk in response:
            if chunk.text:
                full_response += chunk.text
                placeholder.markdown(full_response)
    except Exception as e:
        st.error(f"❌ Error: {e}")
