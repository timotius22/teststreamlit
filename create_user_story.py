import streamlit as st
import openai

def show_create_user_story():
    st.title("Create User Story")

    api_key = st.text_input("Enter your OpenAI API key")
    user_story_description = st.text_input("Write your user Story here")
    create_ticket_button = st.button("Create User Story")

    if create_ticket_button:
        openai.api_key = api_key
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=f"Create a user story for the following issue:\n{user_story_description}\n",
            temperature=0.5,
            max_tokens=100,
        )
        st.text("User Story:")
        st.text_area("", response.choices[0].text, disabled=True)
