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

series = input("Type the vehicles series (numbers only): ")
brand = input("Type the vehicle brande (letters only): ")
year = input("Type the vehicle year (numbers only):")
model = input("Type the vehicle model ('Carros' or 'Caminhões leves'):")

# Path to your ChromeDriver
driver_path = './chromedriver.exe'
s = Service(driver_path)
driver = webdriver.Chrome(service=s)  

# Open the web page
driver.get(os.getenv('SINP_URL'))

# Initialize WebDriverWait
wait = WebDriverWait(driver, 5)

# Wait for email input to be clickable
email_input = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[2]/form/div/div[1]/div/input')))
email_input.send_keys(os.getenv('SINP_LOGIN'))

# Wait for password input to be clickable
password_input = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[2]/form/div/div[2]/div/input')))
password_input.send_keys(os.getenv('SINP_PASSWORD'))

# Click on login button
login_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[2]/form/button')))
login_btn.click()

time.sleep(1)

# Click on the vehicles page
vehicles_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[1]/div[2]/a[3]')))
vehicles_btn.click()

# Clicks at the register a vehicle page
register_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/button')))
register_btn.click()

type_dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[1]/form/div[1]/div[1]/div/div/div/div/div[1]/div[2]')))
type_dropdown.click()  
type_select = wait.until(EC.element_to_be_clickable((By.XPATH, f"//div[contains(text(), '{model}')]")))
type_select.click()

model_dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[1]/form/div[1]/div[2]/div/div/div/div/div[1]/div[2]')))
model_dropdown.click()
model_select = wait.until(EC.element_to_be_clickable((By.XPATH,"//input[@type='checkbox']"))) 
model_select.click()

series_input = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[1]/form/div[1]/div[3]/div/div/input')))
series_input.send_keys(series)

vehicle_fuel_dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[1]/form/div[1]/div[4]/div/div/div/div/div[1]/div[2]')))
vehicle_fuel_dropdown.click()
fuel_option = wait.until(EC.element_to_be_clickable((By.XPATH, f"//div[contains(text(), 'Diesel')]")))
fuel_option.click()

brand_input = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[1]/form/div[1]/div[5]/div/div/input')))
brand_input.send_keys(brand)

year_input = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[1]/form/div[1]/div[6]/div/div/input')))
year_input.send_keys(year)

# Clicks at the save button
done_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/form/div[2]/button')))
done_btn.click() 

# Clicks at the close button
close_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/form/button')))
close_btn.click() 

time.sleep(10)

# Close the browser
driver.quit()
