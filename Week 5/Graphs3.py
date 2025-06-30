import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

df = pd.read_csv("athlete_events_cleaned.csv")
medal_counts = df[df['Medal'] != 'None']['Medal'].value_counts()

medal_counts.plot(kind='pie', autopct='%1.1f%%', title='Distribution of Medal Types')
plt.ylabel('')  # Removes default y-axis label
plt.tight_layout()
plt.savefig("Amazing_pictures/medal_pie_chart.png")
plt.show()