import streamlit as st
from home import show_home
from create_ticket import show_create_ticket

# Set the page configuration
st.set_page_config(page_title="Timo's Product Management Tool", page_icon=":bug:")

# Create a sidebar with a burger menu for page navigation
page = st.sidebar.selectbox("Menu", ["Home", "Create Bug Ticket", "Create User Story", "Create Task", "Create Spike"])

# Show the selected page
if page == "Home":
    show_home()
else:
    if page == "Create Bug Ticket":
        prompt = "Create a bug ticket for the following issue:\n"
        title = "Create Bug Ticket"
    elif page == "Create User Story":
        prompt = "Create a user story for the following feature:\n"
        title = "Create User Story"
    elif page == "Create Task":
        prompt = "Create a task for the following action:\n"
        title = "Create Task"
    elif page == "Create Spike":
        prompt = "Create a spike for the following investigation:\n"
        title = "Create Spike"

    show_create_ticket(title, prompt)
