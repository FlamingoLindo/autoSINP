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
import pyautogui

def random_year():
    return random.randint(1945, 2024)

load_dotenv()

# Path to your ChromeDriver
driver_path = './chromedriver.exe'
s = Service(driver_path)
driver = webdriver.Chrome(service=s)  

# Open the web page
driver.get(os.getenv('SINP_URL'))

# Initialize WebDriverWait
wait = WebDriverWait(driver, 5)
#aaaaada
# Wait for email input to be clickable
email_input = wait.until(EC.element_to_be_clickable
                         ((By.XPATH, '/html/body/div[1]/div[2]/form/div/div[1]/div/input'))).send_keys(os.getenv('SINP_LOGIN'))

# Wait for password input to be clickable
password_input = wait.until(EC.element_to_be_clickable
                            ((By.XPATH, '/html/body/div[1]/div[2]/form/div/div[2]/div/input'))).send_keys(os.getenv('SINP_PASSWORD'))

# Click on login button
login_btn = wait.until(EC.element_to_be_clickable
                       ((By.XPATH, '/html/body/div[1]/div[2]/form/button'))).click()

# Click vehicles page
vehicle_btn = wait.until(EC.element_to_be_clickable
                         ((By.XPATH, '/html/body/div[1]/div[1]/div[2]/a[3]'))).click()

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
        register_btn = wait.until(EC.element_to_be_clickable
                                  ((By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/button'))).click()

        # Inputs the vehicle type
        option_type = random.randint(0, 4)
        vehicle_type_dropdown = wait.until(EC.element_to_be_clickable
                                           ((By.XPATH, '/html/body/div[1]/div/div/form/div[1]/div[1]/div/div/div/div/div[1]/div[2]')
                                            )).click()
        
        type_option = wait.until(EC.element_to_be_clickable
                                 ((By.XPATH, f"//div[@id='react-select-2-option-{option_type}']")
                                  )).click()

        # Inputs the vehicle model
        vehicle_model = wait.until(EC.element_to_be_clickable
                                  ((By.XPATH, '/html/body/div[1]/div/div/form/div[1]/div[2]/div/div/input')
                                   )).send_keys(row['modelo'])
        
        # Inputs vehicle series
        series_input = wait.until(EC.element_to_be_clickable
                                  ((By.XPATH, '/html/body/div[1]/div/div/form/div[1]/div[3]/div/div/input')
                                   )).send_keys(row['serie'])

        # Inputs the vehicle fuel type
        option_fuel = random.randint(0, 2)
        vehicle_fuel_dropdown = wait.until(EC.element_to_be_clickable
                                           ((By.XPATH, '/html/body/div[1]/div/div/form/div[1]/div[4]/div/div/div/div/div[1]/div[2]')
                                            )).click()

        fuel_option = wait.until(EC.element_to_be_clickable
                                 ((By.XPATH, f"//div[@id='react-select-3-option-{option_fuel}']")
                                  )).click()

        # Inputs vehicle brand
        brand_input = wait.until(EC.element_to_be_clickable
                                 ((By.XPATH, '/html/body/div[1]/div/div/form/div[1]/div[5]/div/div/input')
                                  )).send_keys(row['marca'])

        # Inputs vehicle year
        year_input = wait.until(EC.element_to_be_clickable
                                ((By.XPATH, '/html/body/div[1]/div/div/form/div[1]/div[6]/div/div/input')
                                 )).send_keys(random_year())
        
        # Register button
        done_btn = wait.until(EC.element_to_be_clickable
                              ((By.XPATH, '/html/body/div[1]/div/div/form/div[2]/button')
                               )).click()

        # Confirm register button
        confirm_btn = wait.until(EC.element_to_be_clickable
                                 ((By.XPATH, '/html/body/div[1]/form/button')
                                  )).click()

        pyautogui.hotkey('f5')
        
# Close the browser
driver.quit()
