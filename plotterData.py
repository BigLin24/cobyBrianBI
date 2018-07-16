#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 16 08:29:04 2018

@author: biglin
"""
import pylab as pl
import pandas as pd 
import numpy as np

actionType = pd.read_csv('actionType.csv')
combinedShotType = pd.read_csv('combinedShotType.csv')
shotType = pd.read_csv('shotType.csv')
shotZoneArea = pd.read_csv('shotZoneArea.csv')
shotZoneRange = pd.read_csv('shotZoneRange.csv')
season = pd.read_csv('season.csv')
opponent = pd.read_csv('opponent.csv')


data = pd.read_csv('shotFlagBerrechnet/restoredAbaBoost.csv')


def getShoted(inputDataFrame):
    output = inputDataFrame[(inputDataFrame['shot_made_flag'] == 1)]
    return output



def getActionTypes(inputDataFrame):
    output = getTypes(actionType, inputDataFrame, 'action_type')
    return output

def getCombinedShotType(inputDataFrame):
    output = getTypes(combinedShotType, inputDataFrame, 'combined_shot_type')
    return output

def getShotType(inputDataFrame):
    output = getTypes(shotType, inputDataFrame, 'shot_type')
    return output

def getShotZoneArea(inputDataFrame):
    output = getTypes(shotZoneArea, inputDataFrame, 'shot_zone_area')
    return output

def getShotZoneRange(inputDataFrame):
    output = getTypes(shotZoneRange, inputDataFrame, 'shot_zone_range')
    return output

def getSeason(inputDataFrame):
    output = getTypes(season, inputDataFrame, 'shot_zone_range')
    return output

def getOpponent(inputDataFrame):
    output = getTypes(season, inputDataFrame, 'shot_zone_range')
    return output


def getTypes(inputDataFrame, dataFrame, rowName):
    output = pd.DataFrame(columns=[rowName, 'Anzahl'])
    
    i = 0
    
    while i < len(inputDataFrame.index):
        n = inputDataFrame.values[i][0]
        
        anzahl = len(dataFrame[(dataFrame[rowName] == n)])
        
        output.loc[i, rowName] = n
        output.loc[i,'Anzahl'] = anzahl
        
        i = i + 1
        
    return output