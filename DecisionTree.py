#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 15 22:26:35 2018

@author: biglin
"""

import ClassifierLoader
from sklearn import tree

obj = tree.DecisionTreeClassifier()
obj1 = obj

def fitDecisionTree(x_train, y_train):
    obj = fit(obj1, x_train, y_train )

def scoreDecisionTree(x_test, y_test):
    score(obj, x_test, y_test)
    
def predictDecisionTree(x_predict):
    yTarget = predictNaNx(obj, x_predict)
    return yTarget

def plotDecisionTree(x_plot, y_plot):
    plot(obj, x_plot, y_plot, "DecisionTree.jpg")
    