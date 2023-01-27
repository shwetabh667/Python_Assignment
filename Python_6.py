#!/usr/bin/env python
# coding: utf-8

# # Programming Basic Assignment 6

# ### 1. Write a Python Program to Display Fibonacci Sequence Using Recursion?

# In[ ]:


nterms = int(input("Enter a Number"))
def recur_fibo(n):
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))

# check if the number of terms is valid
if nterms <= 0:
   print("Plese enter a positive integer")
else:
   print("Fibonacci sequence:")
   for i in range(nterms):
       print(recur_fibo(i))


# ### 2. Write a Python Program to Find Factorial of Number Using Recursion?

# In[1]:



num = int(input("Enter a Number"))
def recur_factorial(n):
   if n == 1:
       return n
   else:
       return n*recur_factorial(n-1)


# check if the number is negative
if num < 0:
   print("factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   print("The factorial of", num, "is", recur_factorial(num))


# ### 3. Write a Python Program to calculate your Body Mass Index?

# In[2]:


height = float(input("Input your height in Feet: "))
weight = float(input("Input your weight in Kilogram: "))
print("Your body mass index is: ", round(weight / (height * height), 2))


# ### 4. Write a Python Program to calculate the natural logarithm of any number?

# In[6]:



import math
N= int(input('Enter a number'))

print ("Natural logarithm of the given number is : ", end="")
print (math.log(N))


# 
# ### 5. Write a Python Program for cube sum of first n natural numbers?
# 

# In[3]:


n = int(input("Enter a number"))
# Returns the sum of series
def sumOfSeries(n):
    sum = 0
    for i in range(1, n+1):
        sum +=pow(i,3)

    return sum


# Driver Function

print(sumOfSeries(n))


# In[ ]:




