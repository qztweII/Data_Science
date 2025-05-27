import pandas as pd

df = pd.read_csv("athlete_events.csv")

print(df['Sport'].value_counts().head()) #The top 5 sports were: Athletics, Gymnastics, Swimming, Shooting, Cycling
print(df['Sex'].value_counts())          #There are 2.638 times more males than females in the olympics (3 d.p.). 
print(df.describe())                     #Average age: 25 years old, oldest: 97 years, youngest: 10 years

print(df['NOC'].nunique())
print(df['NOC'].unique())

print(df.sample(n=10))
print(df.query("Medal.str.startswith('Gold')"))
#Country codes:
#URS = USSR
#GDR = East Germany
#FRG = West Germany