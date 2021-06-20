import ast
import json
from numpy.lib.function_base import vectorize
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
import pandas as pd

df = pd.read_csv('../clean_hashtags.csv')

words_to_vectorize = []
for item in df['hashtags']:
    item = ast.literal_eval(item)
    string = ''
    if len(item) > 0:
        for word in item:
            string += word + ' '
        string = string[:-1]
    words_to_vectorize.append(string)

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(words_to_vectorize)
vectors = vectorizer.transform(words_to_vectorize)
vectors_as_array = vectors.toarray()

arr = []
for n in range(341):
    arr.append([])

df['encoded_hashtags'] = arr

i = 0
for vector in vectors_as_array:
    df['encoded_hashtags'][i] = json.dumps(vector.tolist())
    i += 1

print(type(df['encoded_hashtags'][4][0]))
# print(df['encoded_hashtags'])

df.to_csv('../encoded_hashtags.csv', index=False)