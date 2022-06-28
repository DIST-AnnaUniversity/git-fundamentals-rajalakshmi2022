#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install numpy


# In[5]:


pip install pandas


# In[6]:



import numpy as np

def McOr(x,w,t):
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
w = np.array([15,15,-11])

t = 0
ans1 = McOr(x0,w,t)
print (x0, "value", ans1)
ans2 = McOr(x1,w,t)
print (x1, "value", ans2)
ans3 = McOr(x2,w,t)
print (x2, "value", ans3)
ans4 = McOr(x3,w,t)
print (x3, "value", ans4)


# In[ ]:





# In[ ]:





# In[ ]:




