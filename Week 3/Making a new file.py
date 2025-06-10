import pandas as pd

data_path = "athlete_events.csv"

df = pd.read_csv(data_path)
print(df.head())