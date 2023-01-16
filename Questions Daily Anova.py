#!/usr/bin/env python
# coding: utf-8

## Day1 Questions and answers

# write function that returns no of ways to award 1st, 2nd and 3rd cup among given input 'n' (participants) note :
# 
# 
# 		-> get the input 'n' from user
# 		-> restrict the participants 'n' to 250 (throw error message if participants cross above 250)
#         
#         
#  example : assume if no of participates 'n' given are 9
# 	     no of ways to award 1st, 2nd and 3rd cup are 504

# In[55]:


from math import perm
def no_of_ways_to_award(n):
    if n>250:
        raise Exception("No. Of particpants cannot be more than 250")
    return perm(n,3)


# In[56]:


no_of_ways_to_award(456)


# Write a function that takes a list of integers as input, and returns a new list of integers such that:
# Each element of the new list is the product of all the integers in the input list except the integer at the corresponding index.
# Do not use division operator and the solution should work for large inputs.
# 
# Example: If the input is [1, 2, 3, 4, 5]
# Output should be [120, 60, 40, 30, 24]

# In[ ]:





# In[25]:


#Method 1
def multiply_the_rest(nums):
    l = []        
    for i in nums:
        l.append(math.prod(nums)//i)
    return l
#Works only with non zero values in the list


# In[26]:


multiply_the_rest([1,2,3,4,5])


# In[ ]:





# In[46]:


#Method 2
def product_list(lst):
    n = len(lst)
    left_product = [1] * n
    right_product = [1] * n
    result = [1] * n
 

    left_product[0] = lst[0]
    for i in range(1, n):
        left_product[i] = lst[i] * left_product[i - 1]
        
        
        
    right_product[n - 1] = lst[n - 1]  
    for i in range(n - 2, -1, -1):
        right_product[i] = lst[i] * right_product[i + 1]

        

    for i in range(n):
        if i == 0:
            result[i] = right_product[i + 1]
        elif i == n - 1:
            result[i] = left_product[i - 1]
        else:
            result[i] = left_product[i - 1] * right_product[i + 1]
            
            
 
    return result

print(product_list([1, 2, 3, 4, 5, 0]))


# In[ ]:





# Given an integer number n, return the difference between the product of its digits and the sum of its digits.
# 
# Input: n = 234
# 
# Output: 15 
# 
# Explanation: 
# 
# Product of digits = 2 * 3 * 4 = 24 
# 
# Sum of digits = 2 + 3 + 4 = 9 
# 
# Result = 24 - 9 = 15

# In[ ]:





# In[44]:


def sum_prod_add(n):
    p = list(str(n))
    su = 0
    prod = 1
    for i in p:
        prod *= int(i)
        su += int(i)
    return prod-su
    


# In[45]:


sum_prod_add(234)


# In[47]:


#Write a function in Python that takes a list of integers and returns a new list with only the odd integers

def odd_op(int_list):
    l = []
    for i in int_list:
        if i%2 != 0:
            l.append(i)
    return l
pl = [1,2,3,4,5,6,7,8,9]
odd_op(pl)

#output: [1, 3, 5, 7, 9]




