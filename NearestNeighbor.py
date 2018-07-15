#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 15 20:02:15 2018

@author: biglin
"""
import numpy as np
import pylab as pl
import time
import plotter


from matplotlib import colors
from sklearn import neighbors

nb = neighbors.KNeighborsClassifier()


def fitNearestNeighbors(x_train, y_train):
    nb.fit(x_train, y_train)
    print("Finish Nornal Network: nn")

def scoreNearestNeighbors(x_test, y_test):
    print("Nearest Neighbors Score: " + str(nb.score(x_test, y_test)))
    
def predictNearestNeighbors(x_predict):
    yTarget = nb.predict(x_predict)
    return yTarget

def plotNearestNeighbors(x_plot, y_plot):
    X = prepareData(x_plot)
    nb.fit(X, y_plot)
    plotIt(nb, X, y_plot, "NearestNeighbors.jpg")

