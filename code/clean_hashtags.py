import numpy as np
import pandas as pd
from pandas.io import json

df = pd.read_csv('../data_with_less_cols.csv')

for index in range(len(df['hashtags'])):
    tags = []
    tags_json = json.loads(df['hashtags'][index])
    if len(tags_json) > 0:
        for data in tags_json:
            tags.append(data['name'])
        df['hashtags'][index] = tags

df.to_csv('../clean_hashtags.csv', index=False)