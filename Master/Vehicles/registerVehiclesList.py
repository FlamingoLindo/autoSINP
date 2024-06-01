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

# Contract file
#contract_file = "C:/Users/josef/Desktop/After life, death/SINP/autoSINP/SINP_-_Master_Web.pdf"

# Open the web page
driver.get(os.getenv('SINP_URL'))

# Initialize WebDriverWait
wait = WebDriverWait(driver, 5)
#aaaaada
# Wait for email input to be clickable
email_input = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[2]/form/div/div[1]/div/input')))
email_input.send_keys(os.getenv('SINP_LOGIN'))

# Wait for password input to be clickable
password_input = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[2]/form/div/div[2]/div/input')))
password_input.send_keys(os.getenv('SINP_PASSWORD'))

# Click on login button
login_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[2]/form/button')))
login_btn.click()

# Click vehicles page
vehicle_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[1]/div[2]/a[3]')))
vehicle_btn.click()

# Ask the user for car manufacturers (separated by commas)
manufacturers = input("Please enter car manufacturers (separated by commas): ").split(',')

# Initialize the notification ID
notification_id = 1

# Iterate over each manufacturer
for manufacturer in manufacturers:
    manufacturer = manufacturer.strip()  # Trim any extra spaces

    # Load the Excel file for the specified manufacturer
    file_path = f'Files\Excel\{manufacturer}.xlsx'
    
    df = pd.read_excel(file_path)

    # Iterate over each row in the DataFrame
    for index, row in df.iterrows():
        # Show what index it's currently inputting (Just for debugging)
        print(f"Processing row {index} for manufacturer {manufacturer}")

        # Clicks at the register a client page
        register_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/button')))
        register_btn.click()

        # Inputs the vehicle type
        vehicle_type_dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/form/div[1]/div[1]/div/div/div/div/div[1]/div[2]')))
        vehicle_type_dropdown.click()
        type_option = wait.until(EC.element_to_be_clickable((By.XPATH, f"//div[contains(text(), 'Carros')]")))
        type_option.click()

        # Inputs the vehicle model
        vehicle_model_dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/form/div[1]/div[2]/div/div/div/div/div[1]/div[2]')))
        vehicle_model_dropdown.click()
        model_select = wait.until(EC.element_to_be_clickable((By.XPATH,"//input[@type='checkbox']"))) 
        model_select.click()

        # Inputs vehicle series
        series_input = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/form/div[1]/div[3]/div/div/input')))
        series_input.send_keys(row['serie'])

        # Inputs the vehicle fuel type
        vehicle_fuel_dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/form/div[1]/div[4]/div/div/div/div/div[1]/div[2]')))
        vehicle_fuel_dropdown.click()
        fuel_option = wait.until(EC.element_to_be_clickable((By.XPATH, f"//div[contains(text(), 'Diesel')]")))
        fuel_option.click()
        
        # Inputs vehicle brand
        brand_input = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/form/div[1]/div[5]/div/div/input')))
        brand_input.send_keys(row['marca'])

        # Inputs vehicle year
        year_input = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/form/div[1]/div[6]/div/div/input')))
        year_input.send_keys("2003")
        
        # Register button
        done_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/form/div[2]/button')))
        done_btn.click()

        # Confirm register button
        confirm_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/form/button')))
        confirm_btn.click()

        # Close the button with dynamically changing ID
        close_notify_btn_xpath = f'//*[@id="{notification_id}"]'
        close_notify_btn = wait.until(EC.element_to_be_clickable((By.XPATH, close_notify_btn_xpath)))
        close_notify_btn.click()

        # Increment the ID for the next iteration
        notification_id += 1
    

# Close the browser
driver.quit()
