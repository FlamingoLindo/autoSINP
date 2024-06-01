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

series = input("Type the vehicles series (numbers only): ")
brand = input("Type the vehicle brande (letters only): ")
year = input("Type the vehicle year (numbers only):")
model = input("Type the vehicle model ('Carros' or 'Caminhões leves'):")

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
email_input = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[2]/form/div[1]/div[1]/div/input')))
email_input.send_keys(os.getenv("CLIENT_LOGIN"))

# Wait for password input to be clickable
password_input = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[2]/form/div[1]/div[2]/div/input')))
password_input.send_keys(os.getenv("CLIENT_PASSWORD"))

# Clicks at the login button
login_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[2]/form/button')))
login_btn.click()

time.sleep(1)

# Click at the vehicle page
vehicle_page = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[1]/div[2]/a[3]')))
vehicle_page.click()

# Register a vehicle 
registervehicle_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/button')))
registervehicle_btn.click()

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

send_btn = wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[1]/div/div[1]/form/div[2]/button"))) 
send_btn.click()

time.sleep(10000)
# Close the browser
driver.quit()
