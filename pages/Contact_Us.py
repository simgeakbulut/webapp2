import streamlit as st

st.header('Contact Me')

with set.form(key='email_forms'):
    user_email = st.text_input('your e-mail address:')
    message = st.text_area('Your message')
    button = st.form_submit_button("Submit")
    if button:
        print ('yooooo')
        message = message + user_email

