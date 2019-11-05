# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 10:49:00 2019

@author: Eric Lee
"""

import numpy as np
from Jensen_Point_Model import Jensen_Point as JP
from Katic_Model import Katic
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


nturbines = np.array([[0,0,20],[20,20,20],[-20,20,20]],)
axis = [0,0,20] 
n = len(nturbines)
for i in range(n): 
    nturbines[i,:] = np.dot(rm(axis, WindDir), nturbines[i,:])
#PosWind = np.dot(rm(axis, WindDir), PosWind)
#Turbine1 = np.dot(rm(axis, WindDir), Turbine1)
nturbines = reorder(nturbines)

wtVelocityTH = np.zeros([n,2])
wtVelocityCos = np.zeros([n,2])

wtVelocityTH[0,:] = u
wtVelocityCos[0,:] = u
WSTH = u
WSCos = u

for i in range(n-1):
    WSTH = JP(alpha,rnot,WSTH,nturbines[i,:],nturbines[i+1,:])
    WSCos = JP(alpha,rnot,WSCos,nturbines[i,:],nturbines[i+1,:])
    wtVelocityTH[i+1,:] = WSTH[0]
    wtVelocityCos[i+1,:] = WSCos[1]
    WSTH = WSTH[0]
    WSCos = WSCos[1]


rotorArea = np.pi * rnot**2

wtPowerTH = generatorEfficiency*(0.5*air_density*rotorArea*Cp*np.power(wtVelocityTH, 3))
wtPowerCos = generatorEfficiency*(0.5*air_density*rotorArea*Cp*np.power(wtVelocityCos, 3))