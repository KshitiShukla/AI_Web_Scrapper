import streamlit as st

st.title("AI Web Scrapper")
url = st.text_input("Enter Website URL:")

if st.button("Scrape Site"):
    st.write("Scrapping Website")