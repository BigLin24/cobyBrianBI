#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 15 21:24:38 2018

@author: biglin
"""

import numpy as np
import pylab as pl
import time
import plotter

from matplotlib import colors

def fit(obj, x_train, y_train):
    start_time = time.time()
    obj.fit(x_train, y_train)
    print("Finish")
    print("--- %s seconds ---" % (time.time() - start_time))
    return obj

def score(obj, x_test, y_test):
    print("Score: " + str(obj.score(x_test, y_test)))
    
def predictNaNx(obj, x_predict):
    yTarget = obj.predict(x_predict)
    return yTarget

def plot(obj, x_plot, y_plot, filename):
    X = prepareData(x_plot)
    obj.fit(X, y_plot)
    plotIt(obj, X, y_plot, filename + ".jpg")
    
