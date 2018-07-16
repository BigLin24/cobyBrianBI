#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 16 00:14:16 2018

@author: biglin
"""

import pylab as pl
import pandas as pd 
import numpy as np
from sklearn import model_selection
import KernelSVM
import DecisionTree
import RandomForest

data = pd.read_csv('cleanedFileWithoutNaN.csv')

resFittitng = pd.DataFrame(columns=['Score', 'HandOut'])




def startFitting(data):
    i = 0
    n = 1000
    outputArray = []
    klassen = []
    
    while i < len(data.index):
        temp1 = []
        
        if i >=  n:
            x_train, x_test, y_train, y_test = \
            model_selection.train_test_split(np.array(outputArray)[:,],\
                                             np.array(klassen), test_size=0.33)
            
            
            scoreKernel, handoutKernel = testKernelSVM(x_train, y_train, x_test, y_test)
            resFittitng.loc[i,'Score'] = scoreKernel
            resFittitng.loc[i,'HandOut'] = handoutKernel

            
            
            n = n + 1000

        
        
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
        
    resFittitng.to_csv('fitting.csv')

