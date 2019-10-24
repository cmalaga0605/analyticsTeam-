#!/usr/bin/env python
# coding: utf-8

# In[3]:


import sys   #imported the sys library
import math  # imported the math library
n = int(input()) 
ni = [int(number) for number in input().split()]   #took several inputs of the datatype int
if(n>= 1 and n <= 100000 ):                        #setting constraints for the first input
    for number in ni:                              # for loop to identify each individual number in ni
        if(number >= 0 and number <= 10**9):    
            small = ni.index(min(ni))              #declared a variable and set the variable equal to the min elements index
            print(small)
            break                                  #stoped the program from printing more than once
        else: 
            sys.exit()
else: 
    sys.exit()


# In[ ]:





# In[ ]:




