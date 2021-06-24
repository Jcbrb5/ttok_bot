import pandas as pd
import numpy as np

def bool_to_bin():
    # Read in data from csv
    df = pd.read_csv('../preprocessed_data_with_metric.csv')

    # i = 0
    # for item in df['musicMeta.musicOriginal']:
    #     if item is True:
    #         print("hello")
    #         df['musicMeta.musicOriginal'][i] = 1
    #     else:
    #         df['musicMeta.musicOriginal'][i] = 0
    #     i += 1

    df['musicMeta.musicOriginal'] = df['musicMeta.musicOriginal'] * 1

    df.to_csv('../final_preprocessed_data.csv', index=False)