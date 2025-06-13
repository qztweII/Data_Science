import pandas as pd

df = pd.read_csv("athlete_events.csv")

df_cleaned = df.dropna(subset=['Height', 'Weight'])
print(df_cleaned.shape)