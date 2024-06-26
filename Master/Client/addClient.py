import pyautogui
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import random
import time
import customtkinter as ctk
from dotenv import load_dotenv
import os

load_dotenv()

senha = 12345678

document_path = r"C:\Users\josef\Desktop\AfterLifeDeath\SINP\autoSINP-main\Files\Random\1.pdf"

def get_user_input(prompt):
    def on_submit():
        nonlocal user_input
        user_input = entry.get()
        root.destroy()

    user_input = ""
    root = ctk.CTk()
    root.title("Input Required")

    label = ctk.CTkLabel(root, text=prompt, pady=10)
    label.pack(fill='x')

    entry = ctk.CTkEntry(root)
    entry.pack(fill='x', padx=20, pady=10)

    submit_button = ctk.CTkButton(root, text="Submit", command=on_submit)
    submit_button.pack(pady=20)

    root.mainloop()
    return user_input

def gera_cpf():
    cpf = [random.randint(0, 9) for _ in range(9)]
    soma = sum(x * y for x, y in zip(cpf, range(10, 1, -1)))
    cpf.append((soma * 10) % 11)
    soma = sum(x * y for x, y in zip(cpf, range(11, 1, -1)))
    cpf.append((soma * 10) % 11)
    cpf_formatado = ''.join(map(str, cpf))
    return cpf_formatado[:3] + '.' + cpf_formatado[3:6] + '.' + cpf_formatado[6:9] + '-' + cpf_formatado[9:]

def gera_parcela():
    return str(random.randint(1, 999999999))

def gera_aviso():
    return str(random.randint(1, 29))

driver_path = './chromedriver.exe'
s = Service(driver_path)
driver = webdriver.Chrome(service=s)  

driver.get(os.getenv('SINP_URL'))

wait = WebDriverWait(driver, 5)

email = get_user_input("Type the client's email:")
email_input = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[2]/form/div/div[1]/div/input'))).send_keys(email)

password = get_user_input("Type the client's password:")
password_input = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[2]/form/div/div[2]/div/input'))).send_keys(password)

login_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[2]/form/button'))).click()

time.sleep(1)

register_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/button'))).click()

name = get_user_input("Type the client's name:")
name_input = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/form/div[1]/div[1]/div/div/input'))).send_keys(name)

cpf_radio = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="cpf"]'))).click()
cpf_input = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/form/div[1]/div[2]/div[2]/div/input')))
cpf = gera_cpf()
cpf_input.send_keys(cpf)

phone = get_user_input("Type the client's phone number (numbers only):")
phone_input = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/form/div[1]/div[3]/div[2]/div/input'))).send_keys(phone)

cep = get_user_input("Type the client's CEP (numbers only):")
cep_input = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/form/div[1]/div[4]/div/div/input'))).send_keys(cep)

complemento = get_user_input("Type the client's address complement:")
complement_input = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/form/div[1]/div[6]/div[2]/div/input'))).send_keys(complemento)

password_input = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/form/div[1]/div[9]/div/div/input'))).send_keys(senha)

conf_password_input = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/form/div[1]/div[10]/div/div/input'))).send_keys(senha)

print("You will have to alt tab now")
time.sleep(1.5)
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('enter')
time.sleep(2)
pyautogui.write(document_path)
time.sleep(1.4)
pyautogui.press('enter')

installment_input = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/form/div[1]/div[13]/div/div/input')))
installment = gera_parcela()
installment_str = str(installment)
installment_input.send_keys(installment_str)

parcela = get_user_input("Type the number of installments (1-12):")
time.sleep(1)
pyautogui.press('tab')
pyautogui.write(parcela)
qnt_option = wait.until(EC.element_to_be_clickable((By.XPATH, f"//div[contains(text(), '{parcela}')]"))).click()

data = get_user_input("Type the client's contract date (numbers only):")
date_input = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/form/div[1]/div[15]/div[1]/div/input'))).send_keys(data)

reminder_input = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/form/div[1]/div[15]/div[2]/div/input')))
reminder = gera_aviso()
reminder_str = str(reminder)
reminder_input.send_keys(reminder_str)

numero = get_user_input("Type the client's address number:")
adressNum_input = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/form/div[1]/div[6]/div[1]/div/input'))).send_keys(numero)

done_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/form/div[2]/button'))).click() 

close_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/form/button'))).click()

time.sleep(101010
)

# Close the browser
driver.quit()
