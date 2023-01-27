# ### 1. Write a Python Program to Check if a Number is Positive, Negative or Zero?

# In[5]:


num1 = float(input("Enter a number: "))
if num1 > 0:
    
   print("The Given Number is Positive number")
elif num1 == 0:
   print("The Given Number is Zero")
else:
   print("The Given is Negative number")


# ### 2. Write a Python Program to Check if a Number is Odd or Even?
# 

# In[12]:



num1 = int(input("Enter a number: "))
if (num1 % 2) == 0:
   print("{0} is Even".format(num1))
else:
   print("{0} is Odd".format(num1))


# ### 3. Write a Python Program to Check Leap Year?
# 

# In[13]:




year = int(input("Enter Year in YYYY Format : "))

# if the entered year is divided by 100 means century year (ending with 00)
# if the century year divided by 400 is leap year
if (year % 400 == 0) and (year % 100 == 0):
    print("{0} is a leap year".format(year))

# not divided by 100 means not a century year
# year divided by 4 is a leap year
elif (year % 4 ==0) and (year % 100 != 0):
    print("{0} is a leap year".format(year))

# if not divided by both 400 (century year) and 4 (not century year)
# year is not leap year
else:
    print("{0} is not a leap year".format(year))


# ### 4. Write a Python Program to Check Prime Number?

# In[17]:


#Prime numbers:- Prime Number are numbers that have only 2 factors: 1 and themselves

num1 = int(input("Enter a number: "))

# define a flag variable
flag = False

# prime numbers are greater than 1
if num1 > 1:
    # check for factors
    for i in range(2, num1):
        if (num1 % i) == 0:
            flag = True
            # break out of loop
            break

# check if flag is True
if flag:
    print(num1, "is not a prime number")
else:
    print(num1, "is a prime number")


# ### 5. Write a Python Program to Print all Prime Numbers in an Interval of 1-10000?

# In[20]:




lower = 1
upper = 10000

print("Prime numbers between", lower, "and", upper, "are:")

for prime_num in range(lower, upper + 1):
   
   if prime_num > 1:
       for i in range(2, prime_num):
           if (prime_num % i) == 0:
               break
       else:
           print(prime_num)


# In[ ]:




