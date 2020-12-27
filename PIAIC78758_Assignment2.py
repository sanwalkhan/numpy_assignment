#!/usr/bin/env python
# coding: utf-8

# # Numpy_Assignment_2::

# In[2]:


import numpy as np


# ## Question:1

# ### Convert a 1D array to a 2D array with 2 rows?

# #### Desired output::

# array([[0, 1, 2, 3, 4],
#         [5, 6, 7, 8, 9]])

# In[11]:


x = np.arange(10)
x.ndim
y = x.reshape(5,2)
y.ndim


# ## Question:2

# ###  How to stack two arrays vertically?

# #### Desired Output::
array([[0, 1, 2, 3, 4],
        [5, 6, 7, 8, 9],
       [1, 1, 1, 1, 1],
       [1, 1, 1, 1, 1]])
# In[15]:


x = np.arange(10).reshape(5,2)
y = np.arange(10,20).reshape(5,2)


# In[17]:


np.vstack((x,y))


# ## Question:3

# ### How to stack two arrays horizontally?

# #### Desired Output::
array([[0, 1, 2, 3, 4, 1, 1, 1, 1, 1],
       [5, 6, 7, 8, 9, 1, 1, 1, 1, 1]])
# In[21]:


a = np.arange(10).reshape(5,2)
b = np.arange(10,20).reshape(5,2)


# In[22]:


np.hstack((a,b))


# ## Question:4

# ### How to convert an array of arrays into a flat 1d array?

# #### Desired Output::
array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
# In[25]:


x = np.vstack((a,b))
np.ravel(x)


# ## Question:5

# ### How to Convert higher dimension into one dimension?

# #### Desired Output::
array([ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])
# In[33]:


np.array([[1,2,3,4,5,6,7,8,9],[11,12,13,14,15,16,17,18,19]]).ravel()


# ## Question:6

# ### Convert one dimension to higher dimension?

# #### Desired Output::
array([[ 0, 1, 2],
[ 3, 4, 5],
[ 6, 7, 8],
[ 9, 10, 11],
[12, 13, 14]])
# In[38]:


np.arange(20).reshape(4,5)


# ## Question:7

# ### Create 5x5 an array and find the square of an array?

# In[46]:


arr = np.arange(25).reshape(5,5)*10


# In[47]:


np.sqrt(arr)


# ## Question:8

# ### Create 5x6 an array and find the mean?

# In[50]:


arr = np.arange(30).reshape(5,6)
np.mean(arr)


# ## Question:9

# ### Find the standard deviation of the previous array in Q8?

# In[51]:


np.std(arr)


# ## Question:10

# ### Find the median of the previous array in Q8?

# In[53]:


np.median(arr)


# ## Question:11

# ### Find the transpose of the previous array in Q8?

# In[58]:


arr


# In[59]:


arr.T


# ## Question:12

# ### Create a 4x4 an array and find the sum of diagonal elements?

# In[62]:


x = np.arange(16).reshape(4,4)


# In[65]:


np.diagonal(x)


# In[67]:


np.diagonal(x).sum()


# ## Question:13

# ### Find the determinant of the previous array in Q12?

# In[73]:


np.linalg.det(x)


# ## Question:14

# ### Find the 5th and 95th percentile of an array?

# In[79]:


x = np.arange(50)
print("5th percentile of array is ",np.percentile(x,5))
print("5th percentile of array is ",np.percentile(x,95))


# ## Question:15

# ### How to find if a given array has any null values?

# In[96]:


a = np.zeros(3)
array_sum = np.sum(a)
array_has_nan = np.isnan(array_sum)


# In[97]:


array_has_nan


# In[ ]:




