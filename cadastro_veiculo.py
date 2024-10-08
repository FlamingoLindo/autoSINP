import customtkinter as tk
from tkinter import simpledialog
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import pandas as pd
import time
import pyautogui
load_dotenv()

df = pd.read_excel(r'C:\Users\josef\Desktop\AfterLifeDeath\SINP\autoSINP\Planilha_SINP.xlsx')

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
    print(df)
    
    content = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.louaoe')
                                                            )
                                ).click() 

    veiculos = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id=":re:"]/li[12]/a')
                                                        )
                            ).click() 
        
    time.sleep(1)
    
    for index, row in df.iterrows():
        marca = row['MARCA']
        ano = row['ANO']
        serie = row['SÉRIE']
        comb = row['COMBUSTÍVEL']
        modelo = row['MODELO DO VEÍCULO']
        tipo = row['TIPO DE VEÍCULO']
        
        print(marca, ano, serie, comb, modelo, tipo)
        
        if pd.isna(modelo) or pd.isna(ano) or pd.isna(serie) or pd.isna(comb) or pd.isna(tipo):
            print("terminou!!!!!!!!!!!!!!!!!!!")
            break
        
        add = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="main-content"]/div[1]/div/div[2]/a')
                                                            )
                                ).click() 
        
        brand = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="brand"]')
                                                            )
                                ).send_keys(row['MARCA'])  
        
        year = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="year"]')
                                                            )
                                ).send_keys(row['ANO']) 
        
        series = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="series"]')
                                                            )
                                ).send_keys(row['SÉRIE'])
                    
        status = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="status"]/span[1]/span/span')
                                                            )
                                )
        status.click()
        pyautogui.press('down')
        pyautogui.press('enter')
                    
        fuel = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="fuel"]')
                                                            )
                                )
        fuel.click()
        fuel.send_keys(row['COMBUSTÍVEL'])
        down_enter()
        
        model = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="vehicle_model"]')
                                                            )
                                )
        model.click()
        model.send_keys(row['MODELO DO VEÍCULO'])
        down_enter()
        
        type = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="vehicle_type"]')
                                                            )
                                )
        type.click()
        type.send_keys(row['TIPO DE VEÍCULO'])
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
        
        time.sleep(0.6)
        
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
