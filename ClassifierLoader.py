#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 15 21:24:38 2018

@author: Daniel K.
"""

import numpy as np
import pylab as pl
import time
import plotter

from matplotlib import colors
from sklearn.model_selection import cross_val_score

def fit(obj, x_train, y_train):
    start_time = time.time()
    obj.fit(x_train, y_train)
    #print("Finish")
    #print("--- %s seconds ---" % (time.time() - start_time))
    return obj

def score(obj, x_test, y_test):
    #print("Score: " + str(obj.score(x_test, y_test)))
    return obj.score(x_test, y_test)

def predictNaNx(obj, x_predict):
    yTarget = obj.predict(x_predict)
    return yTarget

def plot(obj, x_plot, y_plot, filename):
    X = prepareData(x_plot)
    obj.fit(X, y_plot)
    plotIt(obj, X, y_plot, filename + ".jpg")

def crossVal(obj, x_train, y_train, iterable):
    output = cross_val_score(obj, x_train, y_train, cv=iterable)
    return output

def testing(obj, x_train, y_train, nichtsX, nichtsY):
    obj1 = fit(obj, x_train, y_train)
    
    xTrain, xTest = np.split(x_train, 2)
    yTrain, yTest = np.split(y_train, 2)


    obj1 = fit(obj, xTrain, yTrain)
    yTargetTrain = obj1.predict(xTrain)
    yTarget = obj1.predict(xTest)
    
    
    i = 0
    n = 0
    m = 0
    
    while i < len(yTest):
        if yTest[i]== yTarget[i]:
            n = n + 1
            
        if yTargetTrain[i] == yTrain[i]:
            m = m +1
            
        i = i + 1
    
    holdout = n / i
    training = m / i

    return holdout, training

"""
def testing(obj, x_train, y_train, x_test, y_test):
    obj1 = fit(obj, x_train, y_train)
    scoreRes = score(obj1, x_test, y_test)
    handoutRes = handOut(obj1, x_train, y_train)
    return scoreRes, handoutRes"""