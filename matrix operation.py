#!/usr/bin/env python
# coding: utf-8

# In[3]:


pip install numpy


# In[4]:


pip install pandas


# In[6]:


import numpy as np

A = np.array([[1,6,6],[8,-2,4],[-7,3,9]])
B = np.array([[6,-5,-2],[5,6,-4],[-9,6,8]])
C = A+B
print(C)


# In[7]:


import numpy as np

A = np.array([[1,6,6],[8,-2,4],[-7,3,9]])
B = np.array([[6,-5,-2],[5,6,-4],[-9,6,8]])
C = A-B
print(C)


# In[8]:


import numpy as np
 
mat1 = ([1, 6, 5],[3 ,4, 8],[2, 12, 3])
mat2 = ([3, 4, 6],[5, 6, 7],[6,56, 7])
res = np.dot(mat1,mat2)
print(res)


# In[ ]:




