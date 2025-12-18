import streamlit as st
from scrape import scrapeWebsite

st.title("AI Web Scrapper")
url = st.text_input("Enter Website URL:")

if st.button("Scrape Site"):
    st.write("Scrapping Website")
    result = scrapeWebsite(url)
    print(result)