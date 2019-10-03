#!/usr/bin/env python
# coding: utf-8

# In[7]:


import sys
N = int(input ())
if (N>1000000 and N<1):
    sys.exit()
else:
    if(N % 2)== 0:
        print('Bob')
    else: 
        print('Alice')


# In[ ]:




