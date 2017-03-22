# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 12:05:24 2017

inputs:
- h_p [ft] as float or array
- TAT [deg C] as float or array
- V_IAS [kts] as float or array

output:
- V_e [m/s]
- M [-] Mach number
"""
from constants import *
import numpy as np

def equivalentspeed(h_p, TAT, V_IAS):
    TAT     =   TAT+273.15 #convert to Kelvin
    V_IAS   =   V_IAS*kts_to_ms #convert to m/s
    h_p     =   h_p*ft_to_m    
    p       =   p0*(1.+(lambda1*h_p/Temp0))**(-g/(lambda1*R))
    M       =   np.sqrt((2./(gamma-1.))*((((p0/p)*(((1.+(((gamma-1.)*rho0*V_IAS**2.)/(2*gamma*p0)))**(gamma/(gamma-1.)))-1.))+1.)**((gamma-1.)/gamma) -1.))
    Temp    =   TAT/(1.+(((gamma-1.)/2)*M**2.))
    rho     =   p/(R*Temp)
    a_mach  =   np.sqrt(gamma*R*Temp)
    V_t     =   M*a_mach
    V_e     =   V_t*np.sqrt(rho/rho0)
    
    return V_e, V_t, rho, M

