# Script number 6

import pandas as pd
import numpy as np

# Read in data from csv
df = pd.read_csv('../encoded_text.csv')

i = 0
for item in df['musicMeta.musicOriginal']:
    if item:
        df['musicMeta.musicOriginal'][i] = 1
    else:
        df['musicMeta.musicOriginal'][i] = 0
    i += 1

df.to_csv('../preprocessed_data.csv', index=False)
