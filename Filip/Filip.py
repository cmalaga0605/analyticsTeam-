#!/usr/bin/env python
# coding: utf-8

# In[11]:


import sys
A ,B = input().split()

if (A !=B and len(A) != "0" and len(B) != "0"):
    listA = [A[0] , A[1] , A[2]]
    listB = [B[0] , B[1] , B[2]]
    
    listA.reverse ()
    listB.reverse ()
    
    finalA = "".join(map(str , listA))
    finalB = "".join(map(str , listB))
    
    if(finalA > finalB ):
        print(finalA)
    else:
        print(finalB)
else:
    sys.exit()
    


# In[ ]:




