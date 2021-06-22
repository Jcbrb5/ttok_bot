#!/usr/bin/env python
# coding: utf-8

# In[7]:


import numpy as np
import pandas as pd

data = pd.read_csv('preprocessed_data.csv', parse_dates=['createTime'])


# In[8]:


data.head


# In[22]:


data.iloc[0].shape


# In[16]:


print(type(data['playCount'].values))


# In[20]:


from sklearn.model_selection import train_test_split

train, test = train_test_split(data)



# In[ ]:


from tensorflow import keras
from tensorflow.keras import layers


input_shape = (14, 1)

# metric of engagement = 0.4 * shares + 0.3 * comments + 0.2 * likes + 0.1 * plays

