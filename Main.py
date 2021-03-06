# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 13:35:19 2017

@author: Robin
"""
import numpy as np
import control.matlab as cs
from Cit_par import *
import matplotlib.pyplot as plt


#A = np.matrix([[1, 2], [2, 4]])
#B = np.matrix([[1], [2]])
#C = np.matrix([[3, 5], [1, 2]])
#D = np.matrix([[0], [0]])


C1 = np.matrix([[-2*muc*(c/V0**2), 0, 0, 0],
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
                
A = - np.linalg.inv(C1)*C2
B = - np.linalg.inv(C1)*C3

eig = np.linalg.eig(A)

C = np.matrix([[1, 0, 0, 0],
              [0, 1, 0, 0],
              [0, 0, 1, 0],
              [0, 0, 0, 1]])     

D = np.matrix([[0], [0], [0], [0]])

sys = cs.ss(A, B, C, D)

t = np.arange(0, 100, 0.1)

X0 = np.matrix([[1], [0], [0], [0]])

y1, t = cs.initial(sys, t, X0)


plt.plot(t, y1)

plt.show()