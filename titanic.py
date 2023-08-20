import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

train_dataset=pd.read_csv('D:/Desktop/coding/ml/titanic_survival/titanic.csv')

#print(train_dataset.head())

#print(train_dataset.info())

#print(train_dataset.describe())

#print(train_dataset['Pclass'].value_counts())

print(train_dataset[['Survived','Sex']].groupby('Sex').mean())