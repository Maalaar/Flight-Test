# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 13:35:19 2017

@author: Robin
"""
import numpy as np
import control.matlab as cs
from Cit_par import *
import matplotlib.pyplot as plt

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


t = np.arange(0, 1000, 0.1) #time step and range 
Xinit = np.matrix([[0], [alpha0], [th0], [0]]) # initial values for control system
delev=1 # elevator deflection angle
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

#eig = np.linalg.eig(A)
#eigenvalue = eig[0]
#eigenvector = eig[1]
#
#xi = eigenvalue.real
#eta = eigenvalue.imag
#
#P = (2*np.pi)/eta * (c/V0)


plt.subplot(221)
plt.title('u')
plt.plot(t, y1)

plt.subplot(222)
plt.title('alpha')
plt.plot(t, y2)

plt.subplot(223)
plt.title('Theta')
plt.plot(t, y3)

plt.subplot(224)
plt.title('q')
plt.plot(t, y4)

#plt.plot(t, y)

plt.show()