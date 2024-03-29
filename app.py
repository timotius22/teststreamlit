import streamlit as st
import openai
from common_ticket3_norefinement import show_ticket

# Function to validate API key against OpenAI
def validate_api_key(api_key):
    try:
        openai.api_key = api_key
        # Simple, low-cost request to validate key
        openai.Completion.create(engine="text-davinci-003", prompt="Hello world", max_tokens=5)
        return True
    except Exception as e:
        return False

# Function to show the login page
def show_login_page():
    st.title("Welcome to Product GPT")
    st.title("Login")

    # Radio button for login method selection
    login_method = st.radio("Login Method:", ["Username & Password", "API Key"])

    if login_method == "Username & Password":
        username_input = st.text_input("Username")
        password_input = st.text_input("Password", type="password")

        if st.button("Login"):
            if username_input == st.secrets["login_credentials"]["username"] and \
                    password_input == st.secrets["login_credentials"]["password"]:
                st.session_state['authenticated'] = True
                st.session_state['action'] = 'create_ticket'
                st.experimental_rerun()

    else:
        api_key_input = st.text_input("API Key", type="password")

        if st.button("Login with API Key"):
            if validate_api_key(api_key_input):
                st.session_state['authenticated'] = True
                st.session_state['action'] = 'create_ticket'
                st.experimental_rerun()

# Main function
def main():
    # If the user is not authenticated, show the login page
    if not st.session_state.get('authenticated', False):
        show_login_page()
    else:
        # Define actions for sidebar after login
        if 'action' not in st.session_state:
            st.session_state['action'] = 'create_ticket'

        if st.session_state['action'] == 'create_ticket':
            show_ticket()

        # Sidebar only appears after successful login
        with st.sidebar:
            if st.button("Create New Ticket"):
                st.session_state['action'] = 'create_ticket'
            if st.button("Log Out"):
                # Clear the session and show the login page
                st.session_state.clear()
                st.experimental_rerun()

        # Execute actions as per the session state
        if st.session_state.get('action') == 'logout':
            st.session_state.clear()
            st.experimental_rerun()

if __name__ == "__main__":
    main()
