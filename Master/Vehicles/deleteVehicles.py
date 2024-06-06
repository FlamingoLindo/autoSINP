import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import random
import time
from dotenv import load_dotenv
import os

load_dotenv()

# Path to your ChromeDriver
driver_path = './chromedriver.exe'
s = Service(driver_path)
driver = webdriver.Chrome(service=s)  

# Open the web page
driver.get(os.getenv('SINP_URL'))

# Initialize WebDriverWait
wait = WebDriverWait(driver, 5)

# Wait for email input to be clickable
email_input = wait.until(EC.element_to_be_clickable
                         ((By.XPATH, '/html/body/div[1]/div[2]/form/div/div[1]/div/input'))).send_keys(os.getenv('SINP_LOGIN'))

# Wait for password input to be clickable
password_input = wait.until(EC.element_to_be_clickable
                            ((By.XPATH, '/html/body/div[1]/div[2]/form/div/div[2]/div/input'))).send_keys(os.getenv('SINP_PASSWORD'))
# Click on login button
login_btn = wait.until(EC.element_to_be_clickable
                       ((By.XPATH, '/html/body/div[1]/div[2]/form/button'))).click()

time.sleep(1)

# Click on the vehicles page
vehicles_btn = wait.until(EC.element_to_be_clickable
                          ((By.XPATH, '/html/body/div[1]/div[1]/div[2]/a[3]'))).click()

notification_id = 1
# Click on the delete button
for _ in range(999999):
    delete = wait.until(EC.element_to_be_clickable
                        ((By.XPATH, '/html/body/div[1]/div[2]/div[2]/div[2]/div/div[1]/table/tbody/tr[1]/td[7]/div/button[2]'))).click()

    delete2 = wait.until(EC.element_to_be_clickable
                         ((By.XPATH, '/html/body/div[1]/form/div/button[2]'))).click()

    close = wait.until(EC.element_to_be_clickable
                       ((By.XPATH, '/html/body/div[1]/form/button'))).click()

    time.sleep(1)
    
    # Close the button with dynamically changing ID
    close_notify_btn_xpath = f'//*[@id="{notification_id}"]'
    close_notify_btn = wait.until(EC.element_to_be_clickable
                                  ((By.XPATH, close_notify_btn_xpath))).click()

    # Increment the ID for the next iteration
    notification_id += 1

time.sleep(10)

# Close the browser
driver.quit()
