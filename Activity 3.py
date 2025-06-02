import pandas as pd

df = pd.read_csv("athlete_events.csv")

# Combined filter for Aussie swimmers
aus_swimmers = df[(df['NOC'] == 'AUS') & (df["Sport"] == 'Swimming').head()]
print(aus_swimmers)

#Filter by height then weight
sorted_by_height = df.sort_values(by="Height", ascending=False)
print(sorted_by_height[["Name", "Height", "Weight"]].head(20))