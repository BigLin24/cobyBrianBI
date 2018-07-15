#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import setterID


#data = pd.read_csv('data.csv')
data = pd.read_csv('cleanedFileWithNaN-v1.csv')


data['remaining_time'] = data['minutes_remaining'] * 60 + data['seconds_remaining']
data['dist'] = np.sqrt(data['loc_x']**2 + data['loc_y']**2)

dropped = data
dropped = dropped.dropna(subset=['shot_made_flag'])




def writeFiles():
    data.to_csv('cleanedFileWithNaN.csv', index=False)
    dropped.to_csv('cleanedFile.csv', index=False)


def clearFile():
    i = 0
    n = len(data.index)
    
    while i < n:
        actionName = data.values[i][0]
        combinedShotType = data.values[i][1]
        shotType = data.values[i][15]
        shotZoneArea = data.values[i][16]
        shotZoneRange = data.values[i][18]
        season = data.values[i][11]
        opponent = data.values[i][23]
        
        data.loc[i,'action_type'] = getIDforAction(actionName)
        data.loc[i,'combined_shot_type'] = getIDforCombinedShotType(combinedShotType)
        data.loc[i,'shot_type'] = getIDforShotType(shotType)
        data.loc[i,'shot_zone_area'] = getIDforShotZoneArea(shotZoneArea)
        data.loc[i,'shot_zone_range'] = getIDforShotZoneRange(shotZoneRange)
        data.loc[i,'season'] = getIDforSeason(season)
        data.loc[i,'opponent'] = getIDforOpponent(opponent)
        
        print( str(   format((( i / n ) *100), '.2f')) + "%"  )
        
        i = i +1


def clearJustNaN():
    i = 0
    n = len(data.index)
    
    output = data
    
    while i < n:
        
        if not pd.isna(output['shot_made_flag'][i]):
            output.drop([i], inplace=True)
        
        print( str(   format((( i / n ) *100), '.2f')) + "%"  )
        
        i = i + 1
    
    output1 = output.reset_index()
    output1.drop(columns='index', inplace=True)
    
    return output1

    
def getDataFrameKobeBryant():
    return dropped

def getDataFrameKobeBryantWithNaN():
    return data

def getDataFrameKobeBryantJustNaN():
    return justNaN

