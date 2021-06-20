from numpy.lib.function_base import vectorize
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
import pandas as pd
import ast

df = pd.read_csv('../encoded_hashtags.csv')

print(df['encoded_hashtags'][4])