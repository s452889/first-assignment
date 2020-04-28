import pandas as pd
import numpy as np
import matplotlib.pylab as plt
import math as math
pd.set_option("display.max_colwidth", None)
df = pd.read_csv(r"./train.tsv", sep='\t', names=["Price", "Rooms", "Area",
                                                 "Floor", "Address",
                                                 "Description"], usecols=["Description"])
print(df)