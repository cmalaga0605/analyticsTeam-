#!/usr/bin/env python
# coding: utf-8

# In[34]:


t,x = map(float,input().split())
n = int(x)

weights = list(map(int,input().split()))

count = 0

my_max = max(weights)
my_min = min(weights)

ratio = my_min / my_max

while(ratio < t):
    cut = my_max - my_min
    weights.remove(max(weights))
    weights.append(cut)
    weights.append(my_min)

    count += 1
    my_max = max(weights)
    my_min = min(weights)

    ratio = my_min / my_max  

if(ratio > t):
    print(count)


# In[ ]:




