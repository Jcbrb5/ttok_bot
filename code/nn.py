import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from tensorflow import keras
from tensorflow.keras import layers
import tensorflow as tf
import json

input_shape = (10, 1)

data = pd.read_csv('../final_preprocessed_data.csv')
data = data.drop(['diggCount', 'shareCount', 'playCount', 'commentCount'], axis=1)

# i = 0
# for row in data['text']:
#     data['text'][i] = np.asarray(json.loads(data['text'][i])).astype('float32')
#     i += 1

# i = 0
# for row in data['musicMeta.musicName']:
#     data['musicMeta.musicName'][i] = np.asarray(json.loads(data['musicMeta.musicName'][i])).astype('float32')
#     i += 1

# i = 0
# for row in data['musicMeta.musicAuthor']:
#     data['musicMeta.musicAuthor'][i] = np.asarray(json.loads(data['musicMeta.musicAuthor'][i])).astype('float32')
#     i += 1

# i = 0
# for row in data['musicMeta.musicAlbum']:
#     data['musicMeta.musicAlbum'][i] = np.asarray(json.loads(data['musicMeta.musicAlbum'][i])).astype('float32')
#     i += 1

# i = 0
# for row in data['mentions']:
#     data['mentions'][i] = np.asarray(json.loads(data['mentions'][i])).astype('float32')
#     i += 1

# i = 0
# for row in data['hashtags']:
#     data['hashtags'][i] = np.asarray(json.loads(data['hashtags'][i])).astype('float32')
#     i += 1

##############################################
################### TESTING #####################
i = 0
for row in data['text']:
    x = json.loads(data['text'][i])
    data['text'][i] = []
    for item in x:
        data['text'][i].append(item)
    # data['text'][i] = json.loads(data['text'][i])
    i += 1

print('text')
print(len(data['text'][0]))

i = 0
for row in data['musicMeta.musicName']:
    x = json.loads(data['musicMeta.musicName'][i])
    data['musicMeta.musicName'][i] = []
    for item in x:
        data['musicMeta.musicName'][i].append(item)
    # data['musicMeta.musicName'][i] = json.loads(data['musicMeta.musicName'][i])
    i += 1

i = 0
for row in data['musicMeta.musicAuthor']:
    x = json.loads(data['musicMeta.musicAuthor'][i])
    data['musicMeta.musicAuthor'][i] = []
    for item in x:
        data['musicMeta.musicAuthor'][i].append(item)
    # data['musicMeta.musicAuthor'][i] = json.loads(data['musicMeta.musicAuthor'][i])
    i += 1

i = 0
for row in data['musicMeta.musicAlbum']:
    x = json.loads(data['musicMeta.musicAlbum'][i])
    data['musicMeta.musicAlbum'][i] = []
    for item in x:
        data['musicMeta.musicAlbum'][i].append(item)
    # data['musicMeta.musicAlbum'][i] = json.loads(data['musicMeta.musicAlbum'][i])
    i += 1

i = 0
for row in data['mentions']:
    x = json.loads(data['mentions'][i])
    data['mentions'][i] = []
    for item in x:
        data['mentions'][i].append(item)
    # data['mentions'][i] = json.loads(data['mentions'][i])
    i += 1

i = 0
for row in data['hashtags']:
    x = json.loads(data['hashtags'][i])
    data['hashtags'][i] = list()
    for item in x:
        data['hashtags'][i].append(item)
    # data['hashtags'][i] = json.loads(data['hashtags'][i])
    i += 1

np.asarray(data['createTime']).astype('float32')

lol = []
for i in range(len(data['createTime'])):
    arr = []
    arr.append(data['createTime'][i])
    arr.append(data['musicMeta.musicOriginal'][i])
    arr.append(data['musicMeta.duration'][i])
    arr.append(data['videoMeta.duration'][i])
    lol.append(arr)

data['combined'] = lol

data = data.drop(['createTime', 'musicMeta.musicOriginal', 'musicMeta.duration', 'videoMeta.duration'], axis=1)

print(data.columns)

cat_data = data['engagementMetric']


# text = data['text']
# createTime = data['createTime']
# musicName = data['musicMeta.musicName']
# musicAuthor = data['musicMeta.musicAuthor']
# musicOriginal = data['musicMeta.musicOriginal']
# musicAlbum = data['musicMeta.musicAlbum']
# musicDuration = data['musicMeta.duration']
# videoDuration = data['videoMeta.duration']
# mentions = data['mentions']
# hashtags = data['hashtags']
# engagementMetric = data['engagementMetric']


tiktok_data = data.drop(['engagementMetric'], axis=1)

x_train, x_test, y_train, y_test = train_test_split(tiktok_data, cat_data, random_state=4100)

x_train = np.expand_dims(x_train, -1)
x_test = np.expand_dims(x_test, -1)

y_train = keras.utils.to_categorical(y_train)
y_test = keras.utils.to_categorical(y_test)

# text_train, text_test, createTime_train, createTime_test, musicName_train, musicName_test, musicAuthor_train, musicAuthor_test, \
# musicOriginal_train, musicOriginal_test, musicAlbum_train, musicAlbum_test, musicDuration_train, musicDuration_test, videoDuration_train, \
# videoDuration_test, mentions_train, mentions_test, hashtags_train, hashtags_test, engagementMetric_train, engagementMetric_test = \
# train_test_split(text, createTime, musicName, musicAuthor, musicOriginal, musicAlbum, musicDuration, videoDuration, mentions, hashtags,
# engagementMetric)

# text_train = np.expand_dims(text_train, -1)
# text_test = np.expand_dims(text_test, -1)
# createTime_train = np.expand_dims(createTime_train, -1)
# createTime_test = np.expand_dims(createTime_test, -1)
# musicName_train = np.expand_dims(musicName_train, -1)
# musicName_test = np.expand_dims(musicName_test, -1)
# musicAuthor_train = np.expand_dims(musicAuthor_train, -1)
# musicAuthor_test = np.expand_dims(musicAuthor_test, -1)
# musicOriginal_train = np.expand_dims(musicOriginal_train, -1)
# musicOriginal_test = np.expand_dims(musicOriginal_test, -1)
# musicAlbum_train = np.expand_dims(musicAlbum_train, -1)
# musicAlbum_test = np.expand_dims(musicAlbum_test, -1)
# musicDuration_train = np.expand_dims(musicDuration_train, -1)
# musicDuration_test = np.expand_dims(musicDuration_test, -1)
# videoDuration_train = np.expand_dims(videoDuration_train, -1)
# videoDuration_test = np.expand_dims(videoDuration_test, -1)
# mentions_train = np.expand_dims(mentions_train, -1)
# mentions_test = np.expand_dims(mentions_test, -1)
# hashtags_train = np.expand_dims(hashtags_train, -1)
# hashtags_test = np.expand_dims(hashtags_test, -1)



# engagementMetric_train = keras.utils.to_categorical(engagementMetric_train)
# engagementMetric_test = keras.utils.to_categorical(engagementMetric_test)

model = keras.Sequential()

model.add(keras.Input(shape=input_shape))
model.add(keras.layers.Dense(8))
model.add(keras.layers.Dropout(0.5))

model.summary()

batch_size = 128
epochs = 64

model.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"])

# list_of_features = [text_train, createTime_train, musicName_train, musicAuthor_train, musicOriginal_train, musicAlbum_train, \
#                     musicDuration_train, videoDuration_train, mentions_train, hashtags_train]


# features_tensor = tf.convert_to_tensor(list_of_features)

# model.fit(features_tensor, engagementMetric_train, batch_size=batch_size, epochs=epochs, validation_split=0.1)

print(x_train)

y_tensor = tf.convert_to_tensor(y_train)
x_tensor = tf.ragged.constant(x_train)

model.fit(x_tensor, y_tensor, batch_size=batch_size, epochs=epochs, validation_split=0.1)