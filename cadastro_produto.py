import customtkinter as tk
from tkinter import simpledialog
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pandas as pd
import time
import pyautogui

path = r'C:\Users\josef\Desktop\AfterLifeDeath\SINP\autoSINP\Planilha_SINP.xlsx'
sheet2 = pd.read_excel(path, sheet_name='PRODUTO')
print(sheet2)

def get_user_input(prompt):
    root = tk.CTk()
    root.withdraw()  # Hide the main window

    user_input = simpledialog.askstring("Input", prompt)

    return user_input

def down_enter():
    pyautogui.press('space')
    pyautogui.press('backspace')
    time.sleep(1.3)
    pyautogui.press('down')
    pyautogui.press('enter')

try:
    # Drive stuff
    driver_path = './chromedriver.exe'
    s = Service(driver_path)
    driver = webdriver.Chrome(service=s)  

    driver.get('https://sinp.mestresdaweb.io/admin/auth/login')

    wait = WebDriverWait(driver, 5)
except Exception as e:
    print('There has been an error initialising the chrome driver')
    print(e)

try:
    login = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.ibGNzh')
                                                        )
                            ).send_keys('fabio@mestresdaweb.com.br') 
    
    senha = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.eLaMyQ')
                                                        )
                            ).send_keys('Fcodo1505$') 
    
    login = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="main-content"]/div[1]/form/div/button')
                                                        )
                            ).click() 
except Exception as e:
    print('There has been an error on the login')
    print(e)

try:
    content = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.louaoe')
                                                            )
                                ).click() 

    produto = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id=":re:"]/li[6]/a')
                                                        )
                             ).click() 
        
    time.sleep(1)
    
    for index, row in sheet2.iterrows():
        nome = row['NOME']
        prod_e = row['PRODUTO É ']
        valor = row['VALOR']
        desc = row['DESCRIÇÃO DO PRODUTO']
        modelo = row['MODELO DE VEÍCULO']
        
        print(nome, prod_e, valor, desc, modelo)
        
        if pd.isna(nome) or pd.isna(prod_e) or pd.isna(valor) or pd.isna(desc) or pd.isna(modelo):
            print("terminou!!!!!!!!!!!!!!!!!!!")
            break
        
        add = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="main-content"]/div[1]/div/div[2]/a')
                                                            )
                                ).click() 
        
        name = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="name"]')
                                                            )
                                ).send_keys(nome)

        product_is = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="productIs"]/span[1]/span/span')
                                                            )
                                ).click()
        
        if prod_e == "fabricante/original":
            pyautogui.press('down')
            pyautogui.press('enter')
        else:
            pyautogui.press('down')
            pyautogui.press('down')
            pyautogui.press('enter')

        value = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="value"]')
                                                            )
                                ).send_keys(valor)    

        description = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="description"]')
                                                            )
                                ).send_keys(desc) 

        status = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="status"]/span[1]/span/span')
                                                            )
                                )
        status.click()
        pyautogui.press('down')
        pyautogui.press('enter')

        model = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="vehicle_models"]')
                                                            )
                                ).send_keys(modelo) 
        
        down_enter()

        client = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="client"]')
                                                            )
                                )
        client.click()
        client.send_keys('Alain Prost')
        down_enter()
        
        save = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="main-content"]/div[1]/div/div[2]/div[2]/button[2]')
                                                            )
                                ).click() 
        
        close = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id='strapi']/div/div/button")
                                                            )
                                ).click()
        
        publish = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="main-content"]/div[1]/div/div[2]/div[2]/button')
                                                            )
                                ).click()
        
        
        go_back = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="main-content"]/div[1]/div/div[1]/a')
                                                            )
                                ).click()
except Exception as e:
    print('There has been an error opening the profile options')
    print(e)
      
   
get_user_input("DONE")
# Close the browser
driver.quit()
