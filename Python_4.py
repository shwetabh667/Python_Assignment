# ### 1. Write a Python Program to Find the Factorial of a Number?

# In[2]:



#the factorial of a number means:- 
#the multiplication of the number with every positive integer less than that. 
#So, n!= n × (n-1) × (n-2) × (n-3) × ..... × 3 × 2 × 1.

num = int(input("Enter a number: "))

factorial = 1

# check if the number is negative, positive or zero
if num < 0:
   print("factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,num + 1):
       factorial = factorial*i
   print("The factorial of",num,"is",factorial)


# ### 2. Write a Python Program to Display the multiplication Table?

# In[4]:


num = int(input("Display multiplication table of "))
   
for i in range(1, 11):
  print(num, 'x', i, '=', num*i)


# ### 3. Write a Python Program to Print the Fibonacci sequence?
# 

# In[6]:



nterms = int(input("How many terms? "))

n1, n2 = 0, 1
count = 0

# check if the number of terms is valid
if nterms <= 0:
   print("Please enter a positive integer")
# if there is only one term, return n1
elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(n1)
# generate fibonacci sequence
else:
   print("Fibonacci sequence:")
   while count < nterms:
       print(n1)
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth
       count += 1


# ### 4. Write a Python Program to Check Armstrong Number?

# In[7]:


num = int(input("Enter a number: "))

sum = 0

#find the sum of the cube of each digit
temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** 3
   temp //= 10

# display the result
if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")


# ### 5. Write a Python Program to Find Armstrong Number in an Interval?

# In[9]:



lower = int(input("Enter 1st Number"))
upper = int(input("Enter 2nd Number"))

for num in range(lower, upper + 1):

   # order of number
   order = len(str(num))
    
   # initialize sum
   sum = 0

   temp = num
   while temp > 0:
       digit = temp % 10
       sum += digit ** order
       temp //= 10

   if num == sum:
       print(num)


# ### 6. Write a Python Program to Find the Sum of Natural Numbers?

# In[11]:



num = int(input("Enter the number"))

if num < 0:
   print("Enter a positive number")
else:
   sum = 0
   # use while loop to iterate until zero
   while(num > 0):
       sum += num
       num -= 1
   print("The sum is", sum)


# In[ ]:




