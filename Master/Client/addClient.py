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

senha = 12345678

document_path = r"C:\Users\josef\Desktop\AfterLifeDeath\SINP\autoSINP-main\Files\Random\1.pdf"

# Create a CPF (it might not be valid sometimes)
def gera_cpf():
    cpf = [random.randint(0, 9) for _ in range(9)]
    soma = sum(x * y for x, y in zip(cpf, range(10, 1, -1)))
    cpf.append((soma * 10) % 11)
    soma = sum(x * y for x, y in zip(cpf, range(11, 1, -1)))
    cpf.append((soma * 10) % 11)
    cpf_formatado = ''.join(map(str, cpf))
    return cpf_formatado[:3] + '.' + cpf_formatado[3:6] + '.' + cpf_formatado[6:9] + '-' + cpf_formatado[9:]

def gera_parcela():
    parcela = [random.randint(1, 999999999)]
    return parcela

def gera_num_par():
    num = [random.randint(1, 12)]
    return num

def gera_aviso():
    aviso = [random.randint(1, 29)]
    return aviso

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

# Clicks at the register a client page
register_btn = wait.until(EC.element_to_be_clickable
                          ((By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/button'))).click()

# Inputs name
name = input("Type the client's name: ")
name_input = wait.until(EC.element_to_be_clickable
                        ((By.XPATH, '/html/body/div[1]/div/div/form/div[1]/div[1]/div/div/input'))).send_keys(name)

# Click at the CPF radial button
cpf_radio = wait.until(EC.element_to_be_clickable
                       ((By.XPATH, '//*[@id="cpf"]'))).click()

# Inputs random CPF (Might not be valid)
cpf_input = wait.until(EC.element_to_be_clickable
                       ((By.XPATH, '/html/body/div[1]/div/div/form/div[1]/div[2]/div[2]/div/input')))
cpf = gera_cpf()
cpf_input.send_keys(cpf)

# Inputs email
email = input("Type the client's email: ")
email_input = wait.until(EC.element_to_be_clickable
                         ((By.XPATH, '/html/body/div[1]/div/div/form/div[1]/div[3]/div[1]/div/input'))).send_keys(email)

# Inputs phone number
phone = input("Type the client's phone number (numbers only): ")
phone_input = wait.until(EC.element_to_be_clickable
                         ((By.XPATH, '/html/body/div[1]/div/div/form/div[1]/div[3]/div[2]/div/input'))).send_keys(phone)

# Inputs CEP
cep = input("Type the client's CEP (numbers only): ")
cep_input = wait.until(EC.element_to_be_clickable
                       ((By.XPATH, '/html/body/div[1]/div/div/form/div[1]/div[4]/div/div/input'))).send_keys(cep)

# Inputs complement
complemento = input("Type the client's adress coplement: ")
complement_input = wait.until(EC.element_to_be_clickable
                              ((By.XPATH, '/html/body/div[1]/div/div/form/div[1]/div[6]/div[2]/div/input'))).send_keys(complemento)

# Inputs password
password_input = wait.until(EC.element_to_be_clickable
                            ((By.XPATH, '/html/body/div[1]/div/div/form/div[1]/div[9]/div/div/input'))).send_keys(senha)

# Inputs password confirmation
conf_password_input = wait.until(EC.element_to_be_clickable
                                 ((By.XPATH, '/html/body/div[1]/div/div/form/div[1]/div[10]/div/div/input'))).send_keys(senha)

# Inputs contract file
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('enter')
time.sleep(2)
pyautogui.write(document_path)
time.sleep(1.4)
pyautogui.press('enter')
    
# Inputs random installment value
installment_input = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/form/div[1]/div[13]/div/div/input')))
installment = gera_parcela()
installment_str = str(installment)
# Send the installment value to the input field
installment_input.send_keys(installment_str)

# Inputs the installment quantity on the drop-down
parcela = input("Type the number of installments (1-12): ")
pyautogui.press('tab')
pyautogui.write(parcela)
qnt_option = wait.until(EC.element_to_be_clickable
                        ((By.XPATH, f"//div[contains(text(), '{parcela}')]"))).click()

# Inputs the installment date
data = input("Type the client's contract date (numbers only): ")
date_input = wait.until(EC.element_to_be_clickable
                        ((By.XPATH, '/html/body/div[1]/div/div/form/div[1]/div[15]/div[1]/div/input'))).send_keys(data)

# Inputs random rimender
reminder_input = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/form/div[1]/div[15]/div[2]/div/input')))
reminder = gera_aviso()
reminder_str = str(reminder)
reminder_input.send_keys(reminder_str)

# Inputs number
numero = input("Type the client's adress number: ")
adressNum_input = wait.until(EC.element_to_be_clickable
                             ((By.XPATH, '/html/body/div[1]/div/div/form/div[1]/div[6]/div[1]/div/input'))).send_keys(numero)

# Clicks at the save button
done_btn = wait.until(EC.element_to_be_clickable
                      ((By.XPATH, '/html/body/div[1]/div/div/form/div[2]/button'))).click() 

# Clicks at the close button
close_btn = wait.until(EC.element_to_be_clickable
                       ((By.XPATH, '/html/body/div[1]/form/button'))).click()

time.sleep(101010)

# Close the browser
driver.quit()
