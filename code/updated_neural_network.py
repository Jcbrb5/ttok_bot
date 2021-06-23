#!/usr/bin/env python
# coding: utf-8

# In[81]:


import numpy as np
import pandas as pd

data = pd.read_csv('preprocessed_data_with_metric.csv', parse_dates=['createTime'])


# In[82]:


data = data.drop(['diggCount', 'shareCount', 'playCount', 'commentCount'], axis=1)


# In[83]:


data.head


# In[46]:


data.iloc[0].shape


# In[48]:


data[1]


# In[38]:


pip install --upgrade pip


# In[39]:


pip install tensorflow


# In[49]:


from sklearn.model_selection import train_test_split
from tensorflow import keras
from tensorflow.keras import layers

from numpy.random import seed
from tensorflow.random import set_seed

seed(4100)
set_seed(4100)


# In[78]:


data.dtypes


# In[75]:



input_shape = (11, 1)

# metric of engagement = 0.4 * shares + 0.3 * comments + 0.2 * likes + 0.1 * plays

X = data.iloc[:, 0:11]

x_train, x_test, y_train, y_test = train_test_split(X, data['engagementMetric'], random_state=4100)

x_train = np.expand_dims(x_train, -1)
x_test = np.expand_dims(x_test, -1)

print("x_train shape:", x_train.shape)
print(x_train.shape[0], "train samples")
print(x_test.shape[0], "test samples")

y_train = keras.utils.to_categorical(y_train)
y_test = keras.utils.to_categorical(y_test)


# In[76]:


model = keras.Sequential()

model.add(keras.Input(shape=input_shape))
model.add(keras.layers.Dense(8))
model.add(keras.layers.Dropout(0.5))

model.summary()


# In[77]:


batch_size = 128
epochs = 64

model.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"])

model.fit(x_train, y_train, batch_size=batch_size, epochs=epochs, validation_split=0.1)


# In[ ]:




