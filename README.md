# AI_Web_Scrapper

AI_WEB_SCRAPPER is a Streamlit-based application that scrapes website content, cleans and processes the DOM, and uses an LLM (Ollama – LLaMA 3) to extract user-defined information from the scraped data.

The project combines browser automation, HTML parsing, and AI-driven text extraction into a single interactive interface.

# Project Overview

This application allows users to:
- Input a website URL
- Scrape and clean the website’s body content
- View the extracted DOM text
- Describe what information they want to extract
- Use an AI model to parse and return only the requested data
The parsing logic strictly returns only the data matching the user’s description, without additional explanations or formatting.

# Application Flow

1. User enters a website URL in the Streamlit interface
2. The application:
- Loads the website using a remote Chromium browser
- Waits for CAPTCHA resolution
- Extracts and cleans the <body> content
3. Cleaned DOM content is stored in session state
4. User provides a natural language description of what to extract
5. The content is split into chunks and processed by the LLM
6. The extracted information is displayed in the UI

# AI Parsing Logic

The parsing system follows strict rules:
- Extracts only the information matching the user’s description
- Returns no additional commentary or formatting
- Outputs an empty string if no relevant data exists
- Processes large content safely using chunk-based parsing
This ensures accurate and focused data extraction.

# Dependencies and Technologies
- Streamlit – User Interface
- Selenium – Browser automation
- Chromium Remote WebDriver – Website access and CAPTCHA handling
- BeautifulSoup – HTML parsing and cleaning
- LangChain – Prompt management
- Ollama – Local LLM execution (LLaMA 3)
- dotenv – Environment variable management

# Environment Configuration

The project uses an environment variable for browser connectivity:
- SBR_WEBDRIVER: Stores the remote Chromium WebDriver endpoint
This value is loaded at runtime using dotenv

# Intended Use Cases
- Extracting specific information from websites
- Parsing structured or semi-structured web content
- AI-assisted data extraction using natural language instructions
- Processing large webpages with minimal manual filtering

# Limitations
- CAPTCHA handling depends on the configured scraping browser
- Parsing accuracy depends on webpage content structure
- Requires a running Ollama instance with LLaMA 3 available
