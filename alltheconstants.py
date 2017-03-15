# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 11:53:33 2017

@author: rensv
"""

#imports
import numpy as np
from Cit_par import *

#inputs
L = 1
D = 1
T = 1
a = np.pi/180.
a0 = 0
ip = 0
rho = 1
V = 1

#basics, notes eq 7-1
CL = L/(0.5*rho*V**2*S)
CD = D/(0.5*rho*V**2*S)
Tc = T/(0.5*rho*V**2*S)

CX = CL*np.sin(a) - CD*np.cos(a) + Tc
CZ = -CL*np.cos(a) - CD*np.sin(a) - Tc*(a0+ip)


#derivatives with respect to airspeed
CX0    = -CD + Tc #notes eq 7-2
CXu    = (T-D)/(rho*V**3*S) #notes eq 7-5
CXa    = -0.47966
CXadot = +0.08330
CXq    = -0.28170
CXde   = -0.03728

CZ0    = -CL - Tc*(a0+ip) #notes eq 7-2
CZu    = (-L-T*(a0+ip))/(rho*V**3*S) #notes eq 7-7
CZa    = -5.74340
CZadot = -0.00350
CZq    = -5.66290
CZde   = -0.69612

Cmu    = +0.06990
Cmadot = +0.17800
Cmq    = -8.79415

CYb    = -0.7500
CYbdot =  0     
CYp    = -0.0304
CYr    = +0.8495
CYda   = -0.0400
CYdr   = +0.2300

Clb    = -0.10260
Clp    = -0.71085
Clr    = +0.23760
Clda   = -0.23088
Cldr   = +0.03440

Cnb    =  +0.1348
Cnbdot =   0     
Cnp    =  -0.0602
Cnr    =  -0.2061
Cnda   =  -0.0120
Cndr   =  -0.0939