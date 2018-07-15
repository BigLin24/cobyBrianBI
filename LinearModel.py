#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 15 22:52:10 2018

@author: biglin
"""

import ClassifierLoader
from sklearn import linear_model

obj = linear_model.LinearRegression()
obj1 = obj

def fitLinearModel(x_train, y_train):
    obj = fit(obj1, x_train, y_train )

def scoreLinearModel(x_test, y_test):
    score(obj, x_test, y_test)
    
def predictLinearModel(x_predict):
    yTarget = predictNaNx(obj, x_predict)
    return yTarget

def plotLinearModel(x_plot, y_plot):
    plot(obj, x_plot, y_plot, "LinearModel")