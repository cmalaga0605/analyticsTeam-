#!/usr/bin/env python
# coding: utf-8

# In[25]:


x , y = input().split()

month_list = ['JAN ', 'FEB' , 'MAR ' , 'APR ' , 'MAY ' , 'JUN ' , 'JUL ' , 'AUG ' , 'SEP ' ,'OCT','NOV' , 'DEC']

day_list = ['1' , '2'  , '3' , '4' , '5' , '6' , '7' , '8' , '9'  , '10' , '11' , '12' , '13' , '14'  , '15' , '16' ,
           '17' , '18' , '19' , '20', '21' , '22' , '23' , '24' , '25' , '26' , '27' , '28' , '29' , '30' , '31' ]

month1 = month_list[9]
day1 = day_list[30]

month2 = month_list[11]
day2 = day_list[24]


if (x == month1 and y == day1) or (x == month2 and y== day2):
    print("yup")
else: 
    print("nope")

    


# In[ ]:





# In[ ]:




