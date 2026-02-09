import pandas as pd
import numpy as np
DATA_PATH = "export.csv"
COL_PDL = "ID"
COL_DT = "horodate"
COL_PWR = "vale"
df = pd.read_csv(DATA_PATH, parse_dates=[COL_DT])
df.head()