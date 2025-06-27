import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

df = pd.read_csv("athlete_events_cleaned.csv")

df['Weight'].plot(kind='hist', bins=10, title='Distribution of Athlete Weights')
plt.xlabel('Weight')
plt.ylabel('Frequency')
plt.tight_layout()
plt.savefig("Amazing_pictures/weight_distribution_2.png")
plt.show()
