import streamlit as st
import requests

st.title("AI-Powered SDLC Virtual Pod")

requirements = st.text_area("Enter Business Requirements")
if st.button("Generate User Stories"):
    response = requests.get(f"http://localhost:8000/generate_user_stories/?requirements={requirements}")
    st.write(response.json()["user_stories"])
