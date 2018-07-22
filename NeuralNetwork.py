#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 15 22:36:27 2018

@author: biglin
"""

import ClassifierLoader
from sklearn import neural_network

obj = neural_network.MLPClassifier()
obj1 = obj

def fitNeuralNetwork(x_train, y_train):
    obj = fit(obj1, x_train, y_train )

def scoreNeuralNetwork(x_test, y_test):
    output = score(obj, x_test, y_test)
    return output
    
def predictNeuralNetwork(x_predict):
    yTarget = predictNaNx(obj, x_predict)
    return yTarget

def testNeuralNetwork(x_train, y_train, x_test, y_test):
    output = testing(obj, x_train, y_train, x_test, y_test)
    return output

def fittingGraphNeuralNetwork(data):
    output = fitting(obj, data, 'fitting-NeuralNetwork')
    return output

def crossValNeuralNetwork(x_train, y_train, iterable):
    output = crossVal(obj, x_train, y_train, iterable)
    return output

def handOutNeuralNetwork(x_train, y_train):
    output = handOut(obj, x_train, y_train)
    return output

def confusionMatrixNeuralNetwork(x_train, y_train, x_test, y_test):
    output = confusionMatrix(obj, x_train, y_train, x_test, y_test)
    return output

def plotNeuralNetwork(x_plot, y_plot):
    plot(obj, x_plot, y_plot, "NeuralNetwork")