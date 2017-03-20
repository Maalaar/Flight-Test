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

# Assigning coefficients to matrices
C1 = np.matrix([[-2*muc*(c/(V0**2)), 0, 0, 0],
                [0, (CZadot-2*muc)*(c/V0), 0, 0],
                [0, 0, -(c/V0), 0],
                [0, Cmadot*(c/V0), 0, -2*muc*KY2*(c/V0)**2]])

C2 = np.matrix([[CXu/V0, CXa, CZ0, 0],
                [CZu/V0, CZa, -CX0, (CZq + 2*muc)*(c/V0)],
                [0, 0, 0, (c/V0)],
                [Cmu/V0, Cma, 0, Cmq*(c/V0)]])
                
C3 = np.matrix([[CXde],
                [CZde],
                [0],
                [Cmde]])
 
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
delev = deltae *(np.pi/180) #input of elevator deflection
t = np.linspace(0,len(delev)*0.1, num=len(delev), endpoint=True, retstep=False) #time step and range 
Xinit = np.matrix([[0], [alpha0], [th0], [0]]) # initial values for control system
y, t, x = cs.lsim(sys, U=delev, T=t, X0=Xinit) # computing dybnamic stability


#plotting the total grpahs
plt.subplot(221)
plt.title('u')
plt.plot(t, y1)
plt.plot(t, v_tas)

plt.subplot(222)
plt.title('alpha')
plt.plot(t, y2)
plt.plot(t, AOA)


plt.subplot(223)
plt.title('Theta')
plt.plot(t, y3)
plt.plot(t, pitch)

plt.subplot(224)
plt.title('q')
plt.plot(t, y4)
plt.plot(t, rate)

plt.show()