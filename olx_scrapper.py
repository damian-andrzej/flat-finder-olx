
from selenium.webdriver.common.by import By
from selenium import webdriver
import time
from bs4 import BeautifulSoup
from requests import get
from selenium.webdriver.common.keys import Keys

URL='https://www.olx.pl/nieruchomosci/mieszkania/wynajem/wroclaw/?search%5Bfilter_enum_rooms%5D%5B0%5D=three&search%5Bdistrict_id%5D=387'
offers_titles = []
offers_prices = []
offers_links = []
page = get(URL)
bs = BeautifulSoup(page.content)
titles = bs.find_all(name="a", class_='marginright5')
price = bs.find_all(name="p", class_='price')
links = bs.find_all(name="a", class_='marginright') #something wrong
#looping titles and adding to list
for title in titles:
    offer = (title.text).strip()
    #print(title['href'])
    #takes hyperlinks to offers
    offers_links.append(title['href'])
    #insert records one by one to our list
    offers_titles.append(offer)

# looping prices and adding to list
for p in price:
    #print(p.text)
    becel = (p.text).strip()
    offers_prices.append(becel)
#display flat title, price and link to the offer
for x in range(len(offers_titles)):
    print(offers_titles[x])
    print(offers_prices[x])
    print(offers_links[x])



