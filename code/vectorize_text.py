# Data processing script number 5

import ast
import json
from numpy.lib.function_base import vectorize
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
import pandas as pd

# Read in data from csv
df = pd.read_csv('../encoded_hashtags.csv')

################################# ENCODE MENTIONS #################################

# Initialize list of words to be encoded
words_to_vectorize = []

# Iterate through rows of the 'mentions' column
for item in df['mentions']:
    item = ast.literal_eval(item) # Convert JSON string array to list
    string = ''
    if len(item) > 0: # If the list is not empty do the following...
        for word in item: # Iterate through words in list
            string += word + ' ' # Append words to string separated by spaces
        string = string[:-1] # Remove the last space from the end of the string
    words_to_vectorize.append(string) # Add this string (containing all of the hashtags of a given post) to the list of words to encode

# Create an instance of TfidfVectorizer
mentions_vectorizer = TfidfVectorizer()
x = mentions_vectorizer.fit_transform(words_to_vectorize) # Fit the vectorizer to the data
vectors = mentions_vectorizer.transform(words_to_vectorize) # Convert the list of strings to vectors
vectors_as_array = vectors.toarray() # Convert object to array

i = 0
for vector in vectors_as_array:
    df['mentions'][i] = json.dumps(vector.tolist()) # Add vectors to dataframe
    i += 1

################################# END #################################

################################# ENCODE MUSIC ALBUMS #################################

# Initialize a list of albums
list_of_albums = []

# Iterate through rows of the 'musicMeta.musicAlbum' column
for album in df['musicMeta.musicAlbum']:
    string = ''
    if type(album) == str: # If row has an album
        string += album # Append album to string
    list_of_albums.append(string) # Add this string to the list of words to encode

# Create an instance of TfidfVectorizer
music_albums_vectorizer = TfidfVectorizer()
x = music_albums_vectorizer.fit_transform(list_of_albums) # Fit the vectorizer to the data
vectors = music_albums_vectorizer.transform(list_of_albums) # Convert the list of strings to vectors
vectors_as_array = vectors.toarray() # Convert object to array

i = 0
for vector in vectors_as_array:
    df['musicMeta.musicAlbum'][i] = json.dumps(vector.tolist()) # Add vectors to dataframe
    i += 1

################################# END #################################

################################# ENCODE MUSIC AUTHOR #################################

# Initialize a list of author
list_of_authors = []

# Iterate through rows of the 'musicMeta.musicAuthor' column
for author in df['musicMeta.musicAuthor']:
    string = ''
    if type(author) == str: # Ensure row has author
        string += author # Append album to string
    list_of_authors.append(string) # Add this string to the list of words to encode

# Create an instance of TfidfVectorizer
music_author_vectorizer = TfidfVectorizer()
x = music_author_vectorizer.fit_transform(list_of_authors) # Fit the vectorizer to the data
vectors = music_author_vectorizer.transform(list_of_authors) # Convert the list of strings to vectors
vectors_as_array = vectors.toarray() # Convert object to array

i = 0
for vector in vectors_as_array:
    df['musicMeta.musicAuthor'][i] = json.dumps(vector.tolist()) # Add vectors to dataframe
    i += 1

################################# END #################################

################################# ENCODE MUSIC NAME #################################
# Initialize a list of sounds
list_of_sounds = []

# Iterate through rows of the 'musicMeta.musicAuthor' column
for sound in df['musicMeta.musicName']:
    string = ''
    if type(sound) == str: # Ensure row has a sound
        string += sound # Append sound to string
    list_of_sounds.append(string) # Add this string to the list of words to encode

# Create an instance of TfidfVectorizer
sounds_vectorizer = TfidfVectorizer()
x = sounds_vectorizer.fit_transform(list_of_sounds) # Fit the vectorizer to the data
vectors = sounds_vectorizer.transform(list_of_sounds) # Convert the list of strings to vectors
vectors_as_array = vectors.toarray() # Convert object to array

i = 0
for vector in vectors_as_array:
    df['musicMeta.musicName'][i] = json.dumps(vector.tolist()) # Add vectors to dataframe
    i += 1

################################# END #################################

################################# ENCODE CAPTION #################################
# Initialize a list of captions
list_of_captions = []

# Iterate through rows of the 'text' column
for caption in df['text']:
    string = ''
    if type(caption) == str: # Ensure row has a caption
        string += caption # Append caption to string
    list_of_captions.append(string) # Add this string to the list of words to encode

# Create an instance of TfidfVectorizer
caption_vectorizer = TfidfVectorizer()
x = caption_vectorizer.fit_transform(list_of_captions) # Fit the vectorizer to the data
vectors = caption_vectorizer.transform(list_of_captions) # Convert the list of strings to vectors
vectors_as_array = vectors.toarray() # Convert object to array

i = 0
for vector in vectors_as_array:
    df['text'][i] = json.dumps(vector.tolist()) # Add vectors to dataframe
    i += 1

################################# END #################################

df.to_csv('../encoded_text.csv', index=False) # Save dataframe to csv


'''
TO CONVERT DATETIME STRINGS TO DATETIME OBJECTS:

from datetime import datetime

date_time_str = '18/09/19 01:55:19'

date_time_obj = datetime.strptime(date_time_str, '%d/%m/%y %H:%M:%S')


print "The type of the date is now",  type(date_time_obj)
print "The date is", date_time_obj
'''