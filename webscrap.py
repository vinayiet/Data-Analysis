import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import pandas as pd


logging.basicConfig(
    filename="web_scraper.log",
    format="%(asctime)s - %(levelname)s - %(message)s",
    level=logging.INFO,
    datefmt="%Y-%m-%d %H:%M:%S"
)

logging.info("Script started.")

try:
    
    logging.info("Initializing WebDriver.")
    driver = webdriver.Firefox()

    
    logging.info("Navigating to the website.")
    driver.get('https://uk.investing.com/commodities/us-sugar-no11-historical-data')

    
    logging.info("Waiting for the page to load.")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

   
    logging.info("Selecting the 'Weekly' time frame.")
    try:
        time_frame_dropdown = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[text()='Weekly']"))
        )
        time_frame_dropdown.click()
        logging.info("Time Frame 'Weekly' selected.")
    except Exception as e:
        logging.error(f"Failed to select Time Frame: {str(e)}")

  
    logging.info("Entering date range.")
    try:
        
        date_range_field = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@class='flex flex-1 flex-col justify-center text-sm leading-5 text-[#333]']"))
        )
        driver.execute_script("arguments[0].click();", date_range_field)

      
        start_date = '17/08/2023'
        end_date = '17/08/2024'

        
        date_input = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//input[contains(@class, 'date-input-class')]"))  # Adjust with correct class name
        )

     
        driver.execute_script(f"arguments[0].value = '{start_date} - {end_date}';", date_input)

       
        apply_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[text()='Apply']"))
        )
        driver.execute_script("arguments[0].click();", apply_button)

        logging.info("Date range applied.")
    except Exception as e:
        logging.error(f"Failed to enter date range or click Apply button: {str(e)}")

    # --- Extract Table Data ---
    logging.info("Waiting for the table data to load.")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "table")))

    
    logging.info("Fetching updated page content and parsing it.")
    html_content_updated = driver.page_source
    soup_updated = BeautifulSoup(html_content_updated, 'html.parser')

  
    logging.info("Extracting table rows.")
    table_rows = soup_updated.find_all('tr', class_='relative h-[41px] after:absolute after:bottom-0 after:left-0 after:right-0 after:h-px after:bg-[#ECEDEF] hover:bg-[#F5F5F5] historical-data-v2_price__atUfP')

    headers = ['Date', 'Price', 'Open', 'High', 'Low', 'Vol.', 'Change %']
    data = []
    for row in table_rows:
        columns = row.find_all('td')
        row_data = [col.get_text(strip=True) for col in columns]
        data.append(row_data)

    df = pd.DataFrame(data, columns=headers)

   
    df.to_excel('historical_data.xlsx', index=False)

except Exception as e:
    logging.error(f"An error occurred: {str(e)}")

finally:
    logging.info("Closing the WebDriver.")
    driver.quit()
    logging.info("Script finished.")
