import bs4
import urllib.request
import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup as soup
import csv

filename = 'PLACEMENT.csv'
f = open(filename,mode='w',encoding='utf8',newline = '')
file = csv.writer(f)
url='https://www.bppimt.ac.in/training_placement?val=PlacementDetails#PlacementDetails'
page = requests.get(url)
htmlcontent = page.content
bsobj = soup(htmlcontent,"html.parser")
# html = urlopen('https://www.bppimt.ac.in/training_placement?val=PlacementDetails#PlacementDetails')
# bsobj = soup(html.read())
tbody = bsobj('table',{'class':'table table-bordered center-block'})[0].findAll('tr')
xl = []
for row in tbody:
    cols = row.findChildren(recursive = False)
    cols = [element.text for element in cols]
    file.writerow(cols) #Writing to CSV
    xl.append(cols)
# import pandas as pd
# df = pd.DataFrame(data = xl[1:],columns = xl[0])
# df.to_excel('NEW_PLACEMENT.xlsx', index=False,header = False)#Writing to Excel file

# with open(filename,mode='w',encoding='utf8',newline='')as f:
#   file = csv.writer(f)
#   html = urlopen('https://www.bppimt.ac.in/training_placement?val=PlacementDetails#PlacementDetails')
#   bsobj = soup(html.read())
#   tbody = bsobj('table',{'class':'table table-bordered center-block'})[0].findAll('tr')
#   xl = []
#   for row in tbody:
#     cols = row.findChildren(recursive = False)
#     cols = [element.text for element in cols]
#     file.writerow(cols) #Writing to CSV
#     xl.append(cols)
#   import pandas as pd
#   # df = pd.DataFrame(data = xl[1:],columns = xl[0])
#   # df.to_excel('NEW_PLACEMENT.xlsx', index=False,header = False)#Writing to Excel file