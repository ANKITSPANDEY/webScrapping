from bs4 import BeautifulSoup
import requests
from csv import writer
import pandas as pd

url="https://www.flipkart.com/search?q=mobiles&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_3_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_3_na_na_na&as-pos=1&as-type=RECENT&suggestionId=mobiles%7CMobiles&requestId=32411e0e-b2b3-412c-8163-57e86b813bdc&as-searchtext=mob"
page = requests.get(url)

htmlcontent = page.content
soup = BeautifulSoup(htmlcontent,"html.parser")

product=soup.find('div',class_='_4rR01T')
with open("mobile.csv",'w',encoding='utf8',newline='')as f:
  thewriter=writer(f)
  header=['Product_name','Price','Rating']
  thewriter.writerow(header)
  for a in soup.findAll('a',class_='_1fQZEK'):
    name=a.find('div',class_='_4rR01T')
    price=a.find('div',class_='_30jeq3 _1_WHN1')
    rating=a.find('div',class_='_3LWZlK')
    info=[name.text,price.text,rating.text]
    thewriter.writerow(info)
