#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt


''' Laed die CSV Datei in das
    Panda DataFrame "data" '''
data = pd.read_csv('data.csv')


''' Loescht Eintraege bei welchen kein 
    "shot_made_flag" vorhanden ist und speicher in das Dataframe
    "dropped" ab'''
dropped = data.dropna(subset=['shot_made_flag'])

#dropped.to_csv('testfileDropped.csv')


''' Fasst "minutes_remaining" und "secondas_remaining" zusammen
    in der "Spalte" "remaining_time" im Dataframe dropped'''
dropped['remaining_time'] = dropped['minutes_remaining'] * 60 + dropped['seconds_remaining']


''' Berechnet die Spalte "dist" im Dataframe "dropped" durch:
    (WURZEL von loc_x) HOCH 2 + (loc_y)HOCH 2) '''
    
dropped['dist'] = np.sqrt(dropped['loc_x']**2 + dropped['loc_y']**2)

''' Speicher das Dataframe "dropped" in die datei  "cleanedFile.csv"'''
dropped.to_csv('cleanedFile.csv')


''' Die Funktion gibt das Dataframe zurueck.
    Relevant in anderen Dokumente, um den Dataframe zu erhalten'''
    
def getDataFrameKobeBryant():
    return dropped