#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 15 22:31:57 2018

@author: biglin
"""

import ClassifierLoader
from sklearn import ensemble

obj = ensemble.RandomForestClassifier()
obj1 = obj

def fitRandomForest(x_train, y_train):
    obj = fit(obj1, x_train, y_train )

def scoreRandomForest(x_test, y_test):
    score(obj, x_test, y_test)
    
def predictRandomForest(x_predict):
    yTarget = predictNaNx(obj, x_predict)
    return yTarget

def plotRandomForest(x_plot, y_plot):
    plot(obj, x_plot, y_plot, "RandomForest.jpg")