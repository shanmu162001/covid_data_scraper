#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install pymysql


# In[12]:


import pymysql
import requests
from bs4 import BeautifulSoup as bs
from win10toast import ToastNotifier

#database connection
connection = pymysql.connect(host="localhost", user="root", password="", database="covid")


def update(country):
    header={'User-Agent':'Mozilla'}
    req=requests.get('https://www.worldometers.info/coronavirus/country/'+country+'/',headers=header) 
    html=req.text
    s=bs(html,'lxml')
    total_cases=s.find_all('div',{'class':'maincounter-number'})[0].span.text
    total_deaths=s.find_all('div',{'class':'maincounter-number'})[1].span.text
    total_recovery=s.find_all('div',{'class':'maincounter-number'})[2].span.text
    
    # inserting into database
    sql = "INSERT INTO details (country,death,recover,tcases) VALUES (%s, %s,%s,%s)"
    val = (country,total_deaths,total_recovery,total_cases)
    mycursor=connection.cursor()
    mycursor.execute(sql,val)
    connection.commit()
    connection.close()
    
    # desktop notification
    notifier=ToastNotifier()
    message='Total Cases:'+total_cases+'\nTotal Deaths:'+total_deaths+'\nTotal Recoveries:'+total_recovery
    notifi=notifier.show_toast(title='COVID '+country+' Update:',msg=message,duration=5,icon_path=r"C:\Users\DELL\covid.ico")
    return notifi

### main function  ###

#countries=['us','india','china','brazil','france','italy','japan','uk','germany','spain','iran','canada','singapore']
country=input("Input the country for notification : ")
update(country)


# In[ ]:





# In[ ]:





# In[ ]:




