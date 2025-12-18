import streamlit as st
from scrape import scrapeWebsite
from bs4 import BeautifulSoup

st.title("AI Web Scrapper")
url = st.text_input("Enter Website URL:")

if st.button("Scrape Site"):
    st.write("Scrapping Website")
    result = scrapeWebsite(url)
    print(result)

def extractBodyContent(htmlContent):
    soup = BeautifulSoup(htmlContent, "html.parser")
    bodyContent = soup.body
    if bodyContent:
        return str(bodyContent)
    return ""