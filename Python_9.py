# ### 1. Write a Python program to check if the given number is a Disarium Number?

# In[1]:


def is_disarium(num):
    temp = 0
    for i in range(len(str(num))):
        temp += int(str(num)[i]) ** (i + 1)
    return temp == num

num = int(input("Enter a Number"))
print("\nIs",num,"is Disarium number?",is_disarium(num))


# ### 2. Write a Python program to print all disarium numbers between 1 to 100?

# In[10]:



def sumOfDigits(num):    
  rem = sum = 0;    
  len = calculateLength(num);    
      
  while(num > 0):    
      rem = num%10;    
      sum = sum + (rem**len);    
      num = num//10;    
      len = len - 1;    
  return sum;    
    
result = 0;    

print("Disarium numbers between 1 and 100 are");    
for i in range(1, 101):    
  result = sumOfDigits (i);    
      
  if(result == i):    
      print(i)   


# ### 3. Write a Python program to check if the given number is Happy Number?

# In[12]:


def isHappyNumber(num):    
    rem = sum = 0;    
          
    while(num > 0):    
        rem = num%10;    
        sum = sum + (rem*rem);    
        num = num//10;    
    return sum;    
        
num = int(input("Enter a number"));    
result = num;    
     
while(result != 1 and result != 4):    
    result = isHappyNumber(result);    
     
#Happy number always ends with 1    
if(result == 1):    
    print(str(num) + " is a happy number");    
#Unhappy number ends in a cycle of repeating numbers which contain 4    
elif(result == 4):    
    print(str(num) + " is not a happy number");


# ### 4. Write a Python program to print all happy numbers between 1 and 100?

# In[13]:


def isHappyNumber(num):    
    rem = sum = 0;    
        
    #Calculates the sum of squares of digits    
    while(num > 0):    
        rem = num%10;    
        sum = sum + (rem*rem);    
        num = num//10;    
    return sum;    
              
print("List of happy numbers between 1 and 100: ");    
for i in range(1, 101):    
    result = i;    
        
    #Happy number always ends with 1 and     
    #unhappy number ends in a cycle of repeating numbers which contains 4    
    while(result != 1 and result != 4):    
        result = isHappyNumber(result);    
        
    if(result == 1):    
        print(i),    
        print(" "), 


# ### 5. Write a Python program to determine whether the given number is a Harshad Number?

# In[14]:


num = int(input("Enter a Number"));    
rem = sum = 0;    
     
 
n = num;    
     
#Calculates sum of digits    
while(num > 0):    
    rem = num%10;    
    sum = sum + rem;    
    num = num//10;    
     
#Checks whether the number is divisible by the sum of digits    
if(n%sum == 0):    
    print(str(n) + " is a harshad number");    
else:    
    print(str(n) + " is not a harshad number");


# ### 6. Write a Python program to print all pronic numbers between 1 and 100?

# In[15]:



def isPronicNumber(num):    
 flag = False;    
     
 for j in range(1, num+1):    
     #Checks for pronic number by multiplying consecutive numbers    
     if((j*(j+1)) == num):    
         flag = True;    
         break;    
 return flag;    
  
#Displays pronic numbers between 1 and 100    
print("Pronic numbers between 1 and 100: ");    
for i in range(1, 101):    
 if(isPronicNumber(i)):    
     print(i),    
     print(" "),    


# In[ ]:




