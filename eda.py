import pandas as pd

file_path = input("enter path")

D_new = pd.read_csv(file_path)

# Insight 1
hours_per_day_counts = D_new['Hours per day'].value_counts()
insight_1 = f"A significant percentage of the surveyed individuals reported listening to music for hours per day. \n{hours_per_day_counts}"

# Insight 2
music_genres = ['Rock', 'Video game music','Jazz','R&B','Pop','Rap','Classical', 'Hip hop']
frequencies = [D_new[f'Frequency [{genre}]'].value_counts() for genre in music_genres]
insight_2 = f"A considerable number of respondents indicated that they frequently listen to different types of music  music Rock, Video game music,Jazz,R&B,Pop,Rap,Classical, Hip hop . \n{frequencies}"

#Insight 3
mental_health_columns = ['Anxiety', 'Depression', 'Insomnia', 'OCD']
occurrences = {column: D_new[column].value_counts() for column in mental_health_columns}
insight_3 = f"The columns related to mental health indicate a willingness of respondents to disclose information about their mental well-being. \n{occurrences}"

# Save insights to text files
with open('eda_insight_1.txt', 'w') as file:
    file.write(insight_1)

with open('eda_insight_2.txt', 'w') as file:
    file.write(insight_2)

with open('eda_insight_3.txt', 'w') as file:
    file.write(insight_3)

print("Done")