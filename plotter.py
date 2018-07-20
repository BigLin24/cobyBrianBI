#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 15 20:05:17 2018

@author: biglin
"""
import numpy as np
import pylab as pl
from matplotlib import colors

goodData = []


def prepareData(x_prepare):
    goodData = np.array(x_prepare)[:, :2]
    return goodData


def plotIt( X, y, Filename):
    u, v = np.meshgrid(np.linspace(-30, 30),
                   np.linspace(-10, 90))
    
    uv = np.c_[u.ravel(), v.ravel()]
    
    colors1 = colors.ListedColormap(['#0000FF', '#FF0000'])
    #colors1 = colors.ListedColormap(['#FF0000', '#00ff00', '#0000ff', '#000000', '#FFA500', '#008000'])
    colors2 = colors.ListedColormap(['#9090FF', '#FF6060'])
    
    # Plot: Linear SVM
   # toP = obj.predict(uv)
    #toP = toP.reshape(u.shape)
    
    #pl.figure(figsize=(7, 7)) 
    #pl.contourf(u, v, toP, cmap=colors2)
    pl.scatter(X[:,0], X[:,1], 10,c=y, cmap=colors1)
    pl.savefig( Filename  , format='jpg', dpi=900)
    pl.show()
    

def barPlot( listeBar ):
    N = len(listeBar)
    ind = np.arange(N)
    
    #barWerte = np.array(dataFrame['Anzahl'].values).tolist()
    
    barWerte = listeBar
 # the x locations for the groups
    width = 0.35       # the width of the bars: can also be len(x) sequence
    
    p1 = pl.bar(barWerte, ind, width)
    
    pl.yticks(np.arange(0, 20, 10))
    pl.legend(p1[0], 'Men')
    
    pl.show()
    
    
    
    
    
    
    
def test( ):
    N = 5
    menMeans = (20, 35, 30, 35, 27)
    womenMeans = (25, 32, 34, 20, 25)
    menStd = (2, 3, 4, 1, 2)
    womenStd = (3, 5, 2, 3, 3)
    ind = np.arange(N)    # the x locations for the groups
    width = 0.35       # the width of the bars: can also be len(x) sequence
    
    p1 = pl.bar(ind, menMeans, width, yerr=menStd)
    p2 = pl.bar(ind, womenMeans, width,
             bottom=menMeans, yerr=womenStd)
    
    pl.ylabel('Scores')
    pl.title('Scores by group and gender')
    pl.xticks(ind, ('G1', 'G2', 'G3', 'G4', 'G5'))
    pl.yticks(np.arange(0, 81, 10))
    pl.legend((p1[0], p2[0]), ('Men', 'Women'))
    
    pl.show()
    