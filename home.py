import streamlit as st


def show_home():
    st.title("Welcome to Timo's Product Management Tool!")
    st.write("This tool allows you to create bug tickets, user stories, tasks, and spikes.")

    # Check if API key is already saved in session state
    if 'api_key' in st.session_state and st.session_state.api_key:
        st.success("API key is saved!")

        # Allow user to change API key
        change_key = st.button("Change API key")
        if change_key:
            del st.session_state.api_key
    else:
        # Textbox for API key
        api_key = st.text_input("Enter your OpenAI API key:")

        if api_key:
            st.session_state.api_key = api_key
            st.success("API key saved!")
