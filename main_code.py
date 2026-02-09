import pandas as pd
import numpy as np
DATA_PATH = "data/courbes_fictives_30min.csv"
COL_PDL = "pdl_id"
COL_DT = "datetime"
COL_PWR = "p_kw"
df = pd.read_csv(DATA_PATH, parse_dates=[COL_DT])
df.head()