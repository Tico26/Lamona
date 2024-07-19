import requests
from bs4 import BeautifulSoup
import re


url = "https://thecabinetshop.co.uk/collections/drawers?page=2"

# Send a GET request to the website
response = requests.get(url)
labeled_data = []
# Check if the request was successful
if response.status_code == 200:
    html_content = response.text
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Find all product containers
    products = soup.find_all('li', class_='grid__item')
    counter = 0
    # Extract product details
    for product in products:
        counter+=1
        name = product.find('h3', class_='card__heading h5')
        price = product.find('span', class_='price-item price-item--regular')
        image = product.find('span', class_='monkuProdImgey')
        productPage = product.find('a', class_='full-unstyled-link')
        productJSON = {"html":product, "name":name,"price":price,"image":image, "productPage":productPage}
        labeled_data.append(productJSON)
        file = open("Products/cabinetshopDrawers"+str(counter)+".txt","w")
        file.write(str(productJSON))
        file.close()

        
        
else:
    print(f"Failed to retrieve content from {url}")



print(len(labeled_data))