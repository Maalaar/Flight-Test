# -*- coding: utf-8 -*-
"""
Created on Thu Mar 09 15:07:22 2017

@author: Bart
"""
import numpy as np
import matplotlib.pyplot as plt

OEW = 9165. #lbs
F_used = np.array([741.,778.,805.,829.,872.,896.]) #lbs
rho_0 = 1.225 #kg/m^3
V_IAS = np.array([240.,224.,194.,163.,136.,115.]) #kts
S = 30. #m^2
lbs_to_kg = 0.453592
kts_to_ms = 0.514444
m_pass = np.array([99.,73.,60.,72.,73.,81.,79.,85.,85.]) #mass of pilots and passengers
m_fuel_0 = 4150. #lbs
g = 9.81 #m/s^2
Thrust = np.genfromtxt('thrust.dat')


V_IAS = V_IAS*kts_to_ms #convert to m/s
OEW = OEW*lbs_to_kg #convert to kg
F_used = F_used*lbs_to_kg #convert to kg
m_fuel_0 = m_fuel_0*lbs_to_kg 


C_L = []
for i in range(V_IAS.size):
    m = OEW + m_fuel_0 - F_used[i] + m_pass.sum()
    W = m*g
    CL = W/(0.5*rho_0*S*(V_IAS[i])**2.)
    C_L.append(CL)
C_L = np.array(C_L)

Thrust_total = np.sum(Thrust, axis = 1)

C_D = []
for i in range(V_IAS.size):
    CD = Thrust_total[i]/(0.5*rho_0*S*V_IAS[i]**2)
    C_D.append(CD)
C_D = np.array(C_D)

plt.plot(C_L**2.,C_D)
plt.show()