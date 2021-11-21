#!/usr/bin/env python
# coding: utf-8

# In[45]:


#Write a Python function to sum all the numbers in a list.
# Sample List : (8, 2, 3, 0, 7)
# Expected Output : 20


def sum(my_list):
    sum_num = 0
    for i in my_list:
        sum_num +=i
    return sum_num
print("Sum of number =",sum((8, 2, 3, 0, 7)))


# In[ ]:




