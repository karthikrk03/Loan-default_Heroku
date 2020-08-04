#!/usr/bin/env python
# coding: utf-8

# In[2]:


import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'ApprovalFY':1997, 'Term':120, 'DisbursementGross':60000})

print(r.json())


# In[ ]:




