import sys
print(f"Python executable: {sys.executable}")
import streamlit as st
from scrape import scrape_website
st.title('AI Web Scraper')

url = st.text_input('Enter a website URL')

if st.button('Scrape site'):
    st.write("Scraping site...")
    result = scrape_website(url)
    print(result)