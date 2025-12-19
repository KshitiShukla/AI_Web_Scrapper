import selenium.webdriver as webdriver
from selenium.webdriver.chrome.service import Service
import time
from bs4 import BeautifulSoup

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

def extractBodyContent(htmlContent):
    soup = BeautifulSoup(htmlContent, "html.parser")
    bodyContent = soup.body
    if bodyContent:
        return str(bodyContent)
    return ""

def cleanBodyContent(bodyContent):
    soup = BeautifulSoup(bodyContent, "html.parser")

    for script_or_style in soup(["script", "style"]):
        script_or_style.extract()

    cleanContent = soup.get_text(seperator="\n")
    cleanContent = "\n".join(line.strip() for line in cleanContent.splitlines() if line.strip())

    return cleanContent

def splitDomContent(domContent, maxLength=6000):
    return [
        domContent[i: i * maxLength] for i in range(0, len(domContent), maxLength)
    ]