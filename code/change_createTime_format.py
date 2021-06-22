# Data processing script number 2

import numpy as np
from datetime import datetime
import pandas as pd

df = pd.read_csv("../out.csv")

for index in range(len(df["createTime"])):
    df["createTime"][index] = datetime.fromtimestamp(index)

df.to_csv("../data_with_readable_timestamps.csv", index=False)