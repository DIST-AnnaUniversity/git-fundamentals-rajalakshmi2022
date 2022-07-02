#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install numpy


# In[3]:


pip install pandas


# In[4]:


pip install tensorflow


# In[1]:


import numpy as np
x = np.array([2,5,7])
print(x)
print("Dimension ", x.ndim)
print("Shape ", x.shape)

y = np.array([[2,5,7],[3,6,8]])
print(y)
print("Dimension ", y.ndim)
print("Shape ", y.shape)

z = np.array([[[1,3,5,6],[2,4,6,7],[1,2,3,4]],[[4,3,2,1],[7,9,11,12],[8,10,12,9]]])
print(z)
print("Dimension ", z.ndim)
print("Shape ", z.shape)


# In[3]:


#Simple operation to illustrate constant and variable

import tensorflow as tf
x = tf.constant(2)
y = tf.Variable(x+4)
total=x+y
print(total)


# In[4]:


import tensorflow as tf
import numpy as np

matrix_1 = np.array([(1,2,3),(3,2,1),(1,1,1)],dtype = 'int32')
matrix_2 = np.array([(0,0,0),(-1,0,1),(3,3,4)],dtype = 'int32')
print("The first matrix is ")
print (matrix_1)
print("The second matrix is ")
print (matrix_2)
print("The sum is ")
matrix_1 = tf.constant(matrix_1)
matrix_2 = tf.constant(matrix_2)
matrix_sum = tf.add(matrix_1, matrix_2)
print((matrix_sum))


# In[5]:


import tensorflow as tf
import numpy as np

matrix_1 = np.array([(1,2,3),(3,2,1),(1,1,1)],dtype = 'int32')
matrix_2 = np.array([(0,0,0),(-1,0,1),(3,3,4)],dtype = 'int32')
print("The first matrix is ")
print (matrix_1)
print("The second matrix is ")
print (matrix_2)
print("The Difference is ")
matrix_1 = tf.constant(matrix_1)
matrix_2 = tf.constant(matrix_2)
matrix_diff = tf.subtract(matrix_1, matrix_2)
print((matrix_diff))


# In[6]:


import tensorflow as tf
import numpy as np

matrix_1 = np.array([(1,2,3),(3,2,1),(1,1,1)],dtype = 'int32')
matrix_2 = np.array([(0,0,0),(-1,0,1),(3,3,4)],dtype = 'int32')
print("The first matrix is ")
print (matrix_1)
print("The second matrix is ")
print (matrix_2)
print("The product is ")
matrix_1 = tf.constant(matrix_1)
matrix_2 = tf.constant(matrix_2)
matrix_prod = tf.matmul(matrix_1, matrix_2)
print((matrix_prod))


# In[ ]:




