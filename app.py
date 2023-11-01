import streamlit as st
from home import show_home
from common_ticket import show_ticket

# Initialize session state for page navigation
if 'page' not in st.session_state:
    st.session_state.page = 'Home'

# Create a sidebar with buttons for each page
pages = ["Home", "Create Ticket"]
page_functions = [show_home, show_ticket]
for i, (p, f) in enumerate(zip(pages, page_functions)):
    if st.sidebar.button(p, key=f'sidebar_button_{i}'):
        st.session_state.page = p

# Show the selected page
if st.session_state.page == "Home":
    show_home()
elif 'api_key' in st.session_state and st.session_state.api_key:
    page_functions[pages.index(st.session_state.page)]()
else:
    st.warning("Please enter your OpenAI API key on the Home page to access this feature.")
