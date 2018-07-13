#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: hrothe
Original Sources: http://scikit-learn.sourceforge.net/0.5/auto_examples/svm/plot_iris.html
"""

import numpy as np
import pylab as pl
import time
import threading

from matplotlib import colors
from sklearn import svm, datasets, model_selection, linear_model, tree, \
    neural_network, neighbors, gaussian_process, ensemble, \
    naive_bayes, discriminant_analysis

import dataPreperationv2



"""
# import some data to play with
iris = datasets.load_iris()
print(iris)
X = iris.data[:, :2] # we only take the first two features. We could
   # avoid this ugly slicing by using a two-dim dataset
Y = iris.target
h=.02 # step size in the mesh

"""








data = getDataFrameKobeBryant()
predictData = getDataFrameKobeBryantWithNaN()

werte = []
target = []
predict = []
i = 0

#while i < len(data.index):
while i < len(data.index):
    temp1 = []
    
    temp1.append(float(data['loc_x'].values[i] / 10))
    temp1.append(float(data['loc_y'].values[i] / 10))
    
    werte.append(temp1)
    target.append(int(data['shot_made_flag'].values[i]))
    i = i + 1


i = 0

while i < len(predictData.index):
    temp1 = []
    
    temp1.append(float(predictData['loc_x'].values[i] / 10))
    temp1.append(float(predictData['loc_y'].values[i] / 10))
    
    predict.append(temp1)
    
    i = i + 1



x_train, x_test, y_train, y_test = \
    model_selection.train_test_split(np.array(werte)[:,],\
                                     target, test_size=0.33)




# Moegliche Werte
X = x_train
# Klassen
y = y_train

Xpredict = np.array(predict)[:,]

svc3 = svm.LinearSVC()
svc2 = svm.SVC()
svc = svm.SVC(kernel='poly')
regr = linear_model.LinearRegression()
clf = tree.DecisionTreeClassifier()
nn = neural_network.MLPClassifier()
nb = neighbors.KNeighborsClassifier()
gp = gaussian_process.GaussianProcessClassifier()
rf = ensemble.RandomForestClassifier()
ada = ensemble.AdaBoostClassifier()
naveB = naive_bayes.GaussianNB()
qda = discriminant_analysis.QuadraticDiscriminantAnalysis()


def calWithLinearSVC():
    # Normal -> Linear   
    svc3.fit(X, y)
    z3 = svc3.predict(uv)
    z3 = z3.reshape(u.shape)
    print("Finish LinearSVC: svc3")

def calWithSVCnormaleKernel():
    # Kernel Default    
    svc2.fit(X, y)
    z2 = svc2.predict(uv)
    z2 = z2.reshape(u.shape)
    print("Finish KernelSVC: svc2")

def calWithSVCpolyKernel():
    # Kernel mit Poly 
    svc.fit(X, y)
    z = svc.predict(uv)
    z = z.reshape(u.shape)
    print("Finish PolyKernelSVC: svc")

def calLinearRegression():
    regr.fit(X, y)
    print("Finish LinearRegression: regr")
    
def calDecisionTree():
    clf.fit(X, y)
    print("Finish DecisionTree: clf")
    
def calNornalNetwork():
    nn.fit(X, y)
    print("Finish Nornal Network: nn")

def calNearestNeighbors():
    nb.fit(X, y)
    print("Finish Nearest Neighbors: nb")

def calGausianProcess():
    gp.fit(X, y)
    print("Finish Gausian Process: gp")
    
def calRandomForest():
    rf.fit(X, y)
    print("Finish Random Forst: rf")

def calAdaBoost():
    ada.fit(X, y)
    print("Finish Ada Boost: ada")
    
def calNaiveBayes():
    naveB.fit(X, y)
    print("Finish Naive Bayes: naveB")
    
def calQDA():
    qda.fit(X, y)
    print("Finish Quadratic Disciminat Analysis: qda")


t1 = threading.Thread( target = calWithLinearSVC )
t2 = threading.Thread( target = calWithSVCnormaleKernel)
t3 = threading.Thread( target = calWithSVCpolyKernel)
t4 = threading.Thread( target = calLinearRegression)
t5 = threading.Thread( target = calDecisionTree)
t6 = threading.Thread( target = calNornalNetwork)
t7 = threading.Thread( target = calNearestNeighbors)
t8 = threading.Thread( target = calGausianProcess)
t9 = threading.Thread( target = calRandomForest)
t10 = threading.Thread( target = calAdaBoost)
t11 = threading.Thread( target = calNaiveBayes)
t12 = threading.Thread( target = calQDA)


def calWithAll():
   
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()
    t6.start()
    t7.start()
    t8.start()
    t9.start()
    t10.start()
    t11.start()
    t12.start()

def testAll():
    checkThread(t12)
    print("QDA Score: " + str(naveB.score(x_test, y_test)))
    
    checkThread(t11)
    print("Naive Bayes Score: " + str(naveB.score(x_test, y_test)))
    
    checkThread(t10)
    print("Ada Boost Score: " + str(ada.score(x_test, y_test)))
    
    checkThread(t9)
    print("Random Forest Score: " + str(rf.score(x_test, y_test)))
    
    checkThread(t4)
    print("Linear Regression Score: " + str(regr.score(x_test, y_test)))
    
    checkThread(t5)
    print("Decision Tree Score: " + str(clf.score(x_test, y_test)))
    
    checkThread(t1)
    print("Linear SVM Score: " + str(svc3.score(x_test, y_test)))
    
    checkThread(t6)
    print("Nornal Network Score: " + str(nn.score(x_test, y_test)))
    
    checkThread(t7)
    print("Nearest Neighbors Score: " + str(nb.score(x_test, y_test)))
    
    checkThread(t2)
    print("Kernel SVM Score: " + str(svc2.score(x_test, y_test)))
    
    checkThread(t8)
    print("Gaussian Process Score: " + str(gp.score(x_test, y_test)))
    
    checkThread(t3)
    print("Poly-Kernel SVM Score: " + str(svc.score(x_test, y_test)))


def plotQDA():
    checkThread(t12)
    plotIt(qda, "qga.jpg")
    
def plotNaiveBayes():
    checkThread(t11)
    plotIt(naveB,"NaiveBayes.jpg")
    
def plotAdaBoost():
    checkThread(t10)
    plotIt(ada, "AdaBoost.jpg")
    
def plotRandomForest():
    checkThread(t9)
    plotIt(rf, "RandomForest.jpg")





def checkThread(threadID):
    if threading.Thread.is_alive(threadID):
        threadID.join()

def plotIt(obj, Filename):
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
    
   
    
    
    
    
    """
    pl.contourf(u, v, z3, cmap=colors2)
    pl.scatter(X[:,0], X[:,1], 15,c=y, cmap=colors1)
    pl.show()
    
    pl.contourf(u, v, z2, cmap=colors2)
    pl.scatter(X[:,0], X[:,1], 15,c=y, cmap=colors1)
    pl.show()
    
    pl.contourf(u, v, z, cmap=colors2)
    pl.scatter(X[:,0], X[:,1], 15,c=y, cmap=colors1)
    pl.show()
    """










