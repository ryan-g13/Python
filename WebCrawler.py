import requests
from bs4 import BeautifulSoup

'''creating a spider to crawl upon the interwebs'''

def trade_spider(max_pages):

    page = 1

    while page <= max_pages:

        #Url that you are targeting minus the pagination using variable to control this
        url = 'https://www.ebay.com/sch/Cars-Trucks/6001/i.html?_nkw=chevrolet%20corvette&_sacat=6001&_frs=' + str(page)
        source_data = requests.get(url) #saves html source data from URL in variable
        simple_text = source_data.text  #converts to new text format
        soup_object = BeautifulSoup(simple_text) #uses beautiful soup to convert?
        for link in soup_object.findAll('a', {'class': 'vip'}):     #finding all of links in doc that are under the class "vip"
            href = link.get('href')     #get the clickable link out
            print(href)                 #return the clickable link verify if working
        page += 1

'''Calling the method - current use of first page only numerous entries per page'''
trade_spider(1)