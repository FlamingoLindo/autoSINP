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

print("https://www.4devs.com.br/gerador_de_pessoas")

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

# Opens the budget form
new_budget_btn = wait.until(EC.element_to_be_clickable
                            ((By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/button'))).click()

# Inputs budget's info
name = input("Type the client's name: ")
name_input = wait.until(EC.element_to_be_clickable
                        ((By.XPATH, '/html/body/div[1]/div/div[1]/form/div[1]/div[1]/div/div/input'))).send_keys(name)

phone = input("Type the client's phone number: ")
phone_input = wait.until(EC.element_to_be_clickable
                         ((By.XPATH, '/html/body/div[1]/div/div[1]/form/div[1]/div[2]/div[1]/div/input'))).send_keys(phone)

cpf = gera_e_valida_cpf()
cpf_input = wait.until(EC.element_to_be_clickable
                       ((By.XPATH, '/html/body/div[1]/div/div[1]/form/div[1]/div[2]/div[2]/div/input'))).send_keys(cpf)

email = input("Type the client's email: ")
email_input = wait.until(EC.element_to_be_clickable
                         ((By.XPATH, '/html/body/div[1]/div/div[1]/form/div[1]/div[3]/div/input'))).send_keys(email)

cep = input("Type the client's CEP (number only): ")
cep_input = wait.until(EC.element_to_be_clickable
                       ((By.XPATH, '/html/body/div[1]/div/div[1]/form/div[1]/div[4]/div[1]/div/input'))).send_keys(cep)

description_input = wait.until(EC.element_to_be_clickable
                               ((By.XPATH, '/html/body/div[1]/div/div[1]/form/div[1]/div[7]/div[2]/textarea'))).send_keys("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.")

time.sleep(3)

addreNum = random.randint(1, 9999)
adressNum_input = wait.until(EC.element_to_be_clickable
                             ((By.XPATH, '/html/body/div[1]/div/div[1]/form/div[1]/div[4]/div[2]/div/input'))).send_keys(addreNum)

next_btn1 = wait.until(EC.element_to_be_clickable
                       ((By.XPATH, '/html/body/div[1]/div/div[1]/form/div[2]/button'))).click()

option_type = 0
type = input("Type the vehicle type ('Carros' or 'Caminhões leves'): ")

if type == "Caminhões leves" or type == "caminhoes leves" or "caminhoes" or "Caminhoes":
    option_type = 1

type_dropdown = wait.until(EC.element_to_be_clickable
                           ((By.XPATH, '/html/body/div[1]/div/div[1]/form/div[1]/div'))).click()

type_select = wait.until(EC.element_to_be_clickable
                         ((By.XPATH, f"//div[@id='react-select-2-option-{option_type}']"))).click()

modelInput = input("Type the vehicle model ('Toyota Corolla LE' or 'Ford Mustang GT')")
adressNum_input = wait.until(EC.element_to_be_clickable
                             ((By.XPATH, '/html/body/div[1]/div/div[1]/form/div[2]/div/input'))).send_keys(modelInput)

time.sleep(3)

first_option = wait.until(EC.element_to_be_clickable
                           ((By.XPATH, '/html/body/div[1]/div/div[1]/form/table/tbody/tr[1]/td[1]/div/div/div'))).click()

next_btn2 = wait.until(EC.element_to_be_clickable
                           ((By.XPATH, '/html/body/div[1]/div/div[1]/form/div[4]/button[2]'))).click()

time.sleep(1.2)

time.sleep(2)

# Find all items by the common class
all_items = driver.find_elements(By.CLASS_NAME, 'sc-a465b61e-1.dAkyrc')

# Iterate over all items starting from the first one and perform desired actions
for index, item in enumerate(all_items):
    # Perform actions for each item
    # Example: clicking the item if it's clickable
    try:
        wait.until(EC.element_to_be_clickable(item)).click()
        # Wait until the quantity button is clickable and click it 10 times
        quantity_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="Caminho_61858"]')))
        for _ in range(10):
            quantity_button.click()
        print(f"Clicked item {index+1}")
    except Exception as e:
        print(f"Could not click item {index+1}: {e}")

next_btn = wait.until(EC.element_to_be_clickable
                      ((By.XPATH, '/html/body/div[1]/div/div[1]/form/div[3]/button[2]'))).click()

time.sleep(3)

# Wait for all elements with the class 'sc-a465b61e-1 dAkyrc' to be present
all_services = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'sc-a465b61e-1.dAkyrc')))

# Iterate over all found elements and perform actions
for index, service in enumerate(all_services):
    try:
        # Wait for the current element to be clickable and click it
        clickable_service = wait.until(EC.element_to_be_clickable((By.XPATH, f"(//div[@class='sc-a465b61e-1 dAkyrc'])[{index + 1}]")))
        clickable_service.click()
        print(f"Clicked service {index + 1}")
    except Exception as e:
        print(f"Could not click service {index + 1}: {e}")

next_btn = wait.until(EC.element_to_be_clickable
                      ((By.XPATH, '/html/body/div[1]/div/div[1]/form/div[3]/button[2]'))).click()

after_disc_btn = wait.until(EC.element_to_be_clickable
                            ((By.XPATH, '/html/body/div[1]/div/div[1]/form/div[4]/button[2]'))).click()

submit_btn = wait.until(EC.element_to_be_clickable
                        ((By.XPATH, '/html/body/div[1]/div/div[1]/form/div[2]/button[2]'))).click()

time.sleep(10000)
# Close the browser
driver.quit()
