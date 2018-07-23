#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 06:46:02 2018

@author: biglin
"""

def counter(dataframe, group):
    colName = group.columns[0]
    
    i = 0
    output = pd.DataFrame(columns=[colName, 'Anzahl'])
    
    while i < len(group.index):
        
        test = dataframe[(dataframe[colName] == i)]
        
        counter = len(test.index)
        
        output.loc[i,colName] = group.values[i][0]
        output.loc[i,'Anzahl'] = counter
        
        i = i + 1
    
    return output