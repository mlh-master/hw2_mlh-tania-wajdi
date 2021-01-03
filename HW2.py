# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.7.1
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# imports
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split


# 1
# Data Loading & Preprocessing
T1D_data = pd.read_csv('HW2_data.csv')
T1D_data.dropna(inplace=True)

#2
# Data Split
x_cols = ['Age','Gender','Increased Urination','Increased Thirst','Sudden Weight Loss','Weakness','Increased Hunger','Genital Thrush','Visual Blurring','Itching','Irritability','Delayed Healing','Partial Paresis','Muscle Stiffness','Hair Loss','Obesity','Family History']
X = T1D_data[x_cols]
y = T1D_data['Diagnosis']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=10, stratify=y)

#3
# a
col_YN = ['Increased Urination','Increased Thirst','Sudden Weight Loss','Weakness','Increased Hunger','Genital Thrush','Visual Blurring','Itching','Irritability','Delayed Healing','Partial Paresis','Muscle Stiffness','Hair Loss','Obesity']
# col1 = ['Age','Gender','Increased Urination','Increased Thirst','Sudden Weight Loss','Weakness','Increased Hunger','Genital Thrush','Visual Blurring','Itching','Irritability','Delayed Healing','Partial Paresis','Muscle Stiffness','Hair Loss','Obesity','Diagnosis','Family History']
col1 = col_YN +['Gender','Family History','Diagnosis']
col2 = [0]*len(col_YN)
for i,feature in enumerate(col_YN):
    col2[i] = (X_train[feature].value_counts(normalize=True)['Yes'])*100
col2+=[(X_train['Gender'].value_counts(normalize=True)['Female'])*100] #In 'Gender' we chose Female as positive feature for comparison
col2+=[(X_train['Family History'].value_counts(normalize=True)[1])*100] #in 'Family History' we chose 1 as positive feature for comparison
col2+=[(y_train.value_counts(normalize=True)['Positive'])*100] #in 'Diagnosis' we chose 'Positive' as positive feature for comparison
col3 = [0]*len(col_YN)
for i,feature in enumerate(col_YN):
    col3[i] = (X_test[feature].value_counts(normalize=True)['Yes'])*100
col3+=[(X_test['Gender'].value_counts(normalize=True)['Female'])*100] #In 'Gender' we chose Female as positive feature for comparison
col3+=[(X_test['Family History'].value_counts(normalize=True)[1])*100] #in 'Family History' we chose 1 as positive feature for comparison
col3+=[(y_test.value_counts(normalize=True)['Positive'])*100] #in 'Diagnosis' we chose 'Positive' as positive feature for comparison
col4 = [0]*len(col3)
for i in range(len(col4)):
    col4[i]=col2[i]-col3[i]

#4 One Hot Vectors
T1D_data_h =T1D_data.iloc[:,1:]
T1D_data_h = T1D_data_h.replace('Yes',1).replace('No',0).replace('Male',0).replace('Female',1).replace('Negative',0).replace('Positive',1)
x_cols_h = ['Gender','Increased Urination','Increased Thirst','Sudden Weight Loss','Weakness','Increased Hunger','Genital Thrush','Visual Blurring','Itching','Irritability','Delayed Healing','Partial Paresis','Muscle Stiffness','Hair Loss','Obesity','Family History']
X_h = T1D_data_h[x_cols_h]
y_h = T1D_data_h['Diagnosis']
X_train_h, X_test_h, y_train_h, y_test_h= train_test_split(X_h, y_h, test_size=0.2, random_state=10, stratify=y)
features_vec = list(X_train_h.keys()) #without 'age' (numerical) and 'Diagnosis' (the label)
X_train_h = X_train_h.values
X_test_h = X_test_h.values
y_train_h = y_train_h.values
y_test_h = y_test_h.

#5
# x_cols_h = ['Gender','Increased Urination','Increased Thirst','Sudden Weight Loss','Weakness','Increased Hunger','Genital Thrush','Visual Blurring','Itching','Irritability','Delayed Healing','Partial Paresis','Muscle Stiffness','Hair Loss','Obesity','Family History']
# X_h = T1D_data_hot[x_cols_h]
# y_h = T1D_data_hot['Diagnosis']
# X_train_h, X_test_h, y_train_h, y_test_h = train_test_split(X_h, y_h, test_size=0.2, random_state=10, stratify=y)


x=7
