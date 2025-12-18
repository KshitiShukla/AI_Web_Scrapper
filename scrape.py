import selenium.webdriver as webdriver
from selenium.webdriver.chrome.service import Service
import time

def scrapeWebsite(website):
    print("Launching chrome browser...")

    chrome_drive_path = "./chromedriver.exe"
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=Service(chrome_drive_path), options=options)

    try:
        driver.get(website)
        print("Page Loaded...")
        html = driver.page_source
        time.sleep(10)

        return html
    finally:
        driver.quit()