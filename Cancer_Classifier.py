import pandas as pd
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
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

#preparing the data into training Set and test Set

cancer_df['target'] = cancer_data.target
X = cancer_df.drop(['target'],axis=1)
Y = cancer_df['target']
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.15,random_state=417)
