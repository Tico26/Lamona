import requests
from bs4 import BeautifulSoup
import re


url = "https://www.skates.co.uk/collections/scooters?page=4"

# Send a GET request to the website
response = requests.get(url)
labeled_data = []
# Check if the request was successful
if response.status_code == 200:
    html_content = response.text
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Find all product containers
    products = soup.find_all('li', class_='grid__item')
    counter =132    
    # Extract product details
    for product in products:
        counter+=1
        try:
            name = product.find('h3', class_="card__heading h5").text
        except:
            continue
        try:
            price = product.find('span', class_="price-item price-item--regular").text
        except:
            continue
        #image = product.find('img', class_='imgprd')
        #productPage = product.find('a', attrs={"class": None})
        productJSON = {"html":str(product), "name":name,"price":price}
        #labeled_data.append(productJSON)
        print(name)
        print(price)
        labeled_data.append(productJSON)
        file = open("Products/skateScooters"+str(counter)+".txt","w")
        file.write(str(productJSON))
        file.close()
        
        
else:
    print(f"Failed to retrieve content from {url}")

print(counter)