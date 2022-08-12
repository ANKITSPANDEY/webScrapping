import requests
from bs4 import BeautifulSoup as bs
import csv

url="https://www.weather-forecast.com/locations/KolKata/forecasts/latest"
r=requests.get(url)
forecast =bs(r.content,'lxml')

wthr=forecast.findAll('div',{'class':"b-forecast__table-days-name"})
# for i in range(12):
#    print(wthr[i].text)
wthr1=forecast.findAll('div',{'class':"b-forecast__table-days-date"})
#for i in range(12):
    #print(wthr1[i].text)

wthr2=forecast.find("tr",{"class": "b-forecast__table-humidity js-humidity"})
mywthr2=wthr2.findAll("span",{"class":"b-forecast__table-value"})
# for i in range(2,35):
#     print(mywthr2[i].text)

wthr3=forecast.find("tr",{"class": "b-forecast__table-max-temperature js-temp"})
mywthr3=wthr3.findAll("span",{"class":"temp b-forecast__table-value"})
# for i in range(2,35):
#     print(mywthr3[i].text)

wthr4=forecast.find("tr",{"class": "b-forecast__table-min-temperature js-min-temp"})
mywthr4=wthr4.findAll("span",{"class":"temp b-forecast__table-value"})
# for i in range(2,35):
#     print(mywthr4[i].text)


with open("Weather_Forecasting_Report_Of_KOLKATA.csv", mode="w") as csv_file:
    fieldnames=['Days_Name', 'Days_Date','Humidity \n [Am,Pm,Night]','Max_Temp \n [Am,Pm,Night]','Min_Temp \n [Am,Pm,Night]']
    writer=csv.DictWriter(csv_file,fieldnames=fieldnames)
    writer.writeheader()

    for (i,y) in zip(range(12),range(2,35,3)):
        writer.writerow({'Days_Name':str(wthr[i].text),'Days_Date':str(wthr1[i].text),'Humidity \n [Am,Pm,Night]':[str(mywthr2[y].text),str(mywthr2[y+1].text),str(mywthr2[y+2].text)],'Max_Temp \n [Am,Pm,Night]':[str(mywthr3[y].text),str(mywthr3[y+1].text),str(mywthr3[y+2].text)],'Min_Temp \n [Am,Pm,Night]':[str(mywthr4[y].text),str(mywthr4[y+1].text),str(mywthr4[y+2].text)]})
