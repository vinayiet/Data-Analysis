import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import pandas as pd
import requests

# Setup Logging
logging.basicConfig(
    filename="web_scraper.log",
    format="%(asctime)s - %(levelname)s - %(message)s",
    level=logging.INFO,
    datefmt="%Y-%m-%d %H:%M:%S"
)

logging.info("Script started.")

# URL to be tested
test_url = 'https://uk.investing.com/commodities/us-sugar-no11-historical-data'

try:
    # Check URL Availability
    logging.info(f"Checking availability of URL: {test_url}")
    response = requests.get(test_url)
    if response.status_code == 200:
        logging.info("URL is reachable.")
    else:
        logging.error(f"URL returned status code: {response.status_code}")
    
    # Initialize WebDriver (Using Firefox in this case)
    logging.info("Initializing WebDriver.")
    driver = webdriver.Firefox()

    # Navigate to the webpage
    logging.info("Navigating to the website.")
    driver.get(test_url)

    # Wait for the page to fully load
    logging.info("Waiting for the page to load.")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Continue with the rest of your script here

except Exception as e:
    logging.error(f"An error occurred: {str(e)}")

finally:
    logging.info("Closing the WebDriver.")
    driver.quit()
    logging.info("Script finished.")