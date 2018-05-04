
# coding: utf-8

# In[2]:


import pandas
import matplotlib.pyplot as plt


# In[4]:


df=pandas.read_csv('result1.csv')
df.head()


# In[15]:


plt.scatter(range(1024),df.prob[1022:2046])
plt.show()

