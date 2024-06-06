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

# Click on the services page
service_btn = wait.until(EC.element_to_be_clickable
                         ((By.XPATH, '/html/body/div[1]/div[1]/div[2]/a[5]'))).click()

# Clicks at the register a client page
register_btn = wait.until(EC.element_to_be_clickable
                          ((By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/button'))).click()

# Inputs service name
title = input("Type the service's title: ")
title_input = wait.until(EC.element_to_be_clickable
                         ((By.XPATH, '/html/body/div[1]/div/div/form/div[1]/div[1]/div/div/input'))).send_keys(title)

# Inputs service price
price = input("Type the service's price (numebers only): ")
price_input = wait.until(EC.element_to_be_clickable
                         ((By.XPATH, '/html/body/div[1]/div/div/form/div[1]/div[2]/div/div/input'))).send_keys(price)

# Inputs the service description
description = input("Type the service's description: ")
description_input = wait.until(EC.element_to_be_clickable
                               ((By.XPATH, '/html/body/div[1]/div/div/form/div[1]/div[3]/div/div[2]/textarea'))).send_keys(description)

# Clicks at the save button
done_btn = wait.until(EC.element_to_be_clickable
                      ((By.XPATH, '/html/body/div[1]/div/div/form/div[2]/button'))).click() 

# Clicks at the close button
close_btn = wait.until(EC.element_to_be_clickable
                       ((By.XPATH, '/html/body/div[1]/form/button'))).click() 

time.sleep(10)

# Close the browser
driver.quit()
