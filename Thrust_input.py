# -*- coding: utf-8 -*-
"""
Created on Thu Mar 09 16:00:07 2017

@author: Bart
"""

import numpy as np

index = np.array([23081,24211,25201,26501,28481,29701])
h_p = np.array([19000.,19010.,18990.,19000.,18990.,18960.]) #ft
FF_l = np.array([693.,637.,527.,438.,383.,367.]) #lbs/hr
FF_r = np.array([756.,681.,548.,468.,394.,398.]) #lbs/hr
TAT = np.array([-9.8,-11.2,-14.2,-16.5,-18.2,-19.5]) #deg C
M = np.array([0.5188,0.4851,0.4303,0.3551,0.2933,0.2500]) 
gamma = 1.4
lambda1 = -0.0065         # temperature gradient in ISA [K/m]
Temp0  = 288.15          # temperature at sea level in ISA [K] 
ft_to_m = 0.3048
lbs_to_kg = 0.453592


TAT = TAT+273.15 #convert to Kelvin
h_p = h_p*ft_to_m
FF_l = FF_l*lbs_to_kg/3600.
FF_r = FF_r*lbs_to_kg/3600.


T_s = []
for i in range(TAT.size):
    Ts = TAT[i]/(1.+(((gamma-1.)/2)*M[i]*M[i]))
    T_s.append(Ts)
T_s = np.array(T_s)

T_IAS = []
for i in range(h_p.size):
    TIAS = Temp0 + (lambda1*h_p[i])
    T_IAS.append(TIAS)
T_IAS = np.array(T_IAS)

dT_IAS = np.subtract(T_s,T_IAS)

matrix = np.zeros([dT_IAS.size,5])


matrix[:,0] = h_p
matrix[:,1] = M
matrix[:,2] = dT_IAS
matrix[:,3] = FF_l
matrix[:,4] = FF_r

np.savetxt('matlab.dat',matrix,delimiter=' ')

