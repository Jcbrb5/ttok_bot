import numpy as np
import pandas as pd
from pandas.io import json

def clean_hashtags():
    df = pd.read_csv('../data_with_less_cols.csv') # Import the data from csv

    for index in range(len(df['hashtags'])): # For each row of the hashtags column in the dataframe
        tags = [] # Initialize an empty array of hashtags
        tags_json = json.loads(df['hashtags'][index]) # Convert string to JSON
        if len(tags_json) > 0: # if the length of the JSON array is not empty
            for data in tags_json: # For each hashtag
                tags.append(data['name']) # Append the hashtag to tags
            df['hashtags'][index] = tags # Set the current index of the hashtags colunm in the dataframe equal to tags

    df.to_csv('../clean_hashtags.csv', index=False) # Save the data to a csv