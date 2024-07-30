import requests
from bs4 import BeautifulSoup
import csv


tag_data = []
    # remove all unnecessary elements
def get_tags_without_products(soup):
    #remove products from page
    products = soup.find_all('div', class_='prod col-6 col-xl-3')

    divCounter =0
    liCounter =0
    allLI = soup.find_all('li')
    
    allDiv = soup.find_all('div')
    for tags in products:
        tags.decompose()
    '''
    for li in allLI:
        liCounter+=1
        if liCounter >= 386:
            break
        try:
            lis = {'html':str(li),'name':None,'price':None}
            
        except:
            print('error finding li on item: ' + str(liCounter))
            continue
        tag_data.append(lis)
    '''
    for div in allDiv:
        divCounter+=1
        if divCounter >= 386:
            break
        try:    
            divs = {'html':str(div),'name':None,'price':None}
        except:
            print('error finding div on item: ' + str(divCounter))
            continue
        tag_data.append(divs)
    
    '''
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
    '''
    
        
    print(divCounter)
url = "https://www.rollerblade.com/uk/en/all"

    # Send a GET request to the website
saveAs = "rollerblade"
response = requests.get(url)

html_content = response.text
soup = BeautifulSoup(html_content, 'html.parser')

get_tags_without_products(soup)

with open('CSV/Non-Products/'+saveAs+'Div.csv', 'w', newline='') as csvfile:
    fieldnames = ['html', 'name', 'price']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for item in tag_data:
        writer.writerow((item))