import streamlit as st
import google.generativeai as genai
import os

# Configure Google Generative AI
api_key = 'AIzaSyASIaMhK0LEO0CH9RGot9Ko_E5oX0kPBEU'  # Replace with your actual API key
genai.configure(api_key=api_key)

# Streamlit App
st.title("Code Generator")

# Dropdown for selecting the programming language
language = st.selectbox("Select Language:", ["Python", "C", "Java", "C++"])

# Text area for user to input code
code_input = st.text_area("Enter your code:")

# Button to trigger code generation
if st.button("Generate Code"):
    try:
        # Define the history and message for the chat
        history = [
            {
                "role": "user",
                "parts": [
                    f"Code Generation. User selected {language}. Generate the code: {code_input}",
                ],
            }
        ]
        
        # Initialize the generative model
        model = genai.GenerativeModel(model_name="gemini-1.5-flash")
        
        # Start a new chat session with the provided history
        chat_session = model.start_chat(history=history)
        
        # Send the user's input as a message
        response = chat_session.send_message("Generate code")

        # Display the generated code
        if hasattr(response, 'text'):
            st.code(response.text, language.lower())
        else:
            st.error("Unexpected response format.")
    
    except genai.exceptions.StopCandidateException as e:
        st.error(f"Generation failed due to StopCandidateException: {e}")
    except Exception as e:
        st.error(f"An unexpected error occurred: {e}")
