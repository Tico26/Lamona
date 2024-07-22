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
    
    # remove all unnecessary elements
    products = soup.find_all('div',class_="prod col-6 col-xl-3")
    for script in soup("script"):
        script.decompose()

    for noscript in soup("noscript"):
        noscript.decompose()

    for style in soup("style"):
        style.decompose()

    for svg in soup("svg"):
        svg.decompose()

    for meta in soup("meta"):
        meta.decompose() 

    for tags in products:
        tags.decompose()

    children = soup.findChildren()
    dataTags = []
    counter = 0
    for child in children:
        counter+=1
        dataTags.append(child)
    # Extract product details
        
else:
    print(f"Failed to retrieve content from {url}")



newCounter=0
for addTags in dataTags:
    newCounter+=1
   
    if newCounter > 1139 and newCounter < 1241:
        file = open("NonProducts/rollerChildren"+str(newCounter)+".txt","w")
        file.write(str(addTags))
        file.close()


print(newCounter)

