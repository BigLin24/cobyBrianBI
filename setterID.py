#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 13 05:44:36 2018

@author: biglin
"""
import pandas as pd 

actionType = pd.read_csv('actionType.csv')


def getIDforAction( name ):
    i = 0
    
    while i < len(actionType.index):
        if name == actionType.values[i][0]:
            return i
            
        i = i +1
        
        