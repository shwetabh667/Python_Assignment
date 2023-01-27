# ### 1. Write a Python Program to find sum of array?

# In[2]:


arr = [11, 99, 8, 46, 7, 70, 7]
Sum = 0

for i in range(len(arr)):
   Sum = Sum + arr[i]
print (Sum)


# ### 2. Write a Python Program to find largest element in an array?
# 

# In[3]:


a = [11, 99, 8, 46, 7, 70, 7]
max_element = a[0]

for i in range(len(a)):
  if a[i] > max_element:
     max_element = a[i]

print (max_element)


# ### 3. Write a Python Program for array rotation?

# In[5]:



def leftRotate(arr, d, n):
    for i in range(d):
        leftRotatebyOne(arr, n)
 
def leftRotatebyOne(arr, n):
    temp = arr[0]
    for i in range(n-1):
        arr[i] = arr[i + 1]
    arr[n-1] = temp
         
 
def printArray(arr, size):
    for i in range(size):
        print ("% d"% arr[i], end =" ")
 
arr = [11, 99, 8, 46, 7, 70, 7]
leftRotate(arr, 2, 7)
printArray(arr, 7)


# ### 4. Write a Python Program to Split the array and add the first part to the end?

# In[6]:


# Python program to split array

def splitArr(arr, n, k):
    for i in range(0, k):
        x = arr[0]
        for j in range(0, n-1):
            arr[j] = arr[j + 1]
            
        arr[n-1] = x

arr = [11, 99, 8, 46, 7, 70, 7]
n = len(arr)
position = 3

splitArr(arr, n, position)

for i in range(0, n):
    print(arr[i], end = ' ')


# ### 5. Write a Python Program to check if given array is Monotonic?

# In[7]:


def isMonotonic(A):
   return (all(A[i] <= A[i + 1] for i in range(len(A) - 1)) or
      all(A[i] >= A[i + 1] for i in range(len(A) - 1)))

A = [11, 99, 8, 46, 7, 70, 7]
print(isMonotonic(A))


# In[ ]:




