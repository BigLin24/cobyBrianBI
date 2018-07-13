#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 13 05:44:36 2018

@author: biglin
"""
import pandas as pd 

actionType = pd.read_csv('actionType.csv')
combinedShotType = pd.read_csv('combinedShotType.csv')
shotType = pd.read_csv('shotType.csv')
shotZoneArea = pd.read_csv('shotZoneArea.csv')
season = pd.read_csv('shotZoneArea.csv')
opponent = pd.read_csv('opponent.csv')

def getIDforAction( name ):
    output = searchEngine(actionType, name)
    return output

def getIDforCombinedShotType( name ):
    output = searchEngine(combinedShotType, name)
    return output

def getIDforShotType( name ):
    output = searchEngine(shotType, name)
    return output

def getIDforShotZoneArea( name ):
    output = searchEngine(shotZoneArea, name)
    return output

def getIDforSeason( name ):
    output = searchEngine(season, name)
    return output

def getIDforOpponent( name ):
    output = searchEngine(opponent, name)
    return output


def searchEngine(dataFrame, name):
    i = 0
    
    while i < len( dataFrame.index):
        if name == dataFrame.values[i][0]:
            return i
            
        i = i +1
        
        
        
        
        