import pandas as pd
import pyautogui
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
from pynput.keyboard import Key, Controller

load_dotenv()

image_path =  r"C:\Users\josef\Desktop\AfterLifeDeath\SINP\autoSINP-main\Files\Random\capacitor.webp"
document_path = r"C:\Users\josef\Desktop\AfterLifeDeath\SINP\autoSINP-main\Files\Random\1.pdf"

# Path to your ChromeDriver
driver_path = './chromedriver.exe'
s = Service(driver_path)
driver = webdriver.Chrome(service=s)

# Open the web page
driver.get(os.getenv('SINP_URL'))

# Initialize WebDriverWait
wait = WebDriverWait(driver, 10)

# Wait for email input to be clickable
email_input = wait.until(EC.element_to_be_clickable
                         ((By.XPATH, '/html/body/div[1]/div[2]/form/div/div[1]/div/input'))).send_keys(os.getenv('SINP_LOGIN'))

# Wait for password input to be clickable
password_input = wait.until(EC.element_to_be_clickable
                            ((By.XPATH, '/html/body/div[1]/div[2]/form/div/div[2]/div/input'))).send_keys(os.getenv('SINP_PASSWORD'))

# Click on login button
login_btn = wait.until(EC.element_to_be_clickable
                       ((By.XPATH, '/html/body/div[1]/div[2]/form/button'))).click()

# Click on the products page
products_btn = wait.until(EC.element_to_be_clickable
                          ((By.XPATH, '/html/body/div[1]/div[1]/div[2]/a[4]'))).click()

# Open the register a client page
register_btn = wait.until(EC.element_to_be_clickable
                          ((By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/button'))).click()

# Inputs the product's image
image_btn = wait.until(EC.element_to_be_clickable
                       ((By.XPATH, '/html/body/div[1]/div/div/form/div[1]/div[1]/div[1]/div'))).click()
pyautogui.press('tab')
pyautogui.press('enter')
time.sleep(1.5)
pyautogui.write(image_path)
time.sleep(1.5)
pyautogui.press('enter')

# Inputs the product's document
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('enter')
time.sleep(1.5)
pyautogui.write(document_path)
time.sleep(1.5)
pyautogui.press('enter')

# Inputs the product's name
name = input("Type the product's name: ")
name_input = wait.until(EC.element_to_be_clickable
                        ((By.XPATH, '/html/body/div[1]/div/div/form/div[1]/div[3]/div/div/input'))).send_keys(name)

# Inputs the product's model
option_model = random.randint(1, 2)
model_dropdown = wait.until(EC.element_to_be_clickable
                            ((By.XPATH, '/html/body/div[1]/div/div/form/div[1]/div[4]/div/div/div/div/div[1]/div[2]'))).click() 
model_select = wait.until(EC.element_to_be_clickable
                          ((By.XPATH, f"//div[@id='react-select-2-listbox']/div[{option_model}]/input"))).click()

# Inputs the product's type
option_type = random.randint(0, 1)
model_dropdown = wait.until(EC.element_to_be_clickable
                            ((By.XPATH, '/html/body/div[1]/div/div/form/div[1]/div[5]/div/div/div/div/div[1]/div[2]'))).click() 
type_option = wait.until(EC.element_to_be_clickable
                         ((By.XPATH, f"//div[@id='react-select-3-listbox']/div[{option_model}]/input"))).click()

# Inputs product's price
price = input("Enter the product's price (numbers only): ")
price_input = wait.until(EC.element_to_be_clickable
                         ((By.XPATH, '/html/body/div[1]/div/div/form/div[1]/div[6]/div/div/input'))).click()
price_input.send_keys(price)

# Inputs the product's description
description = input("Type the product's description: ")
description_input = wait.until(EC.element_to_be_clickable
                               ((By.XPATH, '/html/body/div[1]/div/div/form/div[1]/div[7]/div/div[2]/textarea'))).click()
description_input.send_keys(description)

# Clicks the save button
done_btn = wait.until(EC.element_to_be_clickable
                      ((By.XPATH, '/html/body/div[1]/div/div/form/div[2]/button'))).click()

# Clicks the close button
close_btn = wait.until(EC.element_to_be_clickable
                       ((By.XPATH, '/html/body/div[1]/form/button'))).click()


time.sleep(1010101)
# Close the browser
driver.quit()
