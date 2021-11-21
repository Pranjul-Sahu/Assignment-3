#!/usr/bin/env python
# coding: utf-8

# In[9]:


# Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.
# Sample String : 'The quick Brow Fox'
# Expected Output :
# No. of Upper case characters : 3
# No. of Lower case Characters : 12

def count_chara(my_char_count):
    count_upper = 0
    count_lower = 0
    for i in my_char_count:
        if i.isupper():
            count_upper +=1
        elif i.islower():
            count_lower +=1
        else:
            pass
    print("My String =",my_char_count)
    print("Number of character in upper case",count_upper)
    print("Number of character in lower case",count_lower)
count_chara('The quick Brow Fox')

