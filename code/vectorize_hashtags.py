# Data processing script number 4

import ast
import json
from numpy.lib.function_base import vectorize
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
import pandas as pd

# Read in data from csv
df = pd.read_csv('../clean_hashtags.csv')

# Initialize list of words to be encoded
words_to_vectorize = []

# Iterate through rows of the 'hashtags' column
for item in df['hashtags']:
    item = ast.literal_eval(item) # Convert JSON string array to list
    string = ''
    if len(item) > 0: # If the list is not empty do the following...
        for word in item: # Iterate through words in list
            string += word + ' ' # Append words to string separated by spaces
        string = string[:-1] # Remove the last space from the end of the string
    words_to_vectorize.append(string) # Add this string (containing all of the hashtags of a given post) to the list of words to encode

# Create an instance of TfidfVectorizer
vectorizer = TfidfVectorizer()
x = vectorizer.fit_transform(words_to_vectorize) # Fit the vectorizer to the data
vectors = vectorizer.transform(words_to_vectorize) # Convert the list of strings to vectors
vectors_as_array = vectors.toarray() # Convert object to array

i = 0
for vector in vectors_as_array:
    df['hashtags'][i] = json.dumps(vector.tolist()) # Add vectors to dataframe
    i += 1

df.to_csv('../encoded_hashtags.csv', index=False) # Save dataframe to csv