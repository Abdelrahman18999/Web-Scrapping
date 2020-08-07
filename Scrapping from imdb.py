#!/usr/bin/env python
# coding: utf-8

# # Scrapping from imdb.com

# In[11]:


#import the libraries that you need
from bs4 import BeautifulSoup
import requests


# In[12]:


#prepare URL that you want to scrap from it
url = 'https://www.imdb.com/find?'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'}


# In[13]:


#Create your query to find the results that you want
MovieName = input('Enter Movie Name: ')
query = {'q':MovieName , 'ref_' :'nv_sr_sm'}


# In[ ]:


s = requests.Session()
s.headers.update(headers)
r = s.get(url, params=query)


# In[14]:


soup = BeautifulSoup(r.content, 'lxml')


# In[15]:


for titles in soup.findAll('div', {'class':'findSection'}):
    for header in titles.findAll('h3', {'class':'findSectionHeader'}):
        if header.text == 'Titles':
            for name in titles.findAll('table', {'class':'findList'}):
                print(name.text)

