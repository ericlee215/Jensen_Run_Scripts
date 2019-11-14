# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 10:49:00 2019

@author: Eric Lee
"""

import numpy as np
from Jensen_Point_Model import Jensen_Point as JP
from Katic_Model2 import Katic
from Tester import rotation_matrix as rm
from Reorder import reorder 

generatorEfficiency = .5
air_density = 1
Cp = .3
alpha = .1
rnot = 20
u = 8.1
WindDir = 0
n = 8


nturbines = np.array([[0,0,20],[0,40,20],[0,100,20]])
n = len(nturbines)

for i in range(n):

    nturbines[i,:] = np.dot(rm(WindDir),nturbines[i,:])

#PosWind = np.dot(rm(axis, WindDir), PosWind)
#Turbine1 = np.dot(rm(axis, WindDir), Turbine1)
nturbines = reorder(nturbines)

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

        WSTop = Katic(nturbines[:i,:], rnot, nturbines[i,:], alpha, WSTop, wtVelocityTH[:i])
        WSCos = Katic(nturbines[:i,:], rnot, nturbines[i,:], alpha, WSCos, wtVelocityCos[:i])
        wtVelocityTH[0,i] = WSTop[0]
        wtVelocityCos[0,i] = WSCos[1]
        WSTop = WSTop[0]
        WSCos = WSCos[1]


rotorArea = np.pi * rnot**2

wtPowerTH = generatorEfficiency*(0.5*air_density*rotorArea*Cp*np.power(wtVelocityTH, 3))
wtPowerCos = generatorEfficiency*(0.5*air_density*rotorArea*Cp*np.power(wtVelocityCos, 3))