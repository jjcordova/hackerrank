# Excersice HackerRank
# Artificial IntelligenceStatistics and Machine LearningDay 6: Multiple Linear Regression: Predicting House Prices
# https://www.hackerrank.com/challenges/battery/problem
# Laptop Battery Life

#!/bin/python3

import math
import os
import random
import re
import sys
import pandas as pd
from sklearn import linear_model



if __name__ == '__main__':
    # Set dataset to training
    #dataset = pd.read_csv('https://s3.amazonaws.com/hr-testcases/399/assets/trainingdata.txt', header=None)
    dataset = pd.read_csv('trainingdata.txt', header=None)
    dataset = dataset[dataset.iloc[:,1] < 8]
    # Add bias
    dataset.insert(0, len(dataset.columns), 0)
    
    # Separe variables dependet and independent
    X = dataset.iloc[:,0:2]
    Y = dataset.iloc[:,2]
    
    # Create the classifier model
    model = linear_model.LinearRegression()
    model.fit(X, Y)
    timeCharged = float(input().strip())
    result = model.predict([[0,timeCharged]])
    if result[0] > 8:
        print(8.0)
    else:
        print(round(result[0],2))
