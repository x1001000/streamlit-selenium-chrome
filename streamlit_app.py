import streamlit as st

"""
## Web scraping on Streamlit Cloud with Selenium

[![Source](https://img.shields.io/badge/View-Source-<COLOR>.svg)](https://github.com/snehankekre/streamlit-selenium-chrome/)

This is a minimal, reproducible example of how to scrape the web with Selenium and Chrome on Streamlit's Community Cloud.

Fork this repo, and edit `/streamlit_app.py` to customize this app to your heart's desire. :heart:
"""

with st.echo():
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.chrome.service import Service
    from webdriver_manager.chrome import ChromeDriverManager

    @st.cache_resource
    def get_driver():
        return webdriver.Chrome(
            service=Service(ChromeDriverManager().install()), options=options
        )

    options = Options()
    options.add_argument("--disable-gpu")
    options.add_argument("--headless")
    # Specify the path to the installed Chromium binary
    # on Streamlit's Community Cloud
    # Update this path to match the path of the installed Chromium binary
    # on your local machine
    options.binary_location = "/usr/bin/chromium"  

    driver = get_driver()
    driver.get("http://example.com")

    st.code(driver.page_source)
