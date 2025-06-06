# Pandas Reference Sheet

Import Pandas
> `import pandas as pd`

Read a csv
> `df = pd.read_csv("data.csv")`

Print the first five rows
> `print(df.head)`

Print the columns
> `print(df.columns)`

Sorts and counts how many categories are found in the rows, each having the number of rows within its category. 
> `df["group"].value_counts()`

Gives the average, median, standard deviation, smallest, 25th percentile, 75th percentile and largest value. 
> `df.describe()`

How many unique items there are within that column
> `df.["group"].nunique`