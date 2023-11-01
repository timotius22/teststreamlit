import streamlit as st
from home import show_home
from create_bug_ticket import show_create_bug_ticket
from create_user_story import show_create_user_story

# Create a sidebar with a burger menu for page navigation
page = st.sidebar.selectbox("Menu", ["Home", "Create Bug Ticket", "Create User Story"])

# Show the selected page
if page == "Home":
    show_home()
elif page == "Create Bug Ticket":
    show_create_bug_ticket()
elif page == "Create User Story":
    show_create_user_story()
