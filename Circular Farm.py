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
import matplotlib.pyplot as plt

generatorEfficiency = .5
air_density = 1
Cp = .3
alpha = .1
rnot = 20
u = 8.1
WindDir = 16

n = 10
D = 200
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

for i in range(n):

    nturbines[i,:] = np.dot(rm(WindDir),nturbines[i,:])

#PosWind = np.dot(rm(axis, WindDir), PosWind)
#Turbine1 = np.dot(rm(axis, WindDir), Turbine1)
nturbines = reorder(nturbines)
plt.plot(nturbines[:,0],nturbines[:,1],'bo')
wtVelocityTH = np.zeros([1,n])
wtVelocityCos = np.zeros([1,n])


WSTop = u
WSCos = u

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
        t =1


rotorArea = np.pi * rnot**2

wtPowerTH = generatorEfficiency*(0.5*air_density*rotorArea*Cp*np.power(wtVelocityTH, 3))
wtPowerCos = generatorEfficiency*(0.5*air_density*rotorArea*Cp*np.power(wtVelocityCos, 3))