#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 15 22:48:17 2018

@author: biglin
"""


import ClassifierLoader
from sklearn import naive_bayes

obj = naive_bayes.GaussianNB()
obj1 = obj

def fitNaiveBayes(x_train, y_train):
    obj = fit(obj1, x_train, y_train )

def scoreNaiveBayes(x_test, y_test):
    score(obj, x_test, y_test)
    
def predictNaiveBayes(x_predict):
    yTarget = predictNaNx(obj, x_predict)
    return yTarget

def testNaiveBayes(x_train, y_train, x_test, y_test):
    testing(obj, x_train, y_train, x_test, y_test)

def plotNaiveBayes(x_plot, y_plot):
    plot(obj, x_plot, y_plot, "NaiveBayes")