import streamlit as st
import openai

def show_create_bug_ticket():
    st.title("Create Bug Ticket")

    api_key = st.text_input("Enter your OpenAI API key")
    bug_description = st.text_input("Write your bug here")
    create_ticket_button = st.button("Create bug ticket")

    if create_ticket_button:
        openai.api_key = api_key
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=f"Create a bug ticket for the following issue:\n{bug_description}\n",
            temperature=0.5,
            max_tokens=100,
        )
        st.text("Bug ticket:")
        st.text_area("", response.choices[0].text, disabled=True)
