import pandas as pd
import numpy as np
# data frame object
# name the columns (names)
df = pd.read_csv("./train.tsv",
                 sep='\t',
                 names=["Price", "Rooms",
                        "Meters2", "Floor", "Address",
                        "Description"])
# price of flats (mean)
price_mean = round(df.Price.mean(), 2)
# create array and data series
data = np.array([price_mean])
series = pd.Series(data)
# export to csv file
series.to_csv("out0.csv", index=False, header=False)