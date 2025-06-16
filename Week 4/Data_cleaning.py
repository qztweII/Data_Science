import pandas as pd

df = pd.read_csv("athlete_events.csv")

print(df.isnull().sum())

df_cleaned = df.dropna(subset=['Height', 'Weight'])
print(df_cleaned.shape)

# Fill missing medals with 'None'
df_cleaned.loc[:, 'Medal'] = df_cleaned['Medal'].fillna('None')

# Fill missing ages with average age
avg_age = df_cleaned['Age'].mean()
df_cleaned.loc[:, 'Age'] = df_cleaned['Age'].fillna(avg_age)

print(df_cleaned.head())

print(df_cleaned.isnull().sum())

print(df_cleaned.describe())

df_cleaned.to_csv("athlete_events_cleaned.csv", index=False)