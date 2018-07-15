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
    score(obj, x_test, y_test)
    
def predictNeuralNetwork(x_predict):
    yTarget = predictNaNx(obj, x_predict)
    return yTarget

def plotNeuralNetwork(x_plot, y_plot):
    plot(obj, x_plot, y_plot, "NeuralNetwork")