import pandas as pd

# data frame object
# name the columns (names)
df = pd.read_csv("./train.tsv",
                 sep='\t',
                 names=["Price", "Rooms",
                        "Meters2", "Floor", "Address",
                        "Description"])
# new column Price per meter
df["Price per meter"] = df.Price / df.Meters2
# conditions
rooms_condition = df["Rooms"] >= 3
PPM_condition = df["Price per meter"] < df["Price per meter"].mean()
# the result
result = df[rooms_condition & PPM_condition]
# export to csv file
result.to_csv('out1.csv', index=False,
              header=False, columns=["Rooms", "Price",
                                     "Price per meter"])
