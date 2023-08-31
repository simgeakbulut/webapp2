import streamlit as st
import pandas

st.set_page_config(layout='wide')
col1,col2 = st.columns([3,4])

with col1:
    st.image("images/simge.jpeg", width=350)

with col2:
    st.title('Simge Akbulut')
    content = """Hey there, wonderful souls! I'm Simge, and if you're in the realm of all things tech, we're about to embark on an exciting journey together.
    Picture this: a passionate computer engineering student who's not just diving into the sea of codes and circuits,
but is also flexing her cybersecurity muscles as an intern at Comodo Cyber Security – yep, that's me!
Originally a proud Istanbulite from the beautiful lands of Turkey, I've got a story that's taken me places.
 For the past year, the USA has been my home, infusing my life with new perspectives, different flavors, and a dash of adventure.
Tech runs through my veins, and as I walk the halls of computer engineering, I'm living my dream of turning complex problems into elegant solutions. 
And guess what? While I'm busy soaking up knowledge, I'm also part of the kick-butt team at Comodo Cyber Security, where I'm on the front lines against digital threats. 
Cybersecurity superhero? Well, you could say that.
So, whether it's debugging lines of code or defending the digital universe, I'm your go-to gal. 
Stay tuned as I juggle bits and bytes, and let's unravel the marvels of technology together!"""
    st.info(content)

col3,empty_col,col4= st.columns([1.5,0.5,1.5])

df= pandas.read_csv('data.csv', sep=';')

with col3:
    for index,row in df[:10].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})+ \n\n")

with col4:
    for index,row in df[10:].iterrows():
        st.header(row['title'])
        st.image("images/" + row["image"])
        st.write(row['description'])
        st.write(f"[Source Code]({row['url']})+ \n\n")