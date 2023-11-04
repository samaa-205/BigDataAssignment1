import matplotlib.pyplot as plt
import pandas as pd

file_path = input("enter path")

D_new= pd.read_csv(file_path)

#Create a bar plot based on age_group and Primary streaming service columns
plt.figure(figsize=(8, 6))
D_new.groupby(['age_group', 'Primary streaming service']).size().unstack().plot(kind='bar', stacked=True)
plt.title('Visualization of Primary Streaming Service by Age Group')
plt.xlabel('Age Group')
plt.ylabel('Count of Primary Streaming Service')

#Saving the plot as an image
plt.savefig('vis.png')

print("Done")