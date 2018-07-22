#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 15 21:24:38 2018

@author: Daniel K.
"""

import numpy as np
import pylab as pl
import time
import plotter

from matplotlib import colors
from sklearn.model_selection import cross_val_score
from sklearn import metrics

def fit(obj, x_train, y_train):
    start_time = time.time()
    obj.fit(x_train, y_train)
    #print("Finish")
    #print("--- %s seconds ---" % (time.time() - start_time))
    return obj

def score(obj, x_test, y_test):
    #print("Score: " + str(obj.score(x_test, y_test)))
    return obj.score(x_test, y_test)

def predictNaNx(obj, x_predict):
    yTarget = obj.predict(x_predict)
    return yTarget

def plot(obj, x_plot, y_plot, filename):
    X = prepareData(x_plot)
    obj.fit(X, y_plot)
    plotIt(obj, X, y_plot, filename + ".jpg")

def crossVal(obj, x_train, y_train, iterable, filename):
    output = cross_val_score(obj, x_train, y_train, cv=iterable)
    plotBars(output, filename + '.jpg')
    return output

def confusionMatrix(obj, x_train, y_train, x_test, y_test):
    obj1 = fit(obj, x_train, y_train)
    predictedY = predictNaNx(obj1, x_test)
    output = metrics.confusion_matrix(y_test, predictedY)
    return output


def testing(obj, x_train, y_train, nichtsX, nichtsY):
    obj1 = fit(obj, x_train, y_train)
    
    xTrain, xTest = np.split(x_train, 2)
    yTrain, yTest = np.split(y_train, 2)


    obj1 = fit(obj, xTrain, yTrain)
    yTargetTrain = obj1.predict(xTrain)
    yTarget = obj1.predict(xTest)
    
    
    i = 0
    n = 0
    m = 0
    
    while i < len(yTest):
        if yTest[i]== yTarget[i]:
            n = n + 1
            
        if yTargetTrain[i] == yTrain[i]:
            m = m +1
            
        i = i + 1
    
    holdout = n / i
    training = m / i

    return holdout, training


def fitting(obj, data, filename):
    i = 0
    n = 100
    outputArray = []
    klassen = []
    resFittitng = pd.DataFrame(columns=['HoldOut', 'Training'])
    
    while i < len(data.index):
        temp1 = []
        
        if i >=  n:
            
            x = np.array(outputArray)[:,]
            y = np.array(klassen)
            
            holdout, training  = testing(obj, x, y, x, y)
            resFittitng.loc[i,'Training'] = 1 - training
            resFittitng.loc[i,'HoldOut'] = 1 - holdout

            
            
            n = n + 100

        
        
        temp1.append(float(data['loc_x'].values[i] / 10))
        temp1.append(float(data['loc_y'].values[i] / 10))
        temp1.append(float(data['action_type'].values[i]))
        temp1.append(float(data['combined_shot_type'].values[i]))
        temp1.append(float(data['period'].values[i]))
        temp1.append(float(data['playoffs'].values[i]))
        temp1.append(float(data['shot_distance'].values[i]))
        temp1.append(float(data['shot_type'].values[i]))
        temp1.append(float(data['shot_zone_area'].values[i]))
        temp1.append(float(data['shot_zone_range'].values[i]))
        temp1.append(float(data['remaining_time'].values[i]))
        temp1.append(float(data['season'].values[i]))
        temp1.append(float(data['opponent'].values[i]))
        klassen.append(int(data['shot_made_flag'].values[i]))
        
        outputArray.append(temp1)
        
        i = i + 1
        
    resFittitng.to_csv( filename + '.csv')
    plotLinies(list(resFittitng.index), list(resFittitng['HoldOut']), list(resFittitng['Training']), filename + '.jpg')
    return resFittitng