#!/usr/bin/env python
# coding: utf-8

# In[1]:


def initialss(name):
    if "-" in name:
        name = name.split("-")
    else:
        name = [name]
    abreviation = ""
    for i in name:
        abreviation += i[0]

    return abreviation
print(initialss(input()))


# In[ ]:




