import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from tensorflow import keras
from tensorflow.keras import layers
import json
from tensorflow.keras import layers
from tensorflow.python.keras.layers.convolutional import Conv1D

def run_neural_net():

    input_shape = (1942, 1, 1) # Store the input data shape

    csv_data = pd.read_csv('../final_preprocessed_data.csv') # Read the data in as a csv

    data = [] # Initialize a list for the feature vectors
    for i in range(len(csv_data)): # For each row of the dataframe
        arr = [] # Initialize a new list for this row's features vector
        for item in json.loads(csv_data['text'][i]): # For each value in the text vector
            arr.append(item) # Append the value to this row's features vector
        for item in json.loads(csv_data['musicMeta.musicName'][i]): # For each value in the musicMeta.musicName vector
            arr.append(item)
        for item in json.loads(csv_data['musicMeta.musicAuthor'][i]): # For each value in the musicMeta.musicAuthor vector
            arr.append(item)
        for item in json.loads(csv_data['musicMeta.musicAlbum'][i]): # For each value in the musicMeta.musicAlbum vector
            arr.append(item)
        for item in json.loads(csv_data['mentions'][i]): # For each value in the mentions vector
            arr.append(item)
        for item in json.loads(csv_data['hashtags'][i]): # For each value in the hashtags vector
            arr.append(item) 
        arr.append(csv_data['musicMeta.musicOriginal'][i]) # Append the musicOriginal value to this row's features vector
        arr.append(csv_data['musicMeta.duration'][i]) # Append the musicMeta.duration value to this row's features vector
        arr.append(csv_data['videoMeta.duration'][i]) # Append the videoMeta.duration value to this row's features vector
        arr.append(csv_data['createTime'][i]) # Append the createTime value to this row's features vector
        data.append(arr) # Append this row's features vector to the list of feature vectors

    engagement_data = csv_data['engagementMetric'] # Store engagementMetric column as a variable

    x_train, x_test, y_train, y_test = train_test_split(data, engagement_data) # Split the training and testing data

    x_train = np.expand_dims(x_train, -1) # Add a dimension to the training data
    x_test = np.expand_dims(x_test, -1) # Add a dimension to the testing data

    y_train = keras.utils.to_categorical(y_train) # Make y_train a binary class matrix
    y_test = keras.utils.to_categorical(y_test) # Make y_test a binary class matrix

    # Create a model with an input layer, a 1 dimensional convolution layer, a dropout layer,
    # and a densly connected neural network layer.
    model = keras.Sequential(
        [
        keras.Input(shape=input_shape),
        layers.Conv1D(100, kernel_size=1, use_bias=True, activation="relu"),
        layers.Dropout(0.5),
        layers.Dense(1, activation='linear')
        ]
    )

    model.summary() # Print a summary of the network

    batch_size = 128 # Set the batch size
    epochs = 64 # Set the number of epochs

    # Compile the model with a mean_squared_logarithmic_error loss function and accuracy as the evaluation metric
    model.compile(loss='mean_squared_logarithmic_error', metrics=["accuracy"])
    model.fit(x_train, y_train, batch_size=batch_size, epochs=epochs, validation_split=0.1) # Fit the model to the data
    score = model.evaluate(x_test, y_test, verbose=0) # Evaluate the model on its performance
    print("Test loss:", score[0]) # Print the loss of the test
    print("Test accuracy:", score[1]) # Print the accuracy of the test