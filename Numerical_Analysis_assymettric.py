# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 13:35:19 2017

@author: Robin
"""
import numpy as np
import control.matlab as cs
from Data_cruncher import *
import matplotlib.pyplot as plt

def Asymetric(name):
    
    # Assigning coefficients to matrices
    C1 = np.matrix([[(CYbdot-2*name.mub),0, 0, 0],
                    [0,-0.5, 0, 0],
                    [0, 0, -4*name.mub*KX2, 4*name.mub*KXZ],
                    [Cnbdot, 0, 4*name.mub*KXZ, -4*name.mub*KZ2]])
                    
    C1[:]   *=b/name.V0
    C1[:,2] *=b/(2*name.V0)
    C1[:,3] *=b/(2*name.V0)
    print np.linalg.eig(C1)
    C2 = np.matrix([[CYb, name.CL, CYp, CYr-4*name.mub],
                    [0 , 0, 1, 0],
                    [Clb, 0, Clp, Clr],
                    [Cnb, 0, Cnp, Cnr]])
                
    C2[:,2]*=b/(2*name.V0)
    C2[:,3]*=b/(2*name.V0)
    print np.linalg.eig(C2)            
    C3 = np.matrix([[CYda, CYdr],
                    [0, 0],
                    [Clda, Cldr],
                    [Cnda, Cndr]])
 
    #combining the matrices to generate the state space system               
    A = - np.linalg.inv(C1)*C2
    B = - np.linalg.inv(C1)*C3
    C = np.matrix([[1, 0, 0, 0],
               [0, 1, 0, 0],
               [0, 0, 1, 0],
               [0, 0, 0, 1]])
    D = np.matrix([[0,0], [0,0], [0,0], [0,0]])

    sys = cs.ss(A, B, C, D)
    print sys
    #input of control system
    delev = np.column_stack((name.delta_a_stab,name.delta_r_stab))
    t = np.linspace(0,len(name.delta_r)*0.1, num=len(name.delta_r), endpoint=True, retstep=False) #time step and range 
    Xinit = np.matrix([[0], [0], [0], [0]]) # initial values for control system
    y, t, x = cs.lsim(sys, U=delev, T=t, X0=Xinit) # computing dynamic stability
#    print sys, C1, C2, C3, np.linalg.eig(A)
    
    #plotting
    y1 = []
    y2=[]
    y3=[]
    y4=[]
    y1.append(y[:,0])
    y2.append(y[:,1])
    y3.append(y[:,2])
    y4.append(y[:,3])
    
    y1 = np.transpose(y1)
    y2 = np.transpose(y2)
    y3 = np.transpose(y3)
    y4 = np.transpose(y4)
    
    y2 += 0
    y3 += 0
    y4 += 0
    
    y2 = y2*(180/np.pi)
    y3 = y3*(180/np.pi)
    y4 = y4*(180/np.pi)
    
    #plotting the total grpahs
    plt.subplot(221)
    plt.title('angle of sideslip')
    plt.plot(t, y1)
    
    plt.subplot(222)
    plt.title('roll angle')
    plt.plot(t, y2)
    plt.plot(t,name.RollAngle)
    
    
    plt.subplot(223)
    plt.title('p')
    plt.plot(t, y3)
    plt.plot(t,name.RollRate)
    
    plt.subplot(224)
    plt.title('r')
    plt.plot(t, y4)
    plt.plot(t, name.YawRate)
    
    plt.show()