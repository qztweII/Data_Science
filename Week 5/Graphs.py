import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

df = pd.read_csv("athlete_events_cleaned.csv")

df['Weight'].plot(kind='hist', bins=10, title='Distribution of Athlete Weights') #bin changes how many bars to show on the histogram. The smaller the number, the wider the bars. 
plt.xlabel('Weight')
plt.ylabel('Frequency')
plt.tight_layout()
plt.savefig("Amazing_pictures/weight_distribution_2.png") #The graph is skewed
plt.show()
