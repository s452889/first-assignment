import pandas as pd
import numpy as np
# set option to see every column
pd.set_option('display.max_columns', None)
# data frame object
# name the columns (names)
train = pd.read_csv("./train.tsv", sep='\t',
                    names=["Price", "Rooms", "Meters2", "Floor", "Address", "Description"])
description = pd.read_csv("./description.csv")
# rename column header
description.rename(columns={'liczba': 'Rooms'}, inplace=True)
# merge frames
# I used 'how=left' to show also NaN values
merge_script = train.merge(description, on="Rooms", how="left")
# export to csv file
merge_script.to_csv('out2.csv', index=False)