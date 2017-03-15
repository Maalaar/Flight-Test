# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 10:02:52 2017

@author: Bart
"""
import numpy as np
import matplotlib.pyplot as plt
import cog


h_p     = np.array([18930.,17920.,17330.,16540.,17210.,17440.,17600.]) #ft
V_IAS   = np.array([158.,170.,180.,188.,149.,140.,130.]) #kts
a       = np.array([4.8,4.,3.3,2.8,5.7,6.6,7.9]) #deg
de      = np.array([-0.4,0.,0.3,0.5,-0.8,-1.2,-1.7]) #deg
detr    = np.array([3.1,3.1,3.1,3.1,3.1,3.1,3.1]) #deg
Fe      = np.array([-2.,19.,36.,59.,-23.,-30.,-42.]) #N
FFl     = np.array([389.,401.,405.,418.,402.,394.,393.]) #lbs/hr
FFr     = np.array([413.,426.,436.,446.,431.,425.,421.]) #lbs/hr
Fused   = np.array([956.,1000.,1020.,1037.,1063.,1081.,1105.]) #lbs
TAT     = np.array([-16.9,-13.8,-11.8,-9.7,-13.8,-14.8,-15.8]) #deg C
m_pass = np.array([99.,73.,60.,72.,73.,81.,79.,85.,85.]) #mass of pilots and passengers

lambda1 = -0.0065         # temperature gradient in ISA [K/m]
p0      = 101325. #Pa
Temp0   = 288.15          # temperature at sea level in ISA [K]
R       = 287.05          # specific gas constant [m^2/sec^2K]
g       = 9.81 #m/s^2
gamma   = 1.4
rho0    = 1.225
W_s     = 60500. #N
OEW     = 9165. #lbs
m_fuel_0 = 4150. #lbs
c       = 2.0569	          # mean aerodynamic cord [m]

ft_to_m = 0.3048
kts_to_ms = 0.514444
lbs_to_kg = 0.453592

TAT     = TAT+273.15 #convert to Kelvin
V_IAS   = V_IAS*kts_to_ms #convert to m/s
h_p     = h_p*ft_to_m
OEW     = OEW*lbs_to_kg
Fused   = Fused*lbs_to_kg
m_pass  = m_pass*lbs_to_kg
m_fuel_0 = m_fuel_0*lbs_to_kg

p       = p0*(1.+(lambda1*h_p/Temp0))**(-g/(lambda1*R))
M       = np.sqrt((2./(gamma-1.))*((((p0/p)*(((1.+(((gamma-1.)*rho0*V_IAS**2.)/(2*gamma*p0)))**(gamma/(gamma-1.)))-1.))+1.)**((gamma-1.)/gamma) -1.))
Temp    = TAT/(1.+(((gamma-1.)/2)*M**2.))
a_mach  = np.sqrt(gamma*R*Temp)
V_t     = M*a_mach
rho     = p/(R*Temp)
V_e     = V_t*np.sqrt(rho/rho0)

m       = OEW + m_fuel_0 + m_pass.sum() - Fused
W       = m*g
V_e_red = V_e*np.sqrt(W_s/W)

W1,cog1 = cog.cog([1140])
W2,cog2 = cog.cog2([1174])

dxcg    = cog2-cog1
de1     = -0.9--0.4


