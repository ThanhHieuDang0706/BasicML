from sklearn.datasets import load_iris
from sklearn import tree

import numpy as np
import pandas as pd

csv_filename = 'TitanicPreprocessed.csv'
db = pd.read_csv(csv_filename)

# print(db)