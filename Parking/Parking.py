#!/usr/bin/env python
# coding: utf-8

# In[12]:


a,b,c = [int(x)for x in input().split()]
d,e = [int(x)for x in input().split()]
f,g = [int(x)for x in input().split()]
h,i = [int(x)for x in input().split()]

j = list(range(d,e))
k = list(range(f,g))
l = list(range(h,i))

final = j+k+l
amount = 0 
for y in final:
    if final.count(y) == 1:
        amount += a
    elif final.count(y) == 2:
        amount += b
    elif final.count(y) == 3 :
        amount += c 
print(amount)


# In[ ]:





# In[ ]:




