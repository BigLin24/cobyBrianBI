#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 13 05:44:36 2018

@author: biglin
"""
import pandas as pd 



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

def getIDforShotZoneRange( name ):
    output = searchEngine(shotZoneRange, name)
    return output

def getIDforSeason( name ):
    output = searchEngine(season, name)
    return output

def getIDforOpponent( name ):
    output = searchEngine(opponent, name)
    return output



def getActionByID( ID ):
    output = searchEngineReverse(actionType, ID)
    return output

def getCombinedShotTypeByID( ID ):
    output = searchEngineReverse(combinedShotType, ID)
    return output

def getShotTypeByID( ID ):
    output = searchEngineReverse(shotType, ID)
    return output

def getShotZoneAreaByID( ID ):
    output = searchEngineReverse(shotZoneArea, ID)
    return output

def getShotZoneRangeByID( ID ):
    output = searchEngineReverse(shotZoneRange, ID)
    return output

def getSeasonByID( ID ):
    output = searchEngineReverse(season, ID)
    return output

def getOpponentByID( ID ):
    output = searchEngineReverse(opponent, ID)
    return output




def searchEngine(dataFrame, name):
    i = 0
    
    while i < len( dataFrame.index):
        if name == dataFrame.values[i][0]:
            return i
            
        i = i +1
        

def searchEngineReverse(dataFrame, ID):
    i = 0
    
    while i < len( dataFrame.index):
        if ID == dataFrame.index[i]:
            output = dataFrame.values[i][0]
            return output
            
        i = i +1
        
        
        