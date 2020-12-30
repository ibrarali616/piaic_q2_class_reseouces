#!/usr/bin/env python
# coding: utf-8

# # Numpy_Assignment_2::

# ## Question:1

# ### Convert a 1D array to a 2D array with 2 rows?

# #### Desired output::

# array([[0, 1, 2, 3, 4],
#         [5, 6, 7, 8, 9]])

# In[4]:


import numpy as np
x=np.array([0,1,2,3,4,5,6,7,8,9]).reshape(2,5)
x


# ## Question:2

# ###  How to stack two arrays vertically?

# #### Desired Output::
array([[0, 1, 2, 3, 4],
        [5, 6, 7, 8, 9],
       [1, 1, 1, 1, 1],
       [1, 1, 1, 1, 1]])
# In[7]:


y=np.ones(10).reshape(2,5)
np.vstack((x,y))


# ## Question:3

# ### How to stack two arrays horizontally?

# #### Desired Output::
array([[0, 1, 2, 3, 4, 1, 1, 1, 1, 1],
       [5, 6, 7, 8, 9, 1, 1, 1, 1, 1]])
# In[8]:


np.hstack((x,y))


# ## Question:4

# ### How to convert an array of arrays into a flat 1d array?

# #### Desired Output::
array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
# In[9]:


np.ravel(x)


# ## Question:5

# ### How to Convert higher dimension into one dimension?

# #### Desired Output::
array([ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])
# In[11]:


x=np.arange(15)
np.ravel(x)


# ## Question:6

# ### Convert one dimension to higher dimension?

# #### Desired Output::
array([[ 0, 1, 2],
[ 3, 4, 5],
[ 6, 7, 8],
[ 9, 10, 11],
[12, 13, 14]])
# In[15]:


x=np.reshape(x,(5,3))
x


# ## Question:7

# ### Create 5x5 an array and find the square of an array?

# In[19]:


x=np.arange(25).reshape(5,5)
x=np.square(x)
x


# ## Question:8

# ### Create 5x6 an array and find the mean?

# In[22]:


x=np.arange(30).reshape(5,6)
x=np.mean(x)
x


# ## Question:9

# ### Find the standard deviation of the previous array in Q8?

# In[27]:


m=np.arange(25).reshape(5,5)
np.std(m)


# ## Question:10

# ### Find the median of the previous array in Q8?

# In[29]:


np.median(m)


# ## Question:11

# ### Find the transpose of the previous array in Q8?

# In[32]:


np.transpose(m)


# ## Question:12

# ### Create a 4x4 an array and find the sum of diagonal elements?

# In[35]:


x=np.arange(16).reshape(4,4)
np.diagonal(x).sum()


# ## Question:13

# ### Find the determinant of the previous array in Q12?

# In[37]:


np.linalg.det(x)


# ## Question:14

# ### Find the 5th and 95th percentile of an array?

# In[40]:


print(np.percentile(x,5))
print(np.percentile(x,95))


# ## Question:15

# ### How to find if a given array has any null values?

# In[64]:


a=np.array([0,1,2,3,4,5,90,6,7,8,9,60])
b=a==0
print(f"the given array has null value {b.any()}")


# In[ ]:




