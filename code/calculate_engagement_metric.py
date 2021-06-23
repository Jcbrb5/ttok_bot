# Script number 6

import numpy as np
import pandas as pd
import math

# Read in data from csv
df = pd.read_csv('../encoded_text.csv')

list_of_engagement = []

for i in range(len(df)):
    list_of_engagement.append(math.log10(df['shareCount'][i] * 0.4 + df['commentCount'][i] * 0.3 + df['diggCount'][i] * 0.2 + df['playCount'][i] * 0.1))

df['engagementMetric'] = list_of_engagement

df.to_csv('../preprocessed_data_with_metric.csv', index=False)