#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from tensorflow import keras
from tensorflow.keras import layers
import tensorflow as tf
import json
from tensorflow.keras import layers

input_shape = (1942, 1, 1)

csv_data = pd.read_csv('final_preprocessed_data.csv')
csv_data = csv_data.drop(['diggCount', 'shareCount', 'playCount', 'commentCount'], axis=1)

data = []
for i in range(len(csv_data)):
    arr = []
    for item in json.loads(csv_data['text'][i]):
        arr.append(item)
    for item in json.loads(csv_data['musicMeta.musicName'][i]):
        arr.append(item)
    for item in json.loads(csv_data['musicMeta.musicAuthor'][i]):
        arr.append(item)
    for item in json.loads(csv_data['musicMeta.musicAlbum'][i]):
        arr.append(item)
    for item in json.loads(csv_data['mentions'][i]):
        arr.append(item)
    for item in json.loads(csv_data['hashtags'][i]):
        arr.append(item)
    arr.append(csv_data['musicMeta.musicOriginal'][i])
    arr.append(csv_data['musicMeta.duration'][i])
    arr.append(csv_data['videoMeta.duration'][i])
    arr.append(csv_data['createTime'][i])
    data.append(arr)

engagement_data = csv_data['engagementMetric']

x_train, x_test, y_train, y_test = train_test_split(data, engagement_data)

x_train = np.expand_dims(x_train, -1)
x_test = np.expand_dims(x_test, -1)

y_train = keras.utils.to_categorical(y_train)
y_test = keras.utils.to_categorical(y_test)

model = keras.Sequential()

model.add(keras.Input(shape=input_shape))
model.add(keras.layers.Dense(1, activation='linear'))
model.add(keras.layers.Dropout(0.5))


model.summary()




batch_size = 128
epochs = 64

model.compile(loss = "mean_squared_logarithmic_error",optimizer="adam", metrics=["accuracy"])
model.fit(x_train, y_train, batch_size=batch_size, epochs=epochs, validation_split=0.1)
score = model.evaluate(x_test, y_test, verbose=0)
print("Test loss:", score[0])
print("Test accuracy:", score[1])


# In[ ]:





# In[ ]:




