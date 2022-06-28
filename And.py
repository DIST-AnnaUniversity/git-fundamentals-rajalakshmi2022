#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install numpy


# In[2]:


pip install pandas


# In[3]:


import numpy as np

def McAnd(x,w,t):
    net = np.dot(x,w)
    if net>t:
        output = 1
    else:
        output = 0
    return output

x0 = np.array([0,0,1])
x1 = np.array([0,1,1])
x2 = np.array([1,0,1])
x3 = np.array([1,1,1])
w = np.array([1,1,-1])

t = 0
ans1 = McAnd(x0,w,t)
print (x0, "value", ans1)
ans2 = McAnd(x1,w,t)
print (x1, "value", ans2)
ans3 = McAnd(x2,w,t)
print (x2, "value", ans3)
ans4 = McAnd(x3,w,t)
print (x3, "value", ans4)


# In[3]:





import numpy as np

def McAnd(x,w,t):
    net = np.dot(x,w)
    if net>t:
        output = 1
    else:
        output = 0
    return output

x0 = np.array([0,0,1])
x1 = np.array([0,1,1])
x2 = np.array([1,0,1])
x3 = np.array([1,1,1])
w = np.array([1,1,-1])

t = 0
ans1 = McAnd(x0,w,t)
print (x0, "value", ans1)
ans2 = McAnd(x1,w,t)
print (x1, "value", ans2)
ans3 = McAnd(x2,w,t)
print (x2, "value", ans3)
ans4 = McAnd(x3,w,t)
print (x3, "value", ans4)


# In[12]:


#MC Culloch numpy Not
import numpy as np

def McNot(x,w,t):
    net = np.dot(x,w)
    if net>t:
        output = 1
    else:
        output = 0
    return output

x0 = np.array([0,1])
x1 = np.array([1,1])
w = np.array([1,-1])

t = 0
ans1 = McNot(x0,w,t)
print (x0, "value", ans1)
ans2 = McAnd(x1,w,t)
print (x1, "value", ans2)

 


# In[5]:


import numpy as np

# Matrices as ndarray objects
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [8, 9]])
print("a", type(a))
print(a)
print("\nb", type(b))
print(b)

# Matrices as matrix objects
c = np.matrix([[1, 2], [3, 4]])
d = np.matrix([[5, 6], [8, 9]])
print("\nc", type(c))
print(c)
print("\nd", type(d))
print(d)
print("\n* operation on two ndarray objects (Elementwise)")
print(a * b)
print("\n* operation on two matrix objects (same as np.dot())")
print(c * d)


# In[ ]:





# In[ ]:




