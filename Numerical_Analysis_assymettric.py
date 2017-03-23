# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 13:35:19 2017

@author: Robin
"""
import numpy as np
import control.matlab as cs
from Cit_par import *
import matplotlib.pyplot as plt
from Data_cruncher_vanmij import *

def Asymetric(name)
    # Assigning coefficients to matrices
    C1 = np.matrix([[(name.CYbdot-2*name.mub)*b/name.V0,0, 0, 0],
                [0,-0.5*b/V0, 0, 0],
                [0, 0, -4*name.mub*KX2*b/name.V0, 4*name.mub*KXZ*b/name.V0],
                [name.Cnbdot*b/name.V0, 0, 4*name.mub*KXZ*b/name.V0, -4*name.mub*KZ2*b/name.V0]])

    C1[:,2]*=b/(2*V0)
    C1[:,3]*=b/(2*V0)

    C2 = np.matrix([[name.CYb, name.CL, name.CYp, name.CYr-4*name.mub],
                    [0 , 0, 1, 0],
                    [name.Clb, 0, name.Clp, name.Clr],
                    [name.Cnb, 0, name.Cnp, name.Cnr]])
                
    C2[:,2]*=b/(2*V0)
    C2[:,3]*=b/(2*V0)
                
    C3 = np.matrix([[name.CYda, name.CYdr],
                    [0, 0],
                    [name.Clda, name.Cldr],
                    [name.Cnda, name.Cndr]])
 
    #combining the matrices to generate the state space system               
    A = - np.linalg.inv(C1)*C2
    B = - np.linalg.inv(C1)*C3
    C = np.matrix([[1, 0, 0, 0],
               [0, 1, 0, 0],
               [0, 0, 1, 0],
               [0, 0, 0, 1]])
    D = np.matrix([[0,0], [0,0], [0,0], [0,0]])

    sys = cs.ss(A, B, C, D)

    #input of control system
    delev = np.column_stack((delta_a,delta_r))/180*np.pi
    t = np.linspace(0,len(delta_a)*0.1, num=len(delta_r), endpoint=True, retstep=False) #time step and range 
    Xinit = np.matrix([[0], [0], [0], [0]]) # initial values for control system
    y, t, x = cs.lsim(sys, U=delev, T=t, X0=Xinit) # computing dynamic stability

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
    
    y1 = y1 + V0
    y2 += alpha0
    y3 += th0
    
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