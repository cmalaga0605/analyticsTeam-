#!/usr/bin/env python
# coding: utf-8

# In[17]:


s = input()
y = 10**5
if(len(s) >= 1 and len(s) <= y):
    t = list(s)
    
    countW = 0
    countB = 0
    for element in t: 
        if(element == 'W'):
            countW += 1
        elif(element == 'B'):
            countB += 1
    if(countW == countB):
        print('1')
    else: 
        print('0')


# In[ ]:




