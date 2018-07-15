#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 15 22:17:41 2018

@author: biglin
"""

import ClassifierLoader
from sklearn import svm

obj = svm.SVC(kernel='poly')
obj1 = obj

def fitPolyKernelSVM(x_train, y_train):
    obj = fit(obj1, x_train, y_train )

def scorePolyKernelSVM(x_test, y_test):
    score(obj, x_test, y_test)
    
def predictPolyKernelSVM(x_predict):
    yTarget = predictNaNx(obj, x_predict)
    return yTarget

def plotPolyKernelSVM(x_plot, y_plot):
    plot(obj, x_plot, y_plot, "PolyKernelSVM.jpg")
    
