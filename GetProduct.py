import requests
from bs4 import BeautifulSoup
import re


url = "https://portopets.co.uk/collections/cats?page=9"

# Send a GET request to the website
response = requests.get(url)
labeled_data = []
# Check if the request was successful
if response.status_code == 200:
    html_content = response.text
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Find all product containers
    products = soup.find_all('div', class_='col-md-3 col-sm-6 col-xs-6 element mb30')
    counter =160    
    # Extract product details
    for product in products:
        counter+=1
        name = product.find('h5', attrs={"class": None}).text
        
        try:
            price = product.find('span', class_="money").text
        except:
            continue
        #image = product.find('img', class_='imgprd')
        #productPage = product.find('a', attrs={"class": None})
        productJSON = {"html":str(product), "name":name,"price":price}
        #labeled_data.append(productJSON)
        print(name)
        print(price)
        
        file = open("Products/portoTrial"+str(counter)+".txt","w")
        file.write(str(productJSON))
        file.close()
        labeled_data.append(productJSON)
        
        
else:
    print(f"Failed to retrieve content from {url}")



print(counter)