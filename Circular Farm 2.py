# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 20:47:00 2019

@author: Owner
"""

import numpy as np
from Jensen_Point_Model import Jensen_Point as JP
from Katic_Model2 import Katic
from Tester import rotation_matrix as rm
from Reorder import reorder
import random 
import matplotlib.pyplot as plt

Direction = np.array([0,-5, 5,-7.5, 10, -15, 20, -22.5, 30, 35])
Speed = np.array([6.5, 6.75, 7, 7.25, 7.5, 7.75, 8, 8.1, 8.25, 8.5])
FreqS = np.array([.05, .07, .11, .12, .13, .13, .11, .10, .10, .08])
FreqD = np.array([.27, .21, .21, .09, .08, .05, .04, .03, .01 , .01])
amount = len(FreqS)


generatorEfficiency = .93
air_density = 1.275
Cp = .41
alpha = .1
rnot = 20

n = 20
D = 250
spacing = 360/n
theta = 0
coordinates = np.zeros([n,3])



for i in range(n):
    coordinates[i,0] = D*np.cos(np.deg2rad(theta))
    coordinates[i,1] = D*np.sin(np.deg2rad(theta))
    theta = theta + spacing
coordinates[:,2] = 20

nturbines = coordinates
n = len(nturbines)


#PosWind = np.dot(rm(axis, WindDir), PosWind)
#Turbine1 = np.dot(rm(axis, WindDir), Turbine1)

#plt.plot(nturbines[:,0],nturbines[:,1],'bo')
wtVelocityTH = np.zeros([1,n])
wtVelocityCos = np.zeros([1,n])


PowerTH = 0
PowerCos = 0
Y = 0

for k in range(len(Direction)):
    for j in range(len(Direction)):        

        nturbines[k,:] = np.dot(rm(Direction[k]),nturbines[k,:])
            
        nturbines = reorder(nturbines)
        
        WSTop = Speed[j]
        WSCos = Speed[j]
        u = Speed[j]
    
        for i in range(n):
            
            if i == 0:
                wtVelocityTH[0,i] = u
                wtVelocityCos[0,i] = u
                
            elif i == 1:
                
                WSTop = JP(alpha,rnot,WSTop,nturbines[i-1,:],nturbines[i,:])
                WSCos = JP(alpha,rnot,WSCos,nturbines[i-1,:],nturbines[i,:])
                wtVelocityTH[0,i] = WSTop[0]
                wtVelocityCos[0,i] = WSCos[1]
                WSTop = WSTop[0]
                WSCos = WSCos[1]
                
            else:
                #(TurbineN, rnot, PosWind,alpha,u,otheru)
                
                WSTop = Katic(nturbines[:i,:], rnot, nturbines[i,:], alpha, u)
                WSCos = Katic(nturbines[:i,:], rnot, nturbines[i,:], alpha, u)
                wtVelocityTH[0,i] = WSTop[0]
                wtVelocityCos[0,i] = WSCos[1]
                WSTop = WSTop[0]
                WSCos = WSCos[1]
                
            
        rotorArea = np.pi * rnot**2
        
        wtPowerTH = generatorEfficiency*(0.5*air_density*rotorArea*Cp*np.power(wtVelocityTH, 3))
        wtPowerCos = generatorEfficiency*(0.5*air_density*rotorArea*Cp*np.power(wtVelocityCos, 3))
        

        
        PowerTH = (np.sum(wtPowerTH)/1000)*FreqD[k]*FreqS[j] + PowerTH
        PowerCos = (np.sum(wtPowerCos)/1000)*FreqD[k]*FreqS[j] + PowerCos
    



