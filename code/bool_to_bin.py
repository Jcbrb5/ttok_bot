import pandas as pd
import numpy as np

def bool_to_bin():
    # Read in data from csv
    df = pd.read_csv('../preprocessed_data_with_metric.csv')

    df['musicMeta.musicOriginal'] = df['musicMeta.musicOriginal'] * 1 # Convert boolean values to binary (1 = True , 0 = False)

    df.to_csv('../final_preprocessed_data.csv', index=False) # Save data to csv