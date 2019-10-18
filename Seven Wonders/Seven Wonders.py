#!/usr/bin/env python
# coding: utf-8

# In[6]:


import sys
S = str(input().split())
if(len(S)<= 50 and S == 'T'or 'C' or 'G'):
    list(S)
    T = S.count('T')
    C = S.count('C')
    G = S.count('G')
    bonus = 7 
    if(T is 0 or C is 0 or G is 0):
        final = T**2 + C**2 + G**2     
        print(final)
    number = 1 
    sqr = 1
    while (T >= 1 and C >= 1 and G >= 1):
        if (T is number or C is number or G is number):
            final = T**2 + C**2 + G**2 + (bonus*sqr)
            print(final)
            break
        else:
            number += 1 
            sqr += 1
else:
    sys.exit()


# In[5]:





# In[ ]:




