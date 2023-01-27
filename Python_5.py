#!/usr/bin/env python
# coding: utf-8

# ## Python Basic Programming Assignment - 5
# --------------
# 

# ### 1. Write a Python Program to Find LCM?

# In[2]:



num1 = int(input("Enter 1st number")) 
num2 = int(input("Enter 2nd number")) 

def compute_lcm(x, y):

   if x > y:
       greater = x
   else:
       greater = y

   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1

   return lcm

print("The L.C.M. is", compute_lcm(num1, num2))


# ### 2. Write a Python Program to Find HCF?

# In[5]:


num1 = int(input("Enter 1st number")) 
num2 = int(input("Enter 2nd number")) 

def compute_hcf(x, y):

# choose the smaller number
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller+1):
        if((x % i == 0) and (y % i == 0)):
            hcf = i 
    return hcf

print("The H.C.F. is", compute_hcf(num1, num2))


# ### 3. Write a Python Program to Convert Decimal to Binary, Octal and Hexadecimal?

# In[8]:



dec = int(input("Enter th number")) 

print("The decimal value of", dec, "is:")
print(bin(dec), "in binary.")
print(oct(dec), "in octal.")
print(hex(dec), "in hexadecimal.")


# ### 4. Write a Python Program To Find ASCII value of a character?

# In[11]:


c = input("Enter the Character")
print("The ASCII value of '" + c + "' is", ord(c))


# ### 5. Write a Python Program to Make a Simple Calculator with 4 basic mathematical operations?

# In[13]:


num1 = float(input("Enter 1st number"))
num2 = float(input("Enter 2nd number"))

sum = num1 + num2
diff = num1 - num2
mult = num1 * num2
div = num1/ num2


print("The Sum of the Given Number is :", sum)
print("The Substraction of the Given Number is :", diff)
print("The Multiplication of the Given Number is :", mult)
print("The division of the Given Number is :", div)


# In[ ]:




