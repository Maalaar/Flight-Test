# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 13:35:19 2017

@author: Robin
"""
import numpy as np
import control.matlab as cs
import matplotlib.pyplot as plt
from Data_cruncher import *

def Symetric(name):
    
    # Assigning coefficients to matrices
    C1 = np.matrix([[-2*name.muc*(c/(name.V0)), 0, 0, 0],
                    [0, (name.CZadot-2*name.muc)*(c/name.V0), 0, 0],
                    [0, 0, -(c/name.V0), 0],
                    [0, name.Cmadot*(c/name.V0), 0, -2*name.muc*KY2*((c/name.V0))]])

    C1[:,0]/=name.V0
    C1[:,3]*=(c/name.V0)
    
    C2 = np.matrix([[name.CXu, name.CXa, name.CZ0, 0],
                    [name.CZu, name.CZa, -name.CX0, (name.CZq + 2*name.muc)],
                    [0, 0, 0, 1],
                    [name.Cmu, name.Cma, 0, name.Cmq]])
    C2[:,0]/=name.V0
    C2[:,3]*=(c/name.V0)
                
    C3 = np.matrix([[name.CXde],
                    [name.CZde],
                    [0],
                    [name.Cmde]])
 
     #combining the matrices to generate the state space system               
    A = - np.linalg.inv(C1)*C2
    B = - np.linalg.inv(C1)*C3
    C = np.matrix([[1, 0, 0, 0],
                   [0, 1, 0, 0],
                   [0, 0, 1, 0],
                   [0, 0, 0, 1]])
    D = np.matrix([[0], [0], [0], [0]])

    sys = cs.ss(A, B, C, D)

    #input of control system
    delev = name.deltae *(np.pi/180) #input of elevator deflection
    t = np.linspace(0,len(name.deltae)*0.1, num=len(name.deltae), endpoint=True, retstep=False) #time step and range  
    Xinit = np.matrix([[0], [0], [0], [0]]) # initial values for control system
    y, t, x = cs.lsim(sys, U=delev, T=t, X0=Xinit) # computing dybnamic stability

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

    y2 = y2*(180/np.pi)
    y3 = y3*(180/np.pi)
    y4 = y4*(180/np.pi)
    
    y1 += name.V0
    y2 += name.AoA0
    y3 += name.PitchAngle0


#    plotting the total grpahs
    plt.subplot(221)
    plt.title('u')
    plt.plot(t, y1)
    plt.plot(t, name.EAS)

    plt.subplot(222)
    plt.title('alpha')
    plt.plot(t, y2)
    plt.plot(t, name.AoA)

    plt.subplot(223)
    plt.title('Theta')
    plt.plot(t, y3)
    plt.plot(t, name.PitchAngle)


    plt.subplot(224)
    plt.title('q')
    plt.plot(t, y4)

    
    plt.show()