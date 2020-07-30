#!/usr/bin/env python
# coding: utf-8

# In[4]:


from requests_html import HTMLSession
import pandas as pd

def get_results():
    return _raw_get_info1("https://tradingeconomics.com/country-list/capital-flows?continent=g20")

def _raw_get_info1(site):
    session = HTMLSession()
    resp = session.get(site)
    tables = pd.read_html(resp.html.raw_html)  
    df = tables[0].copy()
    df.columns = tables[0].columns  
    session.close()    
    return df

df3=get_results()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




