#!/usr/bin/env python
# coding: utf-8

# In[9]:


import sys
N = int(input())                                #Input integer 
n = [int(number) for number in input().split()] #input several integers 

if(N>= 1 and N <= 100):                         #Setting constraint 
    if(len(n) >= -1000000 and len(n) <= 1000000): #Setting constraint 
        count = 0
        for i in n:                               #loop to get the negative count
            y = int(i)
            if(y < 0):
                count += 1
        print(count)
else:
    sys.exit()


# In[ ]:





# In[ ]:



    

