import streamlit as st
from scrape import (scrapeWebsite, cleanBodyContent, extractBodyContent, splitDomContent)

st.title("AI Web Scrapper")
url = st.text_input("Enter Website URL:")

if st.button("Scrape Site"):
    st.write("Scrapping Website")

    result = scrapeWebsite(url)
    bodyContent = extractBodyContent(result)
    cleanedContent = cleanBodyContent(bodyContent)

    st.session_state.dom_content = cleanedContent

    with st.expander("View DON Content"):
        st.text_area("DOM Content", cleanedContent, height=300)

if "dom_content" in st.session_state:
    parse_description = st.text_area("Describe what you want to parse?")

    if st.button("Parse Content"):
        if parse_description:
            st.write("Parsing the Content")

            dom_chunks = splitDomContent(st.session_state.dom_content)