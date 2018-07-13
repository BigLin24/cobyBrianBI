#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import setterID

''' Laed die CSV Datei in das
    Panda DataFrame "data" '''
data = pd.read_csv('data.csv')



''' Fasst "minutes_remaining" und "secondas_remaining" zusammen
    in der "Spalte" "remaining_time" im Dataframe dropped'''
data['remaining_time'] = data['minutes_remaining'] * 60 + data['seconds_remaining']


''' Berechnet die Spalte "dist" im Dataframe "dropped" durch:
    (WURZEL von loc_x) HOCH 2 + (loc_y)HOCH 2) '''
    
data['dist'] = np.sqrt(data['loc_x']**2 + data['loc_y']**2)




def clearFile():
    i = 0
    n = len(data.index)
    
    while i < n:
        actionName = data.values[i][0]
        combinedShotType = data.values[i][1]
        
        data.loc[i,'action_type'] = getIDforAction(actionName)
        data.loc[i,'combined_shot_type'] = getIDforCombinedShotType(combinedShotType)
        
        print(data.values[i][0])
        
        
        
        print( str(   format((( i / n ) *100), '.2f')) + "%"  )
        i = i + 1
    



''' Speicher das Dataframe "dropped" in die datei  "cleanedFile.csv"'''
data.to_csv('cleanedFileWithNaN.csv')

dropped = data

''' Loescht Eintraege bei welchen kein 
    "shot_made_flag" vorhanden ist und speicher in das Dataframe
    "dropped" ab'''
dropped = dropped.dropna(subset=['shot_made_flag'])

''' Speicher das Dataframe "Data" in die datei  "cleanedFile.csv"'''
dropped.to_csv('cleanedFile.csv')



"""
justDropped = data

i = 0

while i < len(data.index):
    
    if pd.isna(justDropped['shot_made_flag'].values[i]):
        print("yes")
        justDropped.drop(justDropped.index[i])
        print(str(format(((i /len(data.index)) * 100), '.2f')  + "%"))
        
    i = i + 1

justDropped.to_csv('justNaNFile.csv')
"""




''' Die Funktion gibt das Dataframe zurueck.
    Relevant in anderen Dokumente, um den Dataframe zu erhalten'''
    
def getDataFrameKobeBryant():
    return dropped

def getDataFrameKobeBryantWithNaN():
    return data

def getDataFrameKobeBryantJustNaN():
    return justDropped
