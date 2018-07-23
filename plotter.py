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
    

def plotLinies( eintrage, holdoutWerte, trainingWerte, filename ):
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
   
    
def plotBars( barsHigh, filename ):
    years = ('2010', '2011', '2012', '2013', '2014')
    visitors = (1241, 50927, 162242, 222093, 296665 / 8 * 12)
    
    xIndex = []
    average = []
    i = 0
    
    
    while i < len(barsHigh):
        xIndex.append(i + 1)
        average.append(np.average(barsHigh) * 100)
        i = i +1 
    

    index = np.arange(len(visitors))
    bar_width = 0.5
    
    pl.bar(xIndex, np.multiply(barsHigh, 100), bar_width,  color="blue")
    pl.xticks(xIndex) # labels get centered
    
    pl.ylabel('Richtigkeit %')
    pl.xlabel('Faltungen')
    
    pl.axis([0, 11, 0, 100])
    
    
    
    averageLabel = format(np.average(barsHigh) * 100, '.2f') 
    pl.plot(xIndex, 
        average, 
        color="red",
        label='Durchschnitt bei ' + str( averageLabel) + '%')

    pl.legend()
    
    pl.savefig( filename  , format='jpg', dpi=900)
    
    pl.show()
    

def plotItpredict( X, y, Filename):
    
    #Colors1 = colors.ListedColormap(['#0000FF', '#FF0000'])
    colors1 = colors.ListedColormap(['#FF0000', '#0000ff', '#ffff00', '#00ff00','#000000', '#808080'])
    
    pl.figure(figsize=(7, 7)) 
    pl.scatter(X[:,0], X[:,1], 20,c=y, cmap=colors1)
    pl.savefig( Filename  , format='jpg', dpi=900)
    pl.show()
    
    
def pieDiagramm( counterDataframe, Filename):
    
    colName = counterDataframe.columns[0]
    xWerte = counterDataframe['Anzahl'].values
    label = counterDataframe[colName].values
    
    pl.axis("equal") # Kreisdiagramm rund gestaltet (sonst Standard: oval!)
    pl.pie(xWerte, labels=label, autopct="%1.1f%%")
    pl.savefig( Filename  , format='jpg', dpi=900)
    pl.show()