# -*- coding: utf-8 -*-
"""
Created on Thu Mar 09 15:07:22 2017

@author: Bart
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

OEW = 9165. #lbs
F_used = np.array([741.,778.,805.,829.,872.,896.]) #lbs
rho_0 = 1.225 #kg/m^3
V_IAS = np.array([240.,224.,194.,163.,136.,115.]) #kts
S = 30. #m^2
lbs_to_kg = 0.453592
kts_to_ms = 0.514444
ft_to_m = 0.3048
m_pass = np.array([99.,73.,60.,72.,73.,81.,79.,85.,85.]) #mass of pilots and passengers
m_fuel_0 = 4150. #lbs
g = 9.81 #m/s^2
Thrust = np.genfromtxt('thrustCLCD.dat')
b      = 15.911
A      = b ** 2 / S 
a = np.array([1.1,1.5,2.5,4.5,7.3,10.8])
p0 = 101325. #Pa
h_p = np.array([19000.,19010.,18990.,19000.,18990.,18960.]) #ft
lambda1 = -0.0065         # temperature gradient in ISA [K/m]
Temp0  = 288.15          # temperature at sea level in ISA [K]
gamma = 1.4
R      = 287.05          # specific gas constant [m^2/sec^2K]
rho0   = 1.2250          # air density at sea level [kg/m^3]
TAT = np.array([-9.8,-11.2,-14.2,-16.5,-18.2,-19.5]) #deg C

V_IAS = V_IAS*kts_to_ms #convert to m/s
OEW = OEW*lbs_to_kg #convert to kg
F_used = F_used*lbs_to_kg #convert to kg
m_fuel_0 = m_fuel_0*lbs_to_kg 
a = a*np.pi/180. #convert to rad
h_p = h_p*ft_to_m
TAT = TAT+273.15 #convert to Kelvin

p = p0*(1.+(lambda1*h_p/Temp0))**(-g/(lambda1*R))
M = np.sqrt((2./(gamma-1.))*((((p0/p)*(((1.+(((gamma-1.)*rho0*V_IAS**2.)/(2*gamma*p0)))**(gamma/(gamma-1.)))-1.))+1.)**((gamma-1.)/gamma) -1.))
Temp = TAT/(1.+(((gamma-1.)/2)*M**2.))
a_mach = np.sqrt(gamma*R*Temp)
V_t = M*a_mach
rho = p/(R*Temp)
V_e = V_t*np.sqrt(rho/rho0)

C_L = []
for i in range(V_IAS.size):
    m = OEW + m_fuel_0 - F_used[i] + m_pass.sum()
    W = m*g
    CL = W/(0.5*rho_0*S*(V_e[i])**2.)
    C_L.append(CL)
C_L = np.array(C_L)

Thrust_total = np.sum(Thrust, axis = 1)

C_D = []
for i in range(V_IAS.size):
    CD = Thrust_total[i]/(0.5*rho_0*S*V_e[i]**2)
    C_D.append(CD)
C_D = np.array(C_D)

slope, intercept, r_value, p_value, std_err = stats.linregress(C_L**2.,C_D)
line = slope*(C_L**2.)+intercept

C_D0 = intercept
e = 1./(np.pi*A*slope)

C_L1 = np.linspace(0.,1.2,13)
C_D1 = C_D0 + (C_L1**2)/(np.pi*A*e)

#plt.plot(C_D1,C_L1)
#plt.scatter(C_D,C_L)
#plt.show()

CLa, intercept1, r_value1, p_value1, std_err1 = stats.linregress(a,C_L)