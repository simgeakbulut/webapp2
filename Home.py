import streamlit as st

col1,empty_col,col2 = st.columns(3)

with col1:
    st.image("images/simge.jpeg")

with col2:
    st.title('Simge Akbulut')
    content = """Hi! I am Simge. I am a computer engineering student and i'm doing internship in Comodo Cyber Security.
    I made this website to show you the python projects that I've made."""
    st.write(content)

