#!/usr/bin/env python
# coding: utf-8

# # Web Scraping:
# 1. Import the libraries and classes:
#     - urllib request.
#     - BeautifulSoup.
# 2. Steps:
# 
# 
#     a. html upload.
#     b. html parser.
#     c. Extraction of data from web page.
#     d. Transformation into required file: csv.

# In[1]:


# Import useful libraries and classes.
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup


# In[2]:


#html upload
my_url=  "http://www.imdb.com/search/title?sort=num_votes,desc&start=1&title_type=feature&year=1950,2012"
uClient= uReq(my_url)
page_html= uClient.read()
uClient.close()


# In[3]:


page_html


# In[4]:


#html parser
page_soup= soup(page_html)
page_soup


# In[5]:


#read class from web page.
containers= page_soup.findAll("div", {"class": "lister-item mode-advanced"})
print(len(containers))


# In[6]:


print(containers)


# In[13]:


filename= "imdb_m.csv"
f= open(filename, "w")

headers= "Name, Year, Runtime \n"
f.write(headers)

for container in containers:
    name= container.img["alt"]
    year_mov= container.findAll("span", {"class": "lister-item-year"})
    year=year_mov[0].text
    runtime_mov= container.findAll("span", {"class": "runtime"})
    runtime=runtime_mov[0].text
    
    print(name + "," + year + "," + runtime +  "\n")
    f.write(name + "," + year + "," + runtime  + "\n")
    
f.close()


# In[11]:


import pandas as pd


# In[15]:


pd.read_csv('imdb_m.csv',encoding='latin1')


# In[ ]:





# In[ ]:




