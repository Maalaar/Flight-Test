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
M = np.array([ 0.5156014 ,  0.48228907,  0.41898428,  0.35321723,  0.29534562, 0.24997917])
gamma = 1.4
lambda1 = -0.0065         # temperature gradient in ISA [K/m]
Temp0  = 288.15          # temperature at sea level in ISA [K] 
ft_to_m = 0.3048
lbs_to_kg = 0.453592
Temp = np.array([ 250.05484366,  250.30564387,  250.16675414,  250.40185229,
        250.57845661,  250.51903388])

TAT = TAT+273.15 #convert to Kelvin
h_p = h_p*ft_to_m
FF_l = FF_l*lbs_to_kg/3600.
FF_r = FF_r*lbs_to_kg/3600.

T_s = Temp

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

