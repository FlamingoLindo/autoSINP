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
from pynput.keyboard import Key, Controller

load_dotenv()

def gen_price():
    price = random.randint(1, 999999999)
    return price

# Function to upload an image
def upload_image(image_path):
    # Locate and click the hidden file input
    image_input = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="Vector-4"]')))
    image_input.click()
    time.sleep(0.5)
    
    # Type the full path of the file to be uploaded
    pyautogui.write(image_path)
    pyautogui.press('enter')
    time.sleep(1)

# List of image paths to be uploaded
images = [
    r"C:\Users\josef\Desktop\After life, death\SINP\autoSINP-main\Files\Random\capacitor.webp",
    r"C:\Users\josef\Desktop\After life, death\SINP\autoSINP-main\Files\Random\Amortecedor.png",
    r"C:\Users\josef\Desktop\After life, death\SINP\autoSINP-main\Files\Random\cabeca.png",
    r"C:\Users\josef\Desktop\After life, death\SINP\autoSINP-main\Files\Random\filtro.jpg",
    r"C:\Users\josef\Desktop\After life, death\SINP\autoSINP-main\Files\Random\pastilha.webp",
    r"C:\Users\josef\Desktop\After life, death\SINP\autoSINP-main\Files\Random\pneu.webp",
    r"C:\Users\josef\Desktop\After life, death\SINP\autoSINP-main\Files\Random\bateria.webp",
    r"C:\Users\josef\Desktop\After life, death\SINP\autoSINP-main\Files\Random\vela.png",
    r"C:\Users\josef\Desktop\After life, death\SINP\autoSINP-main\Files\Random\Cheirinho.png"
]

# Load the Excel file
df = pd.read_excel('./Files/Excel/Products.xlsx')
print(df)

# Path to your ChromeDriver
driver_path = './chromedriver.exe'
s = Service(driver_path)
driver = webdriver.Chrome(service=s)

# Open the web page
driver.get(os.getenv('SINP_URL'))

# Initialize WebDriverWait
wait = WebDriverWait(driver, 10)

# Wait for email input to be clickable
email_input = wait.until(EC.element_to_be_clickable
                         ((By.XPATH, '/html/body/div[1]/div[2]/form/div/div[1]/div/input'))).send_keys(os.getenv('SINP_LOGIN'))

# Wait for password input to be clickable
password_input = wait.until(EC.element_to_be_clickable
                            ((By.XPATH, '/html/body/div[1]/div[2]/form/div/div[2]/div/input'))).send_keys(os.getenv('SINP_PASSWORD'))

# Click on login button
login_btn = wait.until(EC.element_to_be_clickable
                       ((By.XPATH, '/html/body/div[1]/div[2]/form/button'))).click()

# Click on the products page
products_btn = wait.until(EC.element_to_be_clickable
                          ((By.XPATH, '/html/body/div[1]/div[1]/div[2]/a[4]'))).click()

# Initialize the notification ID
notification_id = 1

# Loop through each image and upload
for image in images:
    # Open the register a client page
    register_btn = wait.until(EC.element_to_be_clickable
                              ((By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/button'))).click()
    
    # Show what image it's currently uploading (Just for debugging)
    print(f"Uploading image {image}")

    time.sleep(1)

    # Uploads the image
    upload_image(image)
    time.sleep(10)
    
    for index, row in df.iterrows():
        # Show what index it's currently inputting (Just for debugging)
        print(f"Processing row {index}")

        time.sleep(1)

        # Inputs the product's name
        name_input = wait.until(EC.element_to_be_clickable
                                ((By.XPATH, '/html/body/div[1]/div/div/form/div[1]/div[3]/div/div/input'))).send_keys(row['name'])

        # Inputs the product's model
        model_dropdown = wait.until(EC.element_to_be_clickable
                                    ((By.XPATH, '/html/body/div[1]/div/div/form/div[1]/div[5]/div/div/div/div/div[1]/div[2]'))).click()
        model_select = wait.until(EC.element_to_be_clickable
                                  ((By.XPATH,"//input[@type='checkbox']"))).click()

        # Inputs the product's type
        type_dropdown = wait.until(EC.element_to_be_clickable
                                   ((By.XPATH, '/html/body/div[1]/div/div/form/div[1]/div[6]/div/div/div/div/div[1]/div[2]'))).click()
        type_select = wait.until(EC.element_to_be_clickable
                                 ((By.XPATH,"//input[@type='checkbox']"))).click() 

        # Inputs product's price
        price_input = wait.until(EC.element_to_be_clickable
                                 ((By.XPATH, '/html/body/div[1]/div/div/form/div[1]/div[7]/div/div/input'))).click()
        price = gen_price()
        price_input.send_keys(str(price))

        # Inputs the product's description
        description_input = wait.until(EC.element_to_be_clickable
                                       ((By.XPATH, '/html/body/div[1]/div/div/form/div[1]/div[8]/div/div/textarea'))).click()
        description_input.send_keys(row['description'])

        # Clicks the save button
        done_btn = wait.until(EC.element_to_be_clickable
                              ((By.XPATH, '/html/body/div[1]/div/div/form/div[2]/button'))).click()

        # Clicks the close button
        close_btn = wait.until(EC.element_to_be_clickable
                               ((By.XPATH, '/html/body/div[1]/form/button'))).click()

        # Close the button with dynamically changing ID
        close_notify_btn_xpath = f'//*[@id="{notification_id}"]'
        close_notify_btn = wait.until(EC.element_to_be_clickable
                                      ((By.XPATH, close_notify_btn_xpath))).click()

        # Increment the ID for the next iteration
        notification_id += 1

        # Open the register form again for the next product
        register_btn = wait.until(EC.element_to_be_clickable
                                  ((By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/button'))).click()
        time.sleep(2)

# Close the browser
driver.quit()
