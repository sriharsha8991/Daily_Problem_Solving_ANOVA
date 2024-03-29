#!/usr/bin/env python
# coding: utf-8
#------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Day1 Questions and answers
#------------------------------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------Q1------------------------------------------------------------------------------------------------------

# write function that returns no of ways to award 1st, 2nd and 3rd cup among given input 'n' (participants) note :
# 		-> get the input 'n' from user
# 		-> restrict the participants 'n' to 250 (throw error message if participants cross above 250)   
#  example : assume if no of participates 'n' given are 9
# 	     no of ways to award 1st, 2nd and 3rd cup are 504
#Method 1
from math import perm
def no_of_ways_to_award(n):
    if n>250:
        raise Exception("No. Of particpants cannot be more than 250")
    return perm(n,3)

#Method 2
def pp(n):
    if n > 250:
        print("Error can participate in event")
    else:
        temp=n
        for i in range(1,3):
            temp = (n-i)*temp
        return "No of ways to awards cup are {}".format(temp)
    
    
#-------------------------------------------------------------------Q2---------------------------------------------------------------------------------------------

# Write a function that takes a list of integers as input, and returns a new list of integers such that:
# Each element of the new list is the product of all the integers in the input list except the integer at the corresponding index.
# Do not use division operator and the solution should work for large inputs.
# Example: If the input is [1, 2, 3, 4, 5]
# Output should be [120, 60, 40, 30, 24]


#Method 1

def multiply_the_rest(nums):
    l = []        
    for i in nums:
        l.append(math.prod(nums)//i)
    return l
#Works only with non zero values in the list
multiply_the_rest([1,2,3,4,5])


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

# Method 3
def product_list(numbers):
    n = len(numbers)
    product = [1] * n
    left_product = 1
    for i in range(n):
        product[i] *= left_product
        left_product *= numbers[i]
    right_product = 1
    for i in range(n-1, -1, -1):
        product[i] *= right_product
        right_product *= numbers[i]
    return product

numbers = [1, 2, 3, 4, 5,0]
print(product_list(numbers))



#----------------------------------------------------------Q3-------------------------------------------------------------------------------------------------

# Given an integer number n, return the difference between the product of its digits and the sum of its digits.
# Input: n = 234
# Output: 15 
# Explanation: 
# Product of digits = 2 * 3 * 4 = 24 
# Sum of digits = 2 + 3 + 4 = 9 
# Result = 24 - 9 = 15

def sum_prod_add(n):
    p = list(str(n))
    su = 0
    prod = 1
    for i in p:
        prod *= int(i)
        su += int(i)
    return prod-su

sum_prod_add(234)



#-----------------------------------------------------------Q4---------------------------------------------------------------------------------------------------------

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


#_____________________________________________________________________________________________________________________________________________________________________
#_______________________________________________________________________D A Y 2_______________________________________________________________________________________
#-----------------------------------------------------------------------------Q1--------------------------------------------------------------------------------------
### Q1
#My Question--
#"Given a list of integers, write a function to find the second largest number in the list.
#The function should return the second largest number, or None if there is less than 2 numbers in the list. 
#Additionally, the function should not use any built-in sorting functions, and should have a time complexity of O(n)."

#Method 1
pp = [1,2,3,4,56,67,5]
def second_largest(nums):
    if len(nums)>2:
        nums.remove(max(nums))
        return max(nums)
    return None
#second_largest(pp)

#Method 2
maxi = 0
second = 0
for i in pp: 
    if i>maxi:
        maxi,second = i,maxi
    elif i>second:
        second = i
print(second)

#Method sorting -3
P_sort = sorted(pp)
second_largest = P_sort[-2]
second_largest
#Output -- 56

#----------------------------------------------------------------------Q2--------------------------------------------------------------------------------------------
### Q2
# Create a function that takes the number of wins, draws and losses and calculates the number of points a football team has obtained so far.

# wins get 3 points
# draws get 1 point
# losses get 0 points

# Examples
# football_points(3, 4, 2) ➞ 13
# football_points(5, 0, 2) ➞ 15
# football_points(0, 0, 1) ➞ 0
# Inputs will be numbers greater than or equal to 0.

def football_points(tup):
    #tup-->(win,draw,lost)
    """ wins get 3 points
        draws get 1 point
        losses get 0 points
        """
    return tup[0]*3+tup[1]*1
football_points((5,0,2))
#Output -- 15

#-----------------------------------------------------------------Q3------------------------------------------------------------------------------------------------
### Q3
# Create a python program that takes a string as input and returns a new string with the first and last letters of the input string swapped.

# You should use string slicing to solve this problem.

# Example:
def swap_first_last(string):
    # return the new string with first and last letters swapped
    pass

# print(swap_first_last("Hello")) # should return "oellH"
# This problem requires the use of string slicing and string manipulation to swap the first and last letters of the input string.
# It's a simple problem that can help students to practice their understanding of string slicing and string manipulation in python.

def swap_first_last(string):
    return string[-1]+string[1:-1]+string[0]
swap_first_last("Hello")
#Output-- 'oellH'

#______________________________________________________________________________________________________________________________________________________________________
#-----------------------------------------------------------------------DAY4-------------------------------------------------------------------------------------------
# Write a program that takes two String input's i.e "str1" , "str2" and returns the letters of str2 that are not in the str1

# Example : 
#  Assume if two strings given by user are
#   -> str1 = "hello"
#   -> str2 = "world"
#   -> result = "wrd"
def uncommon(str1,str2):
    ans = ""
    for i in str2:
        if i not in str1:
            ans += i
    return ans


# Problem Description
# Given an one-dimensional unsorted array A containing N integers.
# You are also given an integer B, find if there exists a pair of elements in the array whose difference is B.
# Return 1 if any such pair exists else return 0.

# Input Format
# First argument is an integer array A of size N.
# Second argument is an integer B.
# Output Format
# Return 1 if any such pair exists else return 0.

# Example Input
# Input 1:
#  A = [5, 10, 3, 2, 50, 80]
#  B = 78

# Input 2:
#  A = [-10, 20]
#  B = 30

# Example Output
# Output 1:  1
# Output 2:  1

# Example Explanation
# Explanation 1:
#  Pair (80, 2) gives a difference of 78.
# Explanation 2:

#  Pair (20, -10) gives a difference of 30 i.e 20 - (-10) => 20 + 10 => 30

# Note:You only need to implement the given function. Do not read input, instead use the arguments to the function. Do not print the output, instead return values as specified.

#Brutforce:
def diff_pair(l,b):
    for i in l:
        for j in l:
            if (i-j==b) or (j-i==b):
                return 1
    return 0

#Hash Table: O(n) complexity
def diff_pair_hast(l,b):
    dt = {}
    for i in range(len(l)):
        dt[l[i]] = i
    print(dt)
    for i in range(len(l)):
        if (l[i]-b in dt) or (l[i]+b in dt):
            return 1
    return 0
        
diff_pair_hast([20,-10,25],35) 


# Create a Python program that takes a list of integers as input and returns a new list with the even numbers sorted in ascending order and the odd numbers sorted in descending order.

# You should use list comprehension and lambda function to solve this problem.

# def sort_even_odd(numbers):
#     # return the new list with even numbers sorted in ascending order and odd numbers sorted in descending order
#     pass

# print(sort_even_odd([1, 2, 3, 4, 5, 6, 7, 8, 9])) # should return [9, 7, 5, 3, 1, 2, 4, 6, 8]

def sort_even_odd(numbers):
    numbers.sort(key=lambda x: x if x%2==0 else -x)
    return numbers

numbers = [3, 2, 7, 9, 12, 8, 11, 6]
print(sort_even_odd(numbers))
