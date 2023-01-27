# ### 1. Write a Python Program to Add Two Matrices?

# In[1]:



X = [[8,3,3],
    [1 ,8,6],
    [9 ,8,9]]

Y = [[9,8,2],
    [6,7,3],
    [3,5,4]]

result = [[0,0,0],
         [0,0,0],
         [0,0,0]]

# iterate through rows
for i in range(len(X)):
   # iterate through columns
   for j in range(len(X[0])):
       result[i][j] = X[i][j] + Y[i][j]

for r in result:
   print(r)


# ### 2. Write a Python Program to Multiply Two Matrices?

# In[2]:



X = [[9,7,3],
    [2 ,5,6],
    [8 ,8,9]]

Y = [[5,8,1,2],
    [6,7,3,0],
    [4,5,9,1]]

result = [[0,0,0,0],
         [0,0,0,0],
         [0,0,0,0]]

# iterate through rows of X
for i in range(len(X)):
   # iterate through columns of Y
   for j in range(len(Y[0])):
       # iterate through rows of Y
       for k in range(len(Y)):
           result[i][j] += X[i][k] * Y[k][j]

for r in result:
   print(r)


# ### 3. Write a Python Program to Transpose a Matrix?

# In[4]:



X = [[9,7],
    [3 ,5],
    [8 ,8]]

result = [[0,0,0],
         [0,0,0]]

# iterate through rows
for i in range(len(X)):

   for j in range(len(X[0])):
       result[j][i] = X[i][j]

for r in result:
   print(r)


# 
# ### 4. Write a Python Program to Sort Words in Alphabetic Order?
# 

# In[5]:



my_str = input("Enter a string: ")

# breakdown the string into a list of words
words = [word.lower() for word in my_str.split()]

# sort the list
words.sort()

# display the sorted words

print("The sorted words are:")
for word in words:
   print(word)


# ### 5. Write a Python Program to Remove Punctuation From a String?

# In[6]:



punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

my_str = input("Enter a string: ")

# remove punctuation from the string
no_punct = ""
for char in my_str:
   if char not in punctuations:
       no_punct = no_punct + char

# display the unpunctuated string
print(no_punct)


# In[ ]:




