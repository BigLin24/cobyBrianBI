#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 15 21:27:14 2018

@author: biglin
"""

import ClassifierLoader
from sklearn import svm

obj = svm.LinearSVC()
obj1 = obj

def fitLinearSVM(x_train, y_train):
    obj = fit(obj1, x_train, y_train )
    return obj

def scoreLinearSVM(x_test, y_test):
    score(obj, x_test, y_test)
    
def predictLinearSVM(x_predict):
    yTarget = predictNaNx(obj, x_predict)
    return yTarget

def testLinearSVM(x_train, y_train, x_test, y_test):
    testing(obj, x_train, y_train, x_test, y_test)

def plotLinearSVM(x_plot, y_plot):
    plot(obj, x_plot, y_plot, "LinearSVM")
