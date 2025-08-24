# Important Libraries

import pandas as pd
import numpy as np
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score,confusion_matrix
# Importing Data

data_income = pd.read_csv('income.csv')

#creating copy

data = data_income.copy()
# getting to know data
#to check variables data type

print(data.info())
#missing values
data.isnull()
print('Data column with null value:\n',data.isnull().sum())
summary_num= data.describe()
print(summary_num)
# summary of categorial variable

summary_cate=data.describe(include = "object")
print(summary_cate)
# freq. of each category

data['JobType'].value_counts()
data['occupation'].value_counts()
# freq. of each category

data['JobType'].value_counts()
data['occupation'].value_counts()
data = pd.read_csv('income.csv',na_values=[" ?"])
# Data Pre Processing
data.isnull().sum()

missing=data[data.isnull().any(axis=1)]
data2=data.dropna(axis=0)
data2=data.dropna(axis=0)
data2.columns
gender_salstat= pd.crosstab(index = data2 ["gender"],
                     columns = data2 ["SalStat"],
                     margins = True,
                     normalize = 'index')
print(gender_salstat)
# frequency distribution of salary status

SalStat = sns.countplot(data2['SalStat'])
# BoxPlot & Histogram
sns.displot(data2['age'],bins=10,kde=False)
sns.boxplot(x='SalStat',y='age', data=data2)
data2.groupby('SalStat')['age'].median   




