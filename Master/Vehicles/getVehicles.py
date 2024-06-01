import requests
from bs4 import BeautifulSoup
import pandas as pd
import os

# Ask the user for car manufacturers (separated by commas)
manufacturers = input("Please enter car manufacturers (separated by commas): ").split(',')

# Initialize an empty dictionary to store data for each manufacturer
manufacturer_data = {}

# Iterate over each manufacturer
for manufacturer in manufacturers:
    # Create the URL for the Wikipedia category page
    url = f"https://pt.wikipedia.org/wiki/Categoria:Ve%C3%ADculos_da_{manufacturer.strip()}"
    
    # Send a GET request to the URL
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find all list items within elements with the class 'mw-category-group'
        category_groups = soup.select('.mw-category-group ul li a')
        
        # Initialize an empty list to store the items
        items = []
        
        # Iterate over each link and append its text to the items list
        for link in category_groups:
            items.append(link.text)
        
        # Add the items list to the dictionary with the manufacturer as the key
        manufacturer_data[manufacturer.strip()] = items
        
    else:
        print(f"Failed to retrieve the page for {manufacturer}. Status code: {response.status_code}")

# Convert the dictionary to a DataFrame
df = pd.DataFrame({k: pd.Series(v) for k, v in manufacturer_data.items()})

# Rename all columns to "serie"
df.columns = ['serie'] * len(df.columns)

# Specify the folder path and filename
folder_path = r"C:\Users\josef\Desktop\After life, death\SINP\autoSINP\Files\Excel"
file_name = os.path.join(folder_path, f'{manufacturer}.xlsx')

# Writing the DataFrame to an Excel file
df.to_excel(file_name, index=False)

print(f"Excel file '{file_name}' created successfully with data for the specified manufacturers.")
