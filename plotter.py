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


def plotIt(obj, X, y, Filename):
    u, v = np.meshgrid(np.linspace(-30, 30),
                   np.linspace(-10, 80))
    
    uv = np.c_[u.ravel(), v.ravel()]
    
    colors1 = colors.ListedColormap(['#0000FF', '#FF0000'])
    #colors1 = colors.ListedColormap(['#FF0000', '#00ff00', '#0000ff', '#000000', '#FFA500', '#008000'])
    colors2 = colors.ListedColormap(['#FFFFFF', '#FF6060'])
    
    # Plot: Linear SVM
    toP = obj.predict(uv)
    toP = toP.reshape(u.shape)
    
    pl.figure(figsize=(7, 7)) 
    pl.contourf(u, v, toP, cmap=colors2)
    pl.scatter(X[:,0], X[:,1], 1,c=y, cmap=colors1)
    pl.savefig( Filename  , format='jpg', dpi=900)
    pl.show()
    

def plotLinies(eintrage, holdoutWerte, trainingWerte, filename):
    pl.ylabel('Fehlerrate %')
    pl.xlabel('Einträge')
    pl.axis([0, 27000, 0, 80])
    

    pl.plot(eintrage, 
            np.multiply(holdoutWerte, 100), 
            color="red",
            label='HoldOut')
    
    pl.plot(eintrage, 
        np.multiply(trainingWerte, 100), 
        color="blue",
        label='Training')
    
    
    
    pl.legend()
    
    pl.savefig( filename  , format='jpg', dpi=900)
    
    pl.show()