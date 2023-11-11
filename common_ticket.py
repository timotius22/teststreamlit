import streamlit as st
import openai


def show_ticket():
    st.title("Timo's Product Management Tool")

    if 'ticket_content' not in st.session_state:
        # Dropdown for ticket type selection
        ticket_type = st.selectbox("Select the ticket type:", ["Bug", "User Story", "Task", "Spike"])

        # Textbox for user input
        user_input = st.text_area("Write your ticket here:")

        # Dropdown for format selection
        format_selection = st.selectbox("Select the output format:", ["Normal", "HTML", "Jira Markup Language"])

        # Button to create ticket
        create_button = st.button("Create Ticket")

        # Display ticket
        if create_button:
            openai.api_key = st.session_state.api_key
            try:
                if ticket_type == "Bug":
                    prompt = "Write a bug ticket for the following issue:\n" \
                             "h1. Possible Explanations for the Bug:\n" \
                             "_Possible explanations that lead to the bug and ideas on how to solve the problem._\n" \
                             "h1. Description\n" \
                             "_A detailed description of the bug. It should give the reader a comprehensive understanding of what the bug is, where it occurs, and its impact._\n" \
                             "h1. Steps to Reproduce\n" \
                             "_Step-by-step instructions on how to reproduce the bug. These steps should be easy to understand and follow._\n" \
                             "h1. Current Result\n" \
                             "_Describe what actually happened, including the error message (if any)._\n" \
                             "_Screenshot(s)/Screen recording: If possible, attach a screenshot or screen recording showing the bug._\n" \
                             "h1. Expected Result\n" \
                             "_Explain what should have happened if the bug didn’t occur._\n" \
                             "h1. Date/Time of Occurrence\n" \
                             "_Date and time when the bug was encountered._\n" \
                             "h1. Additional Information\n" \
                             "_Any other information that can be helpful in understanding or fixing the bug._\n" \
                             "{user_input}"
                elif ticket_type == "User Story":
                    prompt = "Write a user story for the following requirement:\n" \
                             "As a [type of user], I want [an action] so that [benefit/value].\n" \
                             "{user_input}"
                elif ticket_type == "Task":
                    prompt = "Write a task for the following action:\n" \
                             "[Action description]\n" \
                             "{user_input}"
                elif ticket_type == "Spike":
                    prompt = "Write a spike for the following investigation:\n" \
                             "[Investigation description]\n" \
                             "{user_input}"

                with st.spinner("Creating your ticket... This may take up to two minutes."):
                    messages = [
                        {"role": "system", "content": "You are a helpful assistant."},
                        {"role": "user", "content": prompt.format(user_input=user_input)},
                    ]

                    completion = openai.ChatCompletion.create(
                        model="gpt-4",
                        messages=messages
                    )

                    ticket = completion.choices[0]["message"]
                    if ticket is None:
                        raise ValueError("No ticket generated.")

                st.session_state.ticket_content = ticket
            except Exception as e:
                st.error(f"Error creating ticket: {e}")
    else:
        st.text_area("Your ticket:", st.session_state.ticket_content, height=300)

        follow_up = st.text_input("Do you want to add anything else to the ticket?")
        if follow_up:
            openai.api_key = st.session_state.api_key
            try:
                with st.spinner("Updating your ticket... This may take up to two minutes."):
                    messages = [
                        {"role": "system", "content": "You are a helpful assistant."},
                        {"role": "user", "content": st.session_state.ticket_content},
                        {"role": "user", "content": follow_up},
                    ]

                    completion = openai.ChatCompletion.create(
                        model="gpt-4-turbo",
                        messages=messages
                    )

                    ticket = completion.choices[0]["message"]
                    if ticket is None:
                        raise ValueError("No ticket generated.")

                st.session_state.ticket_content = ticket
                st.text_area("Your updated ticket:", ticket, height=300)
            except Exception as e:
                st.error(f"Error updating ticket: {e}")
