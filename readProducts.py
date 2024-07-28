import requests
from bs4 import BeautifulSoup
import csv



# Send a GET request to the website
#products = soup.find_all('div',class_="prod col-6 col-xl-3")
#for tags in products:
 #       tags.decompose()
#children = soup.findChildren()
labeled_data = []
def remove_unnecessary_element(soup):
    # remove all unnecessary elements
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

def extract_product_details():
    try:
         products = soup.find_all('div', class_='product-block layout-align-above flex column max-cols-4 min-cols-2 product-block--gutter-0 product-block--gap-20 product-block--border-true product-block--no-quickbuy')
    except:
        print('error finding products')
    counter =0  
    # Extract product details
    for product in products:
        counter+=1
        try:
            name = product.find('div', class_="product-block__title-price").text
            
        except:
            print('error finding name on item ' + str(counter))
            continue
        try:
            price = product.find('span', class_="money").text
        except:
            print('error finding price on item: ' + str(counter))
            continue
        
        productJSON = {"html":product, "name":name.strip(),"price":price.strip()}
        
        labeled_data.append(productJSON)


pageNum=0
# Check if the request was successful
saveAs = "missdivaHeels"

for items in range(6):
    pageNum+=1
    url = "https://missdiva.co.uk/collections/heels"+"?page="+str(pageNum)

    # Send a GET request to the website
    response = requests.get(url)

    html_content = response.text
    soup = BeautifulSoup(html_content, 'html.parser')
    remove_unnecessary_element(soup)
    extract_product_details()
print("Number of items found: "+ str(len(labeled_data)))



with open('CSV/'+saveAs+'.csv', 'w', newline='') as csvfile:
    fieldnames = ['html', 'name', 'price']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for item in labeled_data:
        writer.writerow(item)


