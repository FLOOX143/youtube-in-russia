import streamlit as st

url = st.text_input('Enter the url of video: ')

if url:
    st.video(url)
