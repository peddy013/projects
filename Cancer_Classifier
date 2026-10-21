import pandas as pd
from sklearn.datasets import load_breast_cancer
cancer_data = load_breast_cancer(as_frame = True)
#print(type(cancer_data))
cancer_df = cancer_data.data
print(type(cancer_df))
cancer_df['target'] = cancer_data.target
print(cancer_df.head())#Look at the first few observations in the dataset.
print(cancer_df.tail())#Look at the last few observations in the dataset.
print(cancer_df.shape)#this print the shape of database

print(cancer_df.isna().sum())#Calculate and print the number of missing values in each column
print(cancer_df["target"].value_counts())

print(cancer_df.describe())#dataset summary
