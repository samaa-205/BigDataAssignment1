import pandas as pd

from sklearn.preprocessing import MinMaxScaler
from sklearn.decomposition import PCA
from sklearn.preprocessing import KBinsDiscretizer

#Data Loading

file_path=input("enter path")

D=pd.read_csv(file_path)

#Data Cleaning

#D.isnull().sum()

D['Age'] = D['Age'].fillna(D['Age'].mean())
D['BPM'] = D['BPM'].fillna(D['BPM'].mean())

D['Music effects'] = D['Music effects'].fillna(D['Music effects'].mode().iloc[0])
D['Primary streaming service'] = D['Primary streaming service'].fillna(D['Primary streaming service'].mode().iloc[0])
D['While working'] = D['While working'].fillna(D['While working'].mode().iloc[0])
D['Instrumentalist'] = D['Instrumentalist'].fillna(D['Instrumentalist'].mode().iloc[0])
D['Composer'] = D['Composer'].fillna(D['Composer'].mode().iloc[0])
D['Foreign languages'] = D['Foreign languages'].fillna(D['Foreign languages'].mode().iloc[0])

#D.isnull().sum()

duplicates_count = D.duplicated().sum()
#print(f"Number of duplicates in the dataset: {duplicates_count}")

D['Timestamp'] = pd.to_datetime(D['Timestamp']) 

column_data_type = D['Timestamp'].dtype
#print(f"Data type of 'Date' column: {column_data_type}")

#Data Transformation

bin_edges = [0, 30, 40, 50, 100]   
bin_labels = ['<30', '30-40', '40-50', '50+']

D['age_group'] = pd.cut(D['Age'], bins=bin_edges, labels=bin_labels)

scaler = MinMaxScaler(feature_range=(-1, 1)) 
D['BPM_scaled'] = scaler.fit_transform(D[['BPM']])

#Dimensionality Reduction

pca = PCA(n_components=1)
D['BPM_pca'] = pca.fit_transform(D[['BPM_scaled']])

#D

#Data Reduction
#Data Cube Aggregation  

#aggregated_data = D.groupby('Primary streaming service').value_counts()  --solving error--

#print(aggregated_data)

# Data Discretization

#Applying Equal Width Discretization on the 'Income' column
D['Depression_Width_Bin'] = pd.cut(D['Depression'], bins=3, labels=["Low", "Medium", "High"])

#Applying Equal Frequency Discretization on the 'Hours per day' column
est = KBinsDiscretizer(n_bins=3, encode='ordinal', strategy='quantile')

D['Hours_per_day_Equal_Freq_Bin'] = est.fit_transform(D[['Hours per day']])
D.to_csv('res_dpre.csv', index=False)

print('Finish')