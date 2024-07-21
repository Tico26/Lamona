import requests
from bs4 import BeautifulSoup
import re


url = "https://www.rollerblade.com/uk/en/all"

# Send a GET request to the website
response = requests.get(url)
labeled_data = []
# Check if the request was successful
if response.status_code == 200:
    html_content = response.text
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Find all product containers
    products = soup.find_all('div', class_='prod col-6 col-xl-3')
    counter = 0
    # Extract product details
    for product in products:
        counter+=1
        name = product.find('p', class_='skate-list-name text-uppercase mb-0')
        price = product.find('span', class_='price skates-list-price')
        image = product.find('img', class_='imgprd')
        productPage = product.find('a', attrs={"class": None})
        productJSON = {"html":product, "name":name,"price":price,"image":image, "productPage":productPage}
        labeled_data.append(productJSON)
        file = open("Products/rollerbladeSkates"+str(counter)+".txt","w")
        file.write(str(productJSON))
        file.close()

        
        
else:
    print(f"Failed to retrieve content from {url}")



print(counter)