import streamlit as st
from common_ticket4 import apply_format

def create_ticket_ui():
    ticket_type = st.selectbox("Select the ticket type:", ["Bug", "User Story", "Task", "Spike"], key='ticket_type')
    user_input = st.text_area("Write your ticket here:", key='user_input')
    format_selection = st.selectbox("Select the output format:", ["Normal", "HTML", "Jira Markup Language"], key='format_selection')

    create_ticket = st.button("Create Ticket")
    return ticket_type, user_input, format_selection, create_ticket

def display_formatted_ticket(ticket, format_selection):
    if ticket:
        formatted_ticket = apply_format(ticket, format_selection)
        st.text_area("Formatted Ticket", formatted_ticket, height=300, key='formatted_ticket')

def refine_ticket_ui():
    refine_input = st.text_area("How would you like to refine the ticket?", key='refine_input')
    refine_ticket = st.button("Refine Ticket")
    return refine_input, refine_ticket
