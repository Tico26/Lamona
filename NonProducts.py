import requests
from bs4 import BeautifulSoup
import csv


tag_data = []
    # remove all unnecessary elements
def get_tags_without_products(soup):
    #remove products from page
    products = soup.find_all('div',class_="product-block layout-align-above flex column max-cols-4 min-cols-2 product-block--gutter-0 product-block--gap-20 product-block--border-true product-block--no-quickbuy")
    for tags in products:
        tags.decompose()

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
    
    children = soup.findChildren()
    counter =0
    for child in children:
        counter+=1
        if counter >= 904 and counter <=1084:
            childJSON = {'html':child,'name':None,'price':None}
            tag_data.append(childJSON)
        
    print(counter)
url = "https://missdiva.co.uk/collections/heels"

    # Send a GET request to the website
saveAs = "missdiva"
response = requests.get(url)

html_content = response.text
soup = BeautifulSoup(html_content, 'html.parser')

get_tags_without_products(soup)

with open('CSV/Non-Products/'+saveAs+'Children.csv', 'w', newline='') as csvfile:
    fieldnames = ['html', 'name', 'price']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for item in tag_data:
        writer.writerow((item))