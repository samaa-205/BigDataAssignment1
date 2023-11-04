
import pandas as pd
from sklearn.cluster import KMeans

file_path=input("enter path")

D_new=pd.read_csv(file_path)

#D_new

columns_to_drop = ['Primary streaming service','Timestamp','age_group' ,'While working', 'Instrumentalist', 'Composer', 'Fav genre', 'Exploratory', 'Foreign languages', 'Frequency [Classical]', 'Frequency [Country]', 'Frequency [EDM]', 'Frequency [Folk]', 'Frequency [Gospel]', 'Frequency [Hip hop]', 'Frequency [Jazz]', 'Frequency [K pop]', 'Frequency [Latin]', 'Frequency [Lofi]', 'Frequency [Metal]', 'Frequency [Pop]', 'Frequency [R&B]', 'Frequency [Rap]', 'Frequency [Rock]', 'Frequency [Video game music]', 'Music effects', 'Permissions', 'Depression_Width_Bin']
D_new.drop(columns_to_drop, axis=1, inplace=True)

#D_new

k = 3  # Number of clusters
kmeans = KMeans(n_clusters=k, random_state=0)
D_new['cluster'] = kmeans.fit_predict(D_new)

cluster_counts = D_new['cluster'].value_counts().sort_index()

with open('k.txt', 'w') as file:
    for cluster, count in enumerate(cluster_counts):
        file.write(f'Cluster {cluster}: {count} records\n')

print("Done")

