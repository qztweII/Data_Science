import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

df = pd.read_csv("athlete_events_cleaned.csv")
median_age = df.groupby('Year')['Age'].median()

#median_age.plot(kind='scatter', title='Median Athlete Age Over Time')
plt.scatter(median_age, df.groupby("Year"))
plt.xlabel('Olympic Year')
plt.ylabel('Median Age')
plt.grid(True)
plt.tight_layout()
plt.savefig("Amazing_pictures/median_age_line.png") #You'd notice over the years, the athletes start get older. This is because of better sports medicine, training and recovery techniques, allowing athletes to stay in olympics for longer. 
plt.show()