# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 13:54:38 2019

@author: Black
"""
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#Import the dataset 
dataset = pd.read_csv('./dataset/Data.csv')
dataset.hist(bins =10)
plt.show()
x = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 3].values

from sklearn.preprocessing import Imputer
imputer = Imputer()
