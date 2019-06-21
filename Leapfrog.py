#Author:Eric Lee
#FIle Name: LeapFrogging Vortexes

import numpy as np
import matplotlib.pyplot as plt

n = 4000                                  
P1 = [0,-.5, 0]
P2 = [0,.5, 0]
P3 = [2, .5, 0]
P4 = [2, -.5, 0]
Gamma = np.array([0,0,1])
dt = .01

Traj1 = np.zeros((2, n))                     
Traj2 = np.zeros((2, n))
Traj3 = np.zeros((2, n))
Traj4 = np.zeros((2,n))
V1 = np.zeros((2, n))
V2 = np.zeros((2, n))
V3 = np.zeros((2, n))
V4 = np.zeros((2, n))


for i in range(n):
    
    R11 = np.subtract(P1, P2)
    R12 = np.subtract(P1, P3)
    R13 = np.subtract(P4, P1)
    R21 = np.subtract(P1, P2)
    R22 = np.subtract(P2, P3)
    R23 = np.subtract(P4, P2)
    R31 = np.subtract(P1, P3)
    R32 = np.subtract(P3, P2)
    R33 = np.subtract(P4, P3)
    R41 = np.subtract(P1, P4)
    R42 = np.subtract(P4, P2)
    R43 = np.subtract(P4, P3)
    
    #First Point
    
    V = (np.cross(Gamma,R11)/np.linalg.norm(R11)**2 + np.cross(Gamma,R12)/np.linalg.norm(R12)**2 + np.cross(Gamma,R13)/np.linalg.norm(R13)**2)/(2*np.pi)
    
    
    V = V[:-1]
    V1[:,i] = V
    
    P1 = P1[:-1]
    Traj1[:,i] = V * dt + P1
    P1 = np.transpose(Traj1[:,i])
    P1 = np.append(P1, 0)
    
    #Second Point
    
    V = (np.cross(Gamma,R21)/np.linalg.norm(R21)**2 + np.cross(Gamma,R22)/np.linalg.norm(R22)**2 + np.cross(Gamma,R23)/np.linalg.norm(R23)**2)/(2*np.pi)
    
    V = V[:-1]
    V2[:,i] = V
    
    P2 = P2[:-1]
    Traj2[:,i] = V * dt + P2
    P2 = np.transpose(Traj2[:,i])
    P2 = np.append(P2, 0)
    
    #Third Point
    
    V = (np.cross(Gamma,R31)/np.linalg.norm(R31)**2 + np.cross(Gamma,R32)/np.linalg.norm(R32)**2 + np.cross(Gamma,R33)/np.linalg.norm(R33)**2)/(2*np.pi)
    
    V = V[:-1]
    V3[:,i] = V
    
    P3 = P3[:-1]
    Traj3[:,i] = V * dt + P3
    P3 = np.transpose(Traj3[:,i])
    P3 = np.append(P3, 0)
    
    #Fourth Point
    
    V = (np.cross(Gamma,R41)/np.linalg.norm(R41)**2 + np.cross(Gamma,R42)/np.linalg.norm(R42)**2 + np.cross(Gamma,R43)/np.linalg.norm(R43)**2)/(2*np.pi)
    
    V = V[:-1]
    V4[:,i] = V
    
    P4 = P4[:-1]
    Traj4[:,i] = V * dt + P4
    P4 = np.transpose(Traj4[:,i])
    P4 = np.append(P4, 0)
    
    
Position1X = Traj1[0,:]
Position1Y = Traj1[1,:]
Position2X = Traj2[0,:]
Position2Y = Traj2[1,:]
Position3X = Traj3[0,:]
Position3Y = Traj3[1,:]
Position4X = Traj4[0,:]
Position4Y = Traj4[1,:]


plt.plot(Position1X,Position1Y, 'c',Position2X,Position2Y, 'c',Position3X,Position3Y, 'r',Position4X,Position4Y, 'r')

plt.title("Vortex Trajectories")
plt.ylabel("Vortex Height")
plt.xlabel("Distance Traveled")
plt.show()



    