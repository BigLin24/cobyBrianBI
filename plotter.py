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
                   np.linspace(-10, 90))
    
    uv = np.c_[u.ravel(), v.ravel()]
    
    colors1 = colors.ListedColormap(['#0000FF', '#FF0000'])
    colors2 = colors.ListedColormap(['#9090FF', '#FF6060'])
    
    # Plot: Linear SVM
    toP = obj.predict(uv)
    toP = toP.reshape(u.shape)
    #pl.figure(figsize=(7, 7)) 
    pl.contourf(u, v, toP, cmap=colors2)
    pl.scatter(X[:,0], X[:,1], 5,c=y, cmap=colors1)
    pl.savefig( Filename  , format='jpg', dpi=900)
    pl.show()