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
load_dotenv()

# Create a CPF (it might not be valid sometimes)
def gera_cpf():
    cpf = [random.randint(0, 9) for _ in range(9)]
    soma1 = sum(x * y for x, y in zip(cpf, range(10, 1, -1)))
    digito1 = (soma1 * 10 % 11) % 10
    cpf.append(digito1)
    
    soma2 = sum(x * y for x, y in zip(cpf, range(11, 1, -1)))
    digito2 = (soma2 * 10 % 11) % 10
    cpf.append(digito2)
    
    cpf_formatado = ''.join(map(str, cpf))
    return cpf_formatado[:3] + '.' + cpf_formatado[3:6] + '.' + cpf_formatado[6:9] + '-' + cpf_formatado[9:]

def valida_cpf(cpf):
    cpf_numeros = [int(char) for char in cpf if char.isdigit()]
    
    if len(cpf_numeros) != 11:
        return False
    
    # Validar primeiro dígito
    soma1 = sum(x * y for x, y in zip(cpf_numeros[:9], range(10, 1, -1)))
    digito1 = (soma1 * 10 % 11) % 10
    if cpf_numeros[9] != digito1:
        return False
    
    # Validar segundo dígito
    soma2 = sum(x * y for x, y in zip(cpf_numeros[:10], range(11, 1, -1)))
    digito2 = (soma2 * 10 % 11) % 10
    if cpf_numeros[10] != digito2:
        return False
    
    return True

def gera_e_valida_cpf():
    while True:
        cpf = gera_cpf()
        if valida_cpf(cpf):
            return cpf

# Path to your ChromeDriver
driver_path = './chromedriver.exe'
s = Service(driver_path)
driver = webdriver.Chrome(service=s)  

# Open the web page
driver.get(os.getenv('CLIENT_URL'))

# Initialize WebDriverWait
wait = WebDriverWait(driver, 5)
time.sleep(2)

# Wait for email input to be clickable
email_input = wait.until(EC.element_to_be_clickable
                         ((By.XPATH, '/html/body/div[1]/div[2]/form/div[1]/div[1]/div/input'))).send_keys(os.getenv("CLIENT_LOGIN"))

# Wait for password input to be clickable
password_input = wait.until(EC.element_to_be_clickable
                            ((By.XPATH, '/html/body/div[1]/div[2]/form/div[1]/div[2]/div/input'))).send_keys(os.getenv("CLIENT_PASSWORD"))

# Clicks at the login button
login_btn = wait.until(EC.element_to_be_clickable
                       ((By.XPATH, '/html/body/div[1]/div[2]/form/button'))).click()

time.sleep(1)

# Click at the vehicle page
vehicle_page = wait.until(EC.element_to_be_clickable
                          ((By.XPATH, '/html/body/div[1]/div[1]/div[2]/a[3]'))).click()

# Register a vehicle 
registervehicle_btn = wait.until(EC.element_to_be_clickable
                                 ((By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/button'))).click()

# Vehicle type
option_type = 0
type = input("Type the vehicle type ('Carros' or 'Caminhões leves'): ")

if type == "Caminhões leves" or type == "caminhoes leves" or "caminhoes" or "Caminhoes":
    option_type = 1

type_dropdown = wait.until(EC.element_to_be_clickable
                           ((By.CSS_SELECTOR, 
                             'body > div.sc-49d27906-0.gkZnae > div > div.sc-3d34bb33-2.eWmjga > form > div.sc-6fcf6ce7-1.kHGnmO > div:nth-child(1) > div > div > div > div > div.css-8akrpk > div.css-19bb58m')
                            )).click()

type_select = wait.until(EC.element_to_be_clickable
                         ((By.XPATH, f"//div[@id='react-select-2-option-{option_type}']"))).click()

# Vehicle model
option_model = 2
model = input("Type the vehicle model ('ford' or 'toyota'): ")

if model == "ford":
    option_model = 1
    
model_dropdown = wait.until(EC.element_to_be_clickable
                            ((By.XPATH, '/html/body/div[1]/div/div[1]/form/div[1]/div[2]/div/div/div/div/div[1]/div[2]'))).click()

model_select = wait.until(EC.element_to_be_clickable
                          ((By.XPATH,f"//div[@id='react-select-3-listbox']/div[{option_model}]/input"))).click()


# Vehicle series
series = input("Type the vehicles series (numbers only): ")
series_input = wait.until(EC.element_to_be_clickable
                          ((By.XPATH, '/html/body/div[1]/div/div[1]/form/div[1]/div[3]/div/div/input'))).send_keys(series)

# Vehicle fuel
option_fuel = 1
fuel = input("Type the fuel type ('diesel' or 'diesel10'): ")

if fuel == "diesel" or type == "diesel":
    option_model = 2
    
vehicle_fuel_dropdown = wait.until(EC.element_to_be_clickable
                                   ((By.XPATH, '/html/body/div[1]/div/div[1]/form/div[1]/div[4]/div/div/div/div/div[1]/div[2]'))).click()

fuel_option = wait.until(EC.element_to_be_clickable
                         ((By.XPATH, f"//div[@id='react-select-4-option-{option_fuel}']"))).click()


brand = input("Type the vehicle brande (letters only): ")
brand_input = wait.until(EC.element_to_be_clickable
                         ((By.XPATH, '/html/body/div[1]/div/div[1]/form/div[1]/div[5]/div/div/input'))).send_keys(brand)

year = input("Type the vehicle year (numbers only):")
year_input = wait.until(EC.element_to_be_clickable
                        ((By.XPATH, '/html/body/div[1]/div/div[1]/form/div[1]/div[6]/div/div/input'))).send_keys(year)

send_btn = wait.until(EC.element_to_be_clickable
                      ((By.XPATH,"/html/body/div[1]/div/div[1]/form/div[2]/button"))).click()

time.sleep(10000)
# Close the browser
driver.quit()
