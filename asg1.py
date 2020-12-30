#!/usr/bin/env python
# coding: utf-8

# # **Assignment For Numpy**

# Difficulty Level **Beginner**

# 1. Import the numpy package under the name np

# In[16]:


import numpy as np


# 2. Create a null vector of size 10 

# In[17]:


np.zeros(10)


# 3. Create a vector with values ranging from 10 to 49

# In[18]:


x=np.arange(10,49)


# 4. Find the shape of previous array in question 3

# In[19]:


np.shape(x)


# 5. Print the type of the previous array in question 3

# In[20]:


type(x)


# 6. Print the numpy version and the configuration
# 

# In[21]:


print(np.__version__)
print(np.show_config())


# 7. Print the dimension of the array in question 3
# 

# In[22]:


x.ndim


# 8. Create a boolean array with all the True values

# In[23]:


np.ones(5, dtype=bool)


# 9. Create a two dimensional array
# 
# 
# 

# In[24]:


y=np.arange(10).reshape(2,5)


# 10. Create a three dimensional array
# 
# 

# In[25]:


z=np.arange(18).reshape(2,3,3)


# Difficulty Level **Easy**

# 11. Reverse a vector (first element becomes last)

# In[26]:


x[::-1]


# 12. Create a null vector of size 10 but the fifth value which is 1 

# In[32]:


x=np.zeros(10)
x[-5]=1
x


# 13. Create a 3x3 identity matrix

# In[33]:


np.identity(3)


# 14. arr = np.array([1, 2, 3, 4, 5]) 
# 
# ---
# 
#  Convert the data type of the given array from int to float 

# In[34]:


arr = np.array([1,2,3,4,5])
arr.astype(float)


# 15. arr1 =          np.array([[1., 2., 3.],
# 
#                     [4., 5., 6.]])  
#                       
#     arr2 = np.array([[0., 4., 1.],
#      
#                    [7., 2., 12.]])
# 
# ---
# 
# 
# Multiply arr1 with arr2
# 

# In[35]:


arr1 = np.array([[1., 2., 3.],

            [4., 5., 6.]])
arr2 = np.array([[0., 4., 1.],

           [7., 2., 12.]])
arr1*arr2


# 16. arr1 = np.array([[1., 2., 3.],
#                     [4., 5., 6.]]) 
#                     
#     arr2 = np.array([[0., 4., 1.], 
#                     [7., 2., 12.]])
# 
# 
# ---
# 
# Make an array by comparing both the arrays provided above

# In[37]:


arr1 = np.array([[1., 2., 3.],

            [4., 5., 6.]]) 
arr2 = np.array([[0., 4., 1.],

            [7., 2., 12.]])

np.where(arr1==arr2)


# 17. Extract all odd numbers from arr with values(0-9)

# In[39]:


x=np.arange(0,10)
x[x % 2 ==1]


# 18. Replace all odd numbers to -1 from previous array

# In[41]:


x[::]=-1
x


# 19. arr = np.arange(10)
# 
# 
# ---
# 
# Replace the values of indexes 5,6,7 and 8 to **12**

# In[43]:


arr = np.arange(10)
arr[5:9]=12
arr


# 20. Create a 2d array with 1 on the border and 0 inside

# In[49]:


x=np.ones((4,4))
x[1:-1,1:-1]=0
x


# Difficulty Level **Medium**

# 21. arr2d = np.array([[1, 2, 3],
# 
#                     [4, 5, 6], 
# 
#                     [7, 8, 9]])
# 
# ---
# 
# Replace the value 5 to 12

# In[52]:


arr2d = np.array([[1, 2, 3],

            [4, 5, 6], 

            [7, 8, 9]])
arr2d[arr2d>=5]=12
arr2d


# 22. arr3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
# 
# ---
# Convert all the values of 1st array to 64
# 

# In[55]:


arr3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
arr3d[0,0:1]=64
arr3d


# 23. Make a 2-Dimensional array with values 0-9 and slice out the first 1st 1-D array from it

# In[60]:


w=np.array([0,1,2,3,4,5,6,7,8,9])
w=w.reshape(2,-1)
w[0]


# 24. Make a 2-Dimensional array with values 0-9 and slice out the 2nd value from 2nd 1-D array from it

# In[65]:


w=np.array([0,1,2,3,4,5,6,7,8,9])
w=w.reshape(2,-1)
w[1,1]


# 25. Make a 2-Dimensional array with values 0-9 and slice out the third column but only the first two rows

# In[69]:


w=np.array([0,1,2,3,4,5,6,7,8,9])
w=w.reshape(2,-1)
w[:,3]


# 26. Create a 10x10 array with random values and find the minimum and maximum values

# In[74]:


randnums=np.random.randint(1,500, size=(10,10))
print(f"min value is {randnums.min()}")
print(f"max value is {randnums.max()}")


# 27. a = np.array([1,2,3,2,3,4,3,4,5,6]) b = np.array([7,2,10,2,7,4,9,4,9,8])
# ---
# Find the common items between a and b
# 

# In[75]:


a = np.array([1,2,3,2,3,4,3,4,5,6])
b = np.array([7,2,10,2,7,4,9,4,9,8])
np.intersect1d(a,b)


# 28. a = np.array([1,2,3,2,3,4,3,4,5,6])
# b = np.array([7,2,10,2,7,4,9,4,9,8])
# 
# ---
# Find the positions where elements of a and b match
# 
# 

# In[76]:


np.where(a==b)


# 29.  names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])  data = np.random.randn(7, 4)
# 
# ---
# Find all the values from array **data** where the values from array **names** are not equal to **Will**
# 

# In[79]:


names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])
data = np.random.randn(7, 4)
print(names!="Will")
data[names!="Will"]



# 30. names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe']) data = np.random.randn(7, 4)
# 
# ---
# Find all the values from array **data** where the values from array **names** are not equal to **Will** and **Joe**
# 
# 

# In[84]:


names!="Joe","Will"


# Difficulty Level **Hard**

# 31. Create a 2D array of shape 5x3 to contain decimal numbers between 1 and 15.

# In[87]:


arr = np.arange(1,16, dtype=float).reshape(3,5)
arr


# 32. Create an array of shape (2, 2, 4) with decimal numbers between 1 to 16.

# In[88]:


arr = np.arange(1,17, dtype=float).reshape(2,2,4)
arr


# 33. Swap axes of the array you created in Question 32

# In[90]:


arr.ndim
arr.transpose()


# 34. Create an array of size 10, and find the square root of every element in the array, if the values less than 0.5, replace them with 0

# In[93]:


x = np.arange(10)
x=np.sqrt(x)
x[x<0.5]=0
x


# 35. Create two random arrays of range 12 and make an array with the maximum values between each element of the two arrays

# In[94]:


a=np.random.rand(12)
b=np.random.rand(12)
x=[]
for i in [a,b]:
    x=i.max
print(x)


# 36. names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])
# 
# ---
# Find the unique names and sort them out!
# 

# In[99]:


names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])
x=np.unique(names)
x=np.sort(x)
x


# 37. a = np.array([1,2,3,4,5])
# b = np.array([5,6,7,8,9])
# 
# ---
# From array a remove all items present in array b
# 
# 

# In[105]:


a = np.array([1,2,3,4,5])
b = np.array([5,6,7,8,9])
x=np.intersect1d(a,b)
a=np.delete(a,b)


# 38.  Following is the input NumPy array delete column two and insert following new column in its place.
# 
# ---
# sampleArray = numpy.array([[34,43,73],[82,22,12],[53,94,66]]) 
# 
# 
# ---
# 
# newColumn = numpy.array([[10,10,10]])
# 

# In[122]:


sampleArray = np.array([[34,43,73],[82,22,12],[53,94,66]])
sampleArray=np.delete(sampleArray,2,1)
newcolumn=([10,10,10])
sampleArray=np.insert(sampleArray,2,newcolumn,1)
sampleArray



# 39. x = np.array([[1., 2., 3.], [4., 5., 6.]]) y = np.array([[6., 23.], [-1, 7], [8, 9]])
# 
# 
# ---
# Find the dot product of the above two matrix
# 

# In[112]:


x = np.array([[1., 2., 3.], [4., 5., 6.]])
y = np.array([[6., 23.], [-1, 7], [8, 9]])
x.dot(y)


# 40. Generate a matrix of 20 random values and find its cumulative sum

# In[113]:


x=np.random.rand(20)
x


# In[114]:


x.cumsum()


# In[ ]:




