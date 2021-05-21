#!/usr/bin/env python
# coding: utf-8

# In[18]:


import requests
from bs4 import BeautifulSoup as bs
from win10toast import ToastNotifier
import pandas as pd

def update(country):
    header={'User-Agent':'Mozilla'}
    req=requests.get('https://www.worldometers.info/coronavirus/country/'+country+'/',headers=header) 
    html=req.text
    s=bs(html,'lxml')
    total_cases=s.find_all('div',{'class':'maincounter-number'})[0].span.text
    total_deaths=s.find_all('div',{'class':'maincounter-number'})[1].span.text
    total_recovery=s.find_all('div',{'class':'maincounter-number'})[2].span.text
    
    # writing in csv file
    data=[]
    data.append(total_cases)
    data.append(total_deaths)
    data.append(total_recovery)
    data.append(country)
    notifier=ToastNotifier()
    df = pd.DataFrame({'CoronaData': data})
    df.index = ['TotalCases', 'Deaths', 'Recovered','Country']
    df.to_csv('Covid_Data.csv')
    
    # desktop notification
    message='Total Cases:'+total_cases+'\nTotal Deaths:'+total_deaths+'\nTotal Recoveries:'+total_recovery
    notifi=notifier.show_toast(title='COVID '+country+' Update:',msg=message,duration=5,icon_path=r"C:\Users\DELL\covid.ico")
    return notifi



### main function  ###

#countries=['us','india','china','brazil','france','italy','japan','uk','germany','spain','iran','canada','singapore']
country=input("Input the country for notification : ")
print(update(country))


# In[ ]:




