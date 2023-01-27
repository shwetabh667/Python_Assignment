#!/usr/bin/env python
# coding: utf-8

# ## Programming Assignment_2
# -------------

# ### 1. Write a Python program to convert kilometers to miles?
# 

# In[2]:


#Kilometer to miles

k = float(input("Enter kilometers: "))   #k = kilometer

# conversion factor
c_f = 0.621371

# calculate miles
miles = k * c_f
print(k,'kilometers is equal to', miles, ' miles')


# ### 2.Write a Python program to convert Celsius to Fahrenheit?

# In[5]:


#celsius to fahrenheit
celsius = float(input('Enter the temperature in celsius'))

fahrenheit = (celsius * 1.8) + 32


print(celsius, "degree Celsius is equal to", fahrenheit, "degree Fahrenheit")


# ### 3. Write a Python program to display calendar?
# 

# In[9]:


# calendar 


import calendar
                       
yy = int(input("Enter year: "))
mm = int(input("Enter month: "))

# display the calendar
print(calendar.month(yy, mm,))


# ### 4. Write a Python program to solve quadratic equation?

# In[15]:


#Quadratic Equation ax**2 + bx + c = 0

import cmath    # import complex math module

a = float( input("Enter the Value of A"))
b = float(input("Enter the Value of B"))
c = float(input("Enter the Value of C"))

# calculate the discriminant
d = (b**2) - (4*a*c)

# finding two solutions
sol1 = (-b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
sol2 = (-b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)


print('The solution are {0} and {1}'.format(sol1,sol2))


# ### 5. Write a Python program to swap two variables without temp variable?

# In[18]:



a = 'Ineuron'
b = 'Python Class'
 
print ("Before swapping")
print("a =", a, "and b:", b)
 
# code to swap 
a, b = b, a
 
print ("After swapping")
print("a =", a , " and b :", b)


# In[ ]:




