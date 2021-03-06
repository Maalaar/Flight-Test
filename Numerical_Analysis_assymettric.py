# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 13:35:19 2017

@author: Robin
"""
import numpy as np
import control.matlab as cs
from Data_cruncher import *
import matplotlib.pyplot as plt

#namem= "Dutch Roll + Yaw [Ultimate Final Johan is een natte pannekoek]"

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
    
    
    y2 *= (180/np.pi)
    y3 *= (180/np.pi)
    y4 *= (180/np.pi)
    y2 += name.RollAngle0
    y3 += name.RollRate0
    y4 += name.YawRate0
    
    return y1,y2,y3,y4,t
    
##    plotting the total grpahs
#    plt.figure(0)
##    plt.gca().set_ylim([-1,0])
##    plt.gca().set_xlim([0,140])    
#    plt.tick_params(axis="x", labelsize=15)
#    plt.tick_params(axis="y", labelsize=15)    
#    plt.title('Angle of Sideslip ')
#    plt.plot(t, y1, label="Numerical Optimized", color="blue")
#    plt.ylabel(r"$\beta$ [deg]")
#    plt.xlabel("t [s]")
#    plt.legend(loc=2)
#    plt.savefig((namem + "Angle of Sideslip"))
#    plt.show()
#    
#    plt.figure(1)
##    plt.gca().set_ylim([-1,0])
##    plt.gca().set_xlim([0,140])    
#    plt.tick_params(axis="x", labelsize=15)
#    plt.tick_params(axis="y", labelsize=15)
#    plt.title('Roll Angle ')
#    plt.plot(t, y2, label="Numerical Optimized", color="blue")
#    plt.ylabel("$\phi$ [deg]")
#    plt.xlabel("t [s]")
#    plt.plot(t, name.RollAngle, label="Experimental", color="green")
#    plt.legend(loc=2)
#    plt.savefig((namem + "RollAngle"))
#    plt.show()
#    
#    plt.figure(2)
##    plt.gca().set_ylim([-1,0])
##    plt.gca().set_xlim([0,140])    
#    plt.tick_params(axis="x", labelsize=15)
#    plt.tick_params(axis="y", labelsize=15)
#    plt.title('Roll Rate')
#    plt.plot(t, y3, label="Numerical Optimized", color="blue")
#    plt.ylabel("p [deg/s]")
#    plt.xlabel("t [s]")
#    plt.plot(t, name.RollRate, label="Experimental", color="green")
#    plt.legend(loc=2)
#    plt.savefig((namem + "RollRate"))
#    plt.show()
#
#    plt.figure(3)
##    plt.gca().set_ylim([-1,0])
##    plt.gca().set_xlim([0,140])    
#    plt.tick_params(axis="x", labelsize=15)
#    plt.tick_params(axis="y", labelsize=15)
#    plt.title('Yaw Rate')
#    plt.plot(t, y4, label="Numerical Optimized", color="blue")
#    plt.ylabel("r [deg/s]")
#    plt.xlabel("t [s]")
#    plt.plot(t, name.YawRate, label="Experimental", color="green")
#    plt.legend(loc=2)
#    plt.savefig((namem + "YawRate"))
#    plt.show()   
#    
#    plt.figure(4)
#    plt.gca().set_ylim([-6,6])
##    plt.gca().set_xlim([0,140])    
#    plt.tick_params(axis="x", labelsize=15)
#    plt.tick_params(axis="y", labelsize=15)
#    plt.title("Aileron Deflection")
#    plt.plot(t, (name.delta_a_stab*180/np.pi), color="green")
#    plt.ylabel("$\delta_a$ [deg]")
#    plt.xlabel("t [s]")
#    plt.savefig((namem + "Ailerondeflection"))
#
#    
#    plt.figure(5)
#    plt.gca().set_ylim([-6,6])
##    plt.gca().set_xlim([0,140])    
#    plt.tick_params(axis="x", labelsize=15)
#    plt.tick_params(axis="y", labelsize=15)
#    plt.title("Rudder Deflection")
#    plt.plot(t, (name.delta_r_stab*180/np.pi), color="green")
#    plt.ylabel("$\delta_r$ [deg]")
#    plt.xlabel("t [s]")
#    plt.savefig((namem + "Rudder Deflection"))