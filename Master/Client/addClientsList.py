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

# Load the Excel file
df = pd.read_excel('C:/Users/josef/Desktop/After life, death/SINP/autoSINP/Files/Excel/clienteSINP.xlsx')
print(df)

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

# Wait for email input to be clickable
email_input = wait.until(EC.element_to_be_clickable
                         ((By.XPATH, '/html/body/div[1]/div[2]/form/div/div[1]/div/input'))).send_keys(os.getenv('SINP_LOGIN'))

# Wait for password input to be clickable
password_input = wait.until(EC.element_to_be_clickable
                            ((By.XPATH, '/html/body/div[1]/div[2]/form/div/div[2]/div/input'))).send_keys(os.getenv('SINP_PASSWORD'))

# Click on login button
login_btn = wait.until(EC.element_to_be_clickable
                       ((By.XPATH, '/html/body/div[1]/div[2]/form/button'))).send_keys(os.getenv('SINP_PASSWORD'))


# Initialize the notification ID
notification_id = 1
for index, row in df.iterrows():

    # Show what index its currently inputing (Just for debuging)
    print(index)
    
    # Clicks at the register a client page
    register_btn = wait.until(EC.element_to_be_clickable
                              ((By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/button'))).click()
    
    # Inputs name
    name_input = wait.until(EC.element_to_be_clickable
                            ((By.XPATH, '/html/body/div[1]/div/div/form/div[1]/div[1]/div/div/input'))).send_keys(row['nomeCompleto'])
    
    # Click at the CPF radial button
    cpf_radio = wait.until(EC.element_to_be_clickable
                           ((By.XPATH, '//*[@id="cpf"]'))).click()

    # Inputs random CPF (Might not be valid)
    cpf_input = wait.until(EC.element_to_be_clickable
                           ((By.XPATH, '/html/body/div[1]/div/div/form/div[1]/div[2]/div[2]/div/input')))
    cpf = gera_cpf()
    cpf_input.send_keys(cpf)

    # Inputs email
    email_input = wait.until(EC.element_to_be_clickable
                             ((By.XPATH, '/html/body/div[1]/div/div/form/div[1]/div[3]/div[1]/div/input'))).send_keys(row['email'])

    # Inputs phone number
    phone_input = wait.until(EC.element_to_be_clickable
                             ((By.XPATH, '/html/body/div[1]/div/div/form/div[1]/div[3]/div[2]/div/input'))).send_keys(row['telefone'])

    # Inputs CEP
    cep_input = wait.until(EC.element_to_be_clickable
                           ((By.XPATH, '/html/body/div[1]/div/div/form/div[1]/div[4]/div/div/input'))).send_keys(row['cep'])

    # Inputs street
    street_input = wait.until(EC.element_to_be_clickable
                              ((By.XPATH, '/html/body/div[1]/div/div/form/div[1]/div[5]/div/div/input'))).send_keys(row['rua'])
    
    # Inputs number
    street_input = wait.until(EC.element_to_be_clickable
                              ((By.XPATH, '/html/body/div[1]/div/div/form/div[1]/div[6]/div[1]/div/input'))).send_keys(row['numero'])
    
    # Inputs complement
    complement_input = wait.until(EC.element_to_be_clickable
                                  ((By.XPATH, '/html/body/div[1]/div/div/form/div[1]/div[6]/div[2]/div/input'))).send_keys(row['complemento'])

    # Inputs neighborhood
    neighborhood_input = wait.until(EC.element_to_be_clickable
                                    ((By.XPATH, '/html/body/div[1]/div/div/form/div[1]/div[7]/div[1]/div/input'))).send_keys(row['bairro'])

    # Inputs city
    city_input = wait.until(EC.element_to_be_clickable
                            ((By.XPATH, '/html/body/div[1]/div/div/form/div[1]/div[7]/div[2]/div/input'))).send_keys(row['cidade'])

    # Inputs estate
    estate_input = wait.until(EC.element_to_be_clickable
                              ((By.XPATH, '/html/body/div[1]/div/div/form/div[1]/div[8]/div/div/input'))).send_keys(row['estado'])

    # Inputs password
    password_input = wait.until(EC.element_to_be_clickable
                                ((By.XPATH, '/html/body/div[1]/div/div/form/div[1]/div[9]/div/div/input'))).send_keys(row['senha'])

    # Inputs password confirmation
    conf_password_input = wait.until(EC.element_to_be_clickable
                                     ((By.XPATH, '/html/body/div[1]/div/div/form/div[1]/div[10]/div/div/input'))).send_keys(row['confSenha'])

    # Inputs contract file
    #file_input = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/form/div[1]/div[12]/div/div/button/svg')))
    #file_path = contract_file
    #file_input.send_keys(file_path)
    time.sleep(5)
    
    # Inputs random installment value
    installment_input = wait.until(EC.element_to_be_clickable
                                   ((By.XPATH, '/html/body/div[1]/div/div/form/div[1]/div[13]/div/div/input')))
    installment = gera_parcela()
    installment_str = str(installment)
    # Send the installment value to the input field
    installment_input.send_keys(installment_str)

    # Inputs the installment quantity on the drop-down
    installment_qnt_dropdown = wait.until(EC.element_to_be_clickable
                                          ((By.XPATH, '/html/body/div[1]/div/div/form/div[1]/div[14]/div[1]/div/div/div'))).click()
    qnt_option = wait.until(EC.element_to_be_clickable
                            ((By.XPATH, f"//div[contains(text(), '{row['parcela']}')]"))).click()

    # Inputs the installment date
    date_str = row['dataParcela'].strftime('%d/%m/%Y')
    date_input = wait.until(EC.element_to_be_clickable
                            ((By.XPATH, '/html/body/div[1]/div/div/form/div[1]/div[15]/div[1]/div/input')))
    date_input.send_keys(date_str)

    # Inputs random rimender
    reminder_input = wait.until(EC.element_to_be_clickable
                                ((By.XPATH, '/html/body/div[1]/div/div/form/div[1]/div[15]/div[2]/div/input')))
    reminder = gera_aviso()
    reminder_str = str(reminder)
    reminder_input.send_keys(reminder_str)

    # Clicks at the save button
    done_btn = wait.until(EC.element_to_be_clickable
                          ((By.XPATH, '/html/body/div[1]/div/div/form/div[2]/button'))).click()

    # Clicks at the close button
    close_btn = wait.until(EC.element_to_be_clickable
                           ((By.XPATH, '/html/body/div[1]/form/button'))).click()
    
    # Close the button with dynamically changing ID
    close_notify_btn_xpath = f'//*[@id="{notification_id}"]'
    close_notify_btn = wait.until(EC.element_to_be_clickable
                                  ((By.XPATH, close_notify_btn_xpath))).click()

    # Increment the ID for the next iteration
    notification_id += 1
    

# Close the browser
driver.quit()
