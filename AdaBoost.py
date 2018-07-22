fit#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 15 22:41:20 2018

@author: biglin
"""

import ClassifierLoader
from sklearn import ensemble

obj = ensemble.AdaBoostClassifier()
obj1 = obj

def fitAdaBoost(x_train, y_train):
    obj = fit(obj1, x_train, y_train )
    return obj

def scoreAdaBoost(x_test, y_test):
    output = score(obj, x_test, y_test)
    return output
    
def predictAdaBoost(x_predict):
    yTarget = predictNaNx(obj, x_predict)
    return yTarget

def testAdaBoost(x_train, y_train, x_test, y_test):
    output = testing(obj, x_train, y_train, x_test, y_test)
    return output

def fittingGraphAdaBoost(data):
    output = fitting(obj, data, 'fitting-AdaBoost')
    return output

def crossValAdaBoost(x_train, y_train, iterable):
    output = crossVal(obj, x_train, y_train, iterable, 'crossVal-AdaBoost')
    return output

def handOutAdaBoost(x_train, y_train):
    output = handOut(obj, x_train, y_train)
    return output

def confusionMatrixAdaBoost(x_train, y_train, x_test, y_test):
    output = confusionMatrix(obj, x_train, y_train, x_test, y_test)
    return output

def plotAdaBoost(x_plot, y_plot):
    plot(obj, x_plot, y_plot, "AdaBoosts")