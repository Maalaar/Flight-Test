# -*- coding: utf-8 -*-
"""
Created on Thu Mar 09 15:07:22 2017

@author: Bart
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from constants import *
import Eq_airspeed

#Recorded values during flight test
F_used = np.array([741.,778.,805.,829.,872.,896.]) #lbs
V_IAS = np.array([240.,224.,194.,163.,136.,115.]) #kts
m_pass = np.array([99.,73.,60.,72.,73.,81.,79.,85.,85.]) #mass of pilots and passengers
Thrust = np.genfromtxt('thrustCLCD.dat')
a = np.array([1.1,1.5,2.5,4.5,7.3,10.8])
h_p = np.array([19000.,19010.,18990.,19000.,18990.,18960.]) #ft
TAT = np.array([-9.8,-11.2,-14.2,-16.5,-18.2,-19.5]) #deg C

#Convert values to SI-units
OEW = OEW*lbs_to_kg 
F_used = F_used*lbs_to_kg 
m_fuel_0 = m_fuel_0*lbs_to_kg 
a = a*np.pi/180. 

#Calculate equivalent airspeed
V_e, M = Eq_airspeed.equivalentspeed(h_p, TAT, V_IAS)

#Calculate lift-coefficient for all data-points
C_L = []
for i in range(V_IAS.size):
    m = OEW + m_fuel_0 - F_used[i] + m_pass.sum()
    W = m*g
    CL = W/(0.5*rho_0*S*(V_e[i])**2.)
    C_L.append(CL)
C_L = np.array(C_L)

#Sum the thrust of the two engines for all data-points
Thrust_total = np.sum(Thrust, axis = 1)

#Calculate drag-coefficient for all data-points
C_D = []
for i in range(V_IAS.size):
    CD = Thrust_total[i]/(0.5*rho_0*S*V_e[i]**2)
    C_D.append(CD)
C_D = np.array(C_D)

#Calculate zero-lift drag and Oswald factor.
slope, intercept, r_value, p_value, std_err = stats.linregress(C_L**2.,C_D)
C_D0 = intercept
e = 1./(np.pi*A*slope)

#Calculate CD according to CL-CD relation
C_L1 = np.linspace(0.,1.2,13)
C_D1 = C_D0 + (C_L1**2)/(np.pi*A*e)

#plt.plot(C_D1,C_L1)
#plt.scatter(C_D,C_L)
#plt.show()

#calculate CLa
CLa, intercept1, r_value1, p_value1, std_err1 = stats.linregress(a,C_L)