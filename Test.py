# -*- coding: utf-8 -*-
"""
Created on Fri Mar 28 17:36:34 2025

@author: Rouzbeh
"""
import pandas as pd
df = pd.read_csv(r'C:\Users\Rouzbeh\Desktop\sample_ecommerce_data.csv')

# Fill numeric columns with their mean
df.fillna(df.mean(numeric_only=True), inplace=True)

print("DataFrame After Replacing Null Values with Mean:")
print(df.isnull().sum())
print(df.head())