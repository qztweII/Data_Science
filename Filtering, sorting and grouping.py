import pandas as pd

df = pd.read_csv("athlete_events.csv")

# Combined filter for Aussie swimmers
aus_swimmers = df[(df['NOC'] == 'AUS') & (df["Sport"] == 'Swimming')].head(10)
print(aus_swimmers)

#Filter by height then weight
sorted_by_height = df.sort_values(by=["Height", "Weight"], ascending=False)
print(sorted_by_height[["Name", "Height", "Weight", "Sex"]].head(30))

#Weight by sport
heavy_sports = df.groupby("Weight")["Sport"].mean().sort_values(ascending=False)
print(heavy_sports.head())