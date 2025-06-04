# Gemini Chatbot

A simple chatbot using Google Gemini API and Streamlit, with memory support.

## Setup

1. Clone the repo.
2. Add your `.env` file with:
    ```plaintext
    GOOGLE_API_KEY=your_google_api_key
    ```
3. Run the app:
    ```bash
    streamlit run app.py
    ```
4. Open your browser and go to `http://localhost:8501`.
## Features
- Chat with Google Gemini.
- Memory support to remember past interactions.
- Streamlit interface for easy interaction.
## Requirements
- Python 3.8+
- Streamlit
- Google Gemini API client
- dotenv