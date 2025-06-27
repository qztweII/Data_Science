import pandas as pd
import matplotlib as plt

df = pd.read_csv("Athlete_events_cleaned.csv")

df['Weight'].plot(kind='hist', bins=30, title='Distribution of Athlete Weights')
plt.xlabel('Weight')
plt.ylabel('Frequency')
plt.tight_layout()
plt.savefig("weight_distribution.png")
plt.show()