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

# Clicks at the register a vehicle page
register_btn = wait.until(EC.element_to_be_clickable
                          ((By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/button'))).click()

# Chooses the vehicle type
option_type = 0
type = input("Type the vehicle type ('Carros' or 'Caminhões leves'): ")

if type == "Caminhões leves" or type == "caminhoes leves" or "caminhoes" or "Caminhoes":
    option_type = 1
    
type_dropdown = wait.until(EC.element_to_be_clickable
                           ((By.XPATH, '/html/body/div[1]/div/div[1]/form/div[1]/div[1]/div/div/div/div/div[1]/div[2]'))).click()
 
type_select = wait.until(EC.element_to_be_clickable
                         ((By.XPATH, f"//div[@id='react-select-2-option-{option_type}']"))).click()

# Chooses the vehicle model
option_model = 1
model = input("Type the vehicle model ('ford' or 'toyota'): ")

if type == "toyota":
    option_model = 2

model_dropdown = wait.until(EC.element_to_be_clickable
                            ((By.XPATH, '/html/body/div[1]/div/div/form/div[1]/div[2]/div/div/div'))).click()

model_select = wait.until(EC.element_to_be_clickable
                          ((By.XPATH, f"//div[@id='react-select-3-listbox']/div[{option_model}]/input"))).click()

# Chooses the vehicle series
series = input("Type the vehicles series (numbers only): ")
series_input = wait.until(EC.element_to_be_clickable
                          ((By.XPATH, '/html/body/div[1]/div/div[1]/form/div[1]/div[3]/div/div/input'))).send_keys(series)

# Chooses the vehicle fuel
option_fuel = 1
fuel = input("Type the fuel type ('diesel' or 'diesel10'): ")

if fuel == "diesel" or type == "diesel":
    option_model = 2

vehicle_fuel_dropdown = wait.until(EC.element_to_be_clickable
                                   ((By.XPATH, '/html/body/div[1]/div/div[1]/form/div[1]/div[4]/div/div/div/div/div[1]/div[2]'))).click()

fuel_option = wait.until(EC.element_to_be_clickable
                         ((By.XPATH, f"//div[@id='react-select-4-option-{option_fuel}']"))).click()

# Chooses the vehicle brand
brand = input("Type the vehicle brande (letters only): ")
brand_input = wait.until(EC.element_to_be_clickable
                         ((By.XPATH, '/html/body/div[1]/div/div[1]/form/div[1]/div[5]/div/div/input'))).send_keys(brand)

# Chooses the vehicle year
year = input("Type the vehicle year (numbers only):")
year_input = wait.until(EC.element_to_be_clickable
                        ((By.XPATH, '/html/body/div[1]/div/div[1]/form/div[1]/div[6]/div/div/input'))).send_keys(year)

# Clicks at the save button
done_btn = wait.until(EC.element_to_be_clickable
                      ((By.XPATH, '/html/body/div[1]/div/div/form/div[2]/button'))).click() 

# Clicks at the close button
close_btn = wait.until(EC.element_to_be_clickable
                       ((By.XPATH, '/html/body/div[1]/form/button'))).click() 

time.sleep(10)

# Close the browser
driver.quit()
