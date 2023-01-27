

# ### 1. Write a Python program to print "Hello Python"?

# In[1]:


print("Hello Python")


# ### 2. Write a Python program to do arithmetical operations addition and division.?
# 

# In[ ]:



Number1 = float(input("Enter First Number"))
Number2 = float(input("Enter Second Number"))
#here i am using float so, that it works with decimal also.
sum = Number1 + Number2
divi = Number1 / Number2

print(sum)
print(divi)


# ### 3. Write a Python program to find the area of a triangle?
# 

# In[ ]:



a = float(input('Enter first side: '))
b = float(input('Enter second side: '))
c = float(input('Enter third side: '))


P = a+b+c              #P= Perimeter
S = P/2        #S= Semi Perimeter


A= (S*(S-a)*(S-b)* (S-c)) **0.5    #A= Area

print("The Perimeter of the Triangle is: ", P )

print("The Semi Perimeter of the Triangle is: ", S )

print("The Area of the Triangle is: ", A )


# ### 4. Write a Python program to swap two variables?
# 

# In[ ]:


#Swaping two variables

a = 3
b = 5

a, b = b, a 


print('The values of a= ', a)
print('The values of b= ', b)


# ### 5. Write a Python program to generate a random number?
# 

# In[ ]:


import random 
num = random.random()
print(num)


# In[ ]:


#to generate random number between two integers values

import random 
num = random.randint(10,20)
print(num)

