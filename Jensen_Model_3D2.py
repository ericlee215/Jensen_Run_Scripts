# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 20:58:35 2019

@author: Owner
"""
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 18:50:16 2019

@author: Eric Lee
"""
import numpy as np
import matplotlib.pyplot as plt

    #parameters 




def Jensen_Calc2(alpha,downwind,rnot,u,theta):
    
    global variablev       #allows for variables to print to variable explorer
    
    x = len(theta)         #Defines the size of our matrices
    y = len(downwind)
    z = len(downwind)
    
    thetahat = np.degrees(np.arctan(alpha))#(downwind[-1]*alpha+rnot)/downwind[-1]))#or it might be just alpha
    variablev = np.zeros((x,y,z))        #Initializes Velocity Array
    TopHat = np.zeros((x,y,z))           #Initializes Tophat Array
    
    for i in range(y):
        for j in range(y):
            for k in range(y):
                
                dtheta = np.sqrt(theta[j]**2 + theta[k]**2)       #finds the angle
                coef = (1 + np.cos(np.deg2rad(9*dtheta)))/2      #determines distance effect
                Loss = (2/3) * (rnot/(rnot + alpha*downwind[i]))**2  #finds the v loss
                
                if dtheta >= 20:
                    
                    variablev[i][j][k] = u    #if outside range of turbine wind stays full speed
                    
                else:    
                
                    variablev[i][j][k] = u * (1 - coef * Loss)  #if inside range of turbine calculates wind speed
                    
                if dtheta >= thetahat:
                    
                    TopHat[i][j][k] = u
                    
                else:
                    
                    TopHat[i][j][k] = u * (1 - Loss)
      
        
    return TopHat

#alpha = .1
#downwind = np.linspace(120,320,41)
#rnot = 20
#u = 8.1
#theta = np.linspace(-20,20,41)
#variablev = Jensen_Calc(alpha,downwind,rnot,u,theta)

#print(Jensen_Calc(alpha,downwind,rnot,u,theta))

#print(variablev[0,20,10])
#plt.plot(theta,variablev[0,:,20]/u)
#plt.plot(theta,variablev[16,:,20]/u)
#plt.plot(theta,variablev[40,:,20]/u)