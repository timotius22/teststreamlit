import streamlit as st
import openai
import json

# Function to load prompts from the JSON file
def load_prompts():
    with open('prompts.json', 'r') as file:
        return json.load(file)

# Functions to format the output
def format_normal(ticket):
    # Convert HTML-like tags to readable text
    ticket = ticket.replace("<h1>", "").replace("</h1>", "\n")
    ticket = ticket.replace("<p>", "").replace("</p>", "\n\n")
    # Add more replacements as needed for other tags
    return ticket.strip()

def format_html(ticket):
    # Wrap the ticket in HTML body tags
    return f"<html><body>\n{ticket}\n</body></html>"

def format_jira(ticket):
    # Replace HTML tags with Jira Markup equivalents
    ticket = ticket.replace("<h1>", "h1. ").replace("</h1>", "\n")
    ticket = ticket.replace("<p>", "").replace("</p>", "\n\n")
    # Add more replacements as needed for other tags
    return ticket.strip()

# Main function to show ticket
def show_ticket():
    st.title("Product GPT")

    # Use the user's API key if it exists, otherwise use the default
    openai.api_key = st.session_state.get('api_key', st.secrets["openai"]["api_key"])

    # Dropdown for ticket type selection
    ticket_type = st.selectbox("Select the ticket type:", ["Bug", "User Story", "Task", "Spike"])

    # Textbox for user input
    user_input = st.text_area("Write your ticket here:")

    # Dropdown for format selection
    format_selection = st.selectbox("Select the output format:", ["Normal", "HTML", "Jira Markup Language"])

    # Button to create ticket
    if st.button("Create Ticket"):
        prompts = load_prompts()
        prompt_text = prompts.get(ticket_type, "")
        if not prompt_text:
            st.error(f"Could not find a prompt for ticket type: {ticket_type}")
            return

        prompt = {
            "role": "user",
            "content": prompt_text + user_input  # Combining prompt text with user input
        }

        system_prompt = {
            "role": "system",
            "content": "You are an experienced product manager and an expert in writing tickets."
        }

        try:
            with st.spinner("Creating your ticket... This may take up to two minutes."):
                response = openai.ChatCompletion.create(
                    model="gpt-4-1106-preview",
                    messages=[system_prompt, prompt]
                )

                ticket = response.choices[0].get("message")

                # Check if ticket is None or not a string
                if ticket is None:
                    raise ValueError("No ticket generated. The completion result was empty.")
                if not isinstance(ticket, str):
                    ticket = str(ticket)  # Convert to string if not already

                st.session_state['ticket_content'] = ticket

                # Format the ticket based on the selected format and display
                if format_selection == "Normal":
                    formatted_ticket = format_normal(ticket)
                    st.text(formatted_ticket)  # Display as plain text
                elif format_selection == "HTML":
                    formatted_ticket = format_html(ticket)
                    st.code(formatted_ticket, language="html")  # Display as HTML code
                elif format_selection == "Jira Markup Language":
                    formatted_ticket = format_jira(ticket)
                    st.code(formatted_ticket, language="markup")  # Display as Jira Markup

                st.success("Ticket created successfully:")

        except openai.error.OpenAIError as openai_error:
            st.error(f"An error occurred with OpenAI: {openai_error}")
        except Exception as e:
            st.error(f"An unexpected error occurred: {e}")

