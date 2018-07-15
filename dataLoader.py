#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 15 20:22:25 2018

@author: biglin
"""
import pylab as pl
import pandas as pd 
import numpy as np
from sklearn import model_selection


data = pd.read_csv('cleanedFileWithoutNaN.csv')
predictData = pd.read_csv('cleanedFileJustNaN.csv')


def convertToArrayData(data):
    i = 0
    outputArray = []
    
    while i < len(data.index):
        temp1 = []
        
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
            
        outputArray.append(temp1)
        
        i = i + 1
        
    return outputArray



def convertToArrayClass(data):
    i = 0
    outputArray = []
    
    while i < len(data.index):
        outputArray.append(int(data['shot_made_flag'].values[i]))
        i = i + 1

    return outputArray



werte = convertToArrayData(data)
klassen = convertToArrayClass(data)
predict = convertToArrayData(predictData)


x_train, x_test, y_train, y_test = \
    model_selection.train_test_split(np.array(werte)[:,],\
                                     klassen, test_size=0.33)



def setPredictedValues(Dataframe, predicted_y):
    i = 0
    n = len(Dataframe.index)
    
    while i < n:
        Dataframe.loc[i,'shot_made_flag'] = predicted_y[i]
        
        i = i + 1
    
    return Dataframe
    