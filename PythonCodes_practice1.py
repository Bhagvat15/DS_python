#!/usr/bin/env python
# coding: utf-8

# In[2]:


10+20


# In[4]:


get_ipython().system('pip install pandas')


# In[1]:


import pandas as pd


# In[2]:


df = pd.read_csv("Salaries.csv")


# In[3]:


df.head(5)


# In[4]:


df.tail(5)


# In[8]:


df.head(10)


# In[9]:


df.head(50)


# In[11]:


df.dtypes


# In[12]:


df.columns


# In[13]:


df.axes


# In[14]:


df.ndim


# In[15]:


df.size


# In[16]:


df.shape


# In[17]:


df.values


# In[18]:


df.rows


# In[19]:


df.shape[0]


# In[8]:


df.describe()


# In[9]:


df.std()


# In[10]:


df.mean()


# In[11]:


df.median()


# In[12]:


df.mean(50)


# In[14]:


df.


# In[15]:


df1 = df.head(50)


# In[16]:


df1.mean()


# In[17]:


df.rank.mean()


# In[18]:


df.phd


# In[20]:


df['phd']


# In[21]:


df2 = df.phd.mean()


# In[22]:


df2


# In[23]:


df3 = df['phd'].median()


# In[24]:


df3


# In[26]:


df4 = df['phd'].std()


# In[27]:


df4


# In[28]:


df5 = df.phd.var()


# In[29]:


df5


# In[31]:


df6 = df.phd.count()


# In[32]:


df6


# In[33]:


df7 = df.salary.mean()


# In[34]:


df7


# In[38]:


df8 = df[['salary','phd']].var()


# In[39]:


df8


# In[40]:


df_rank = df.groupby(['rank'])


# In[42]:


df_rank.mean()


# In[44]:


df_sex  = df.groupby(['sex'])


# In[46]:


df_sex.mean()


# In[47]:


df_sex.count()


# In[48]:


df['salary'] > 120000


# In[57]:


df[(df['salary'] > 120000) & (df['phd'] > 40) & (df['service'] > 45)]
   


# In[5]:


df.iloc[0:10,1:6]


# In[10]:


df.iloc[[1,3],[5,6]]


# In[8]:


df.iloc[60:61]


# In[11]:


df.iloc[[1,10],[3,4]]


# In[13]:


df.iloc[[5,6]]


# In[15]:


df[['phd','salary']].agg(['min','mean','max','median'])


# In[ ]:




