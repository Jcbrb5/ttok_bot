import numpy as np
import pandas as pd
import math

def calculate_engagement_metric():
    # Read in data from csv
    df = pd.read_csv('../encoded_text.csv')

    list_of_engagement = [] # Initialize empty list of engagement metrics

    for i in range(len(df)): # For each row of the dataframe]
        # Calculate the engagement metric and append it onto list_of_engagement
        list_of_engagement.append(math.log10(df['shareCount'][i] * 0.4 + df['commentCount'][i] * 0.3 + df['diggCount'][i] * 0.2 \
            + df['playCount'][i] * 0.1))

    df['engagementMetric'] = list_of_engagement # Make a new column in the dataframe to store list_of_engagement

    df = df.drop(['diggCount', 'shareCount', 'playCount', 'commentCount'], axis=1) # Remove unneccessary columns

    df.to_csv('../preprocessed_data_with_metric.csv', index=False) # Save the data to a csv