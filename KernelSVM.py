#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 15 22:08:52 2018

@author: biglin
"""

import ClassifierLoader
from sklearn import svm

obj = svm.SVC()
obj1 = obj

def fitKernelSVM(x_train, y_train):
    obj = fit(obj1, x_train, y_train )

def scoreKernelSVM(x_test, y_test):
    score(obj, x_test, y_test)
    
def predictKernelSVM(x_predict):
    yTarget = predictNaNx(obj, x_predict)
    return yTarget

def testKernelSVM(x_train, y_train, x_test, y_test):
    testing(obj, x_train, y_train, x_test, y_test)

def crossValKernelSVM(x_train, y_train, iterable):
    output = crossVal(obj, x_train, y_train, iterable)
    return output

def plotKernelSVM(x_plot, y_plot):
    plot(obj, x_plot, y_plot, "KernelSVM.jpg")