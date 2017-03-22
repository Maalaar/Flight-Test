# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 10:06:39 2017

@author: Robin
"""

import numpy as np
import matplotlib.pyplot as plt
from Eq_airspeed import *


#importing all measured data from text files into numpy arrays
time = np.genfromtxt('data/time[sec].txt', delimiter = ',')
v_tas = np.genfromtxt('data/V_tas[kts].txt', delimiter = '\n') #kts
v_ias = np.genfromtxt('data/V_cas[kts].txt', delimiter = '\n') #kts
pitch_angle = np.genfromtxt('data/pitch_angle_[deg].txt', delimiter = '\n') #deg
pitch_rate = np.genfromtxt('data/pitch_rate[degpers].txt', delimiter = '\n') #deg/s
Wfl = np.genfromtxt('data/F_used_l[lbs].txt', delimiter = '\n') #lbs
Wfr = np.genfromtxt('data/F_used_r[lbs].txt', delimiter = '\n') #lbs
AoA = np.genfromtxt('data/AOA[deg].txt', delimiter ='/n') #deg
deltae = np.genfromtxt('data/delta_e[deg].txt', delimiter ='/n') #deg
roll_rate = np.genfromtxt('data/roll_rate[degpers].txt', delimiter ='/n') #deg
yaw_rate = np.genfromtxt('data/yaw_rate[degpers].txt', delimiter ='/n') #deg
delta_r  = np.genfromtxt('data/delta_r[deg].txt', delimiter ='/n') #deg
delta_a  = np.genfromtxt('data/delta_a[deg].txt', delimiter ='/n') #deg
h_p = np.genfromtxt('data/h_p[ft].txt', delimiter ='/n') #deg
TAT = np.genfromtxt('data/TAT[degc].txt', delimiter ='/n') #degc

#converting to meric system
Wfl = 0.45359237*Wfl #lbs to kg
Wfr = 0.45359237*Wfr

#Total fuel
Wf = Wfl + Wfr




#######    symetric motion  ########
step = 0.1

#phugoid motion
phugoid_time = 3600.*1. + 60.*15. + 30.
phugoid_mt = 200
phugoid_index = np.where(time==phugoid_time)[0][0]
phugoid_deltae = deltae[phugoid_index:phugoid_index+(phugoid_mt/step)]
phugoid_height = h_p[phugoid_index:phugoid_index+(phugoid_mt/step)]
phugoid_TAT = TAT[phugoid_index:phugoid_index+(phugoid_mt/step)]
phugoid_speed = v_ias[phugoid_index:phugoid_index+(phugoid_mt/step)]
phugoid_eq_speed=equivalentspeed(phugoid_height, phugoid_TAT, phugoid_speed)
phugoid_AoA = AoA[phugoid_index:phugoid_index+(phugoid_mt/step)]


#short period
short_time = 3600.*1. + 60.*14. + 24.
short_mt = 6
short_index = np.where(time==short_time)[0][0]
short_deltae = deltae[short_index:short_index+(short_mt/step)]

#       assymetric motion

#dutch roll
DR_time =3600.*1. + 60.*10. + 40.
DR_mt = 400
DR_index = np.where(time==DR_time)[0][0]
DR_delta_r = delta_r[DR_index:DR_index+(DR_mt/step)]
DR_delta_a = delta_a[DR_index:DR_index+(DR_mt/step)]

#dutch roll YD
DRY_time =3600.*1. + 60.*12. + 0.    
DRY_mt = 400
DRY_index = np.where(time==DRY_time)[0][0]
DRY_delta_r = delta_r[DRY_index:DRY_index+(DRY_mt/step)]
DRY_delta_a = delta_a[DRY_index:DRY_index+(DRY_mt/step)]


#aper roll
APR_time =3600.*1. + 60.*19. + 0.
APR_mt = 400
APR_index = np.where(time==APR_time)[0][0]
APR_delta_r = delta_r[APR_index:APR_index+(APR_mt/step)]
APR_delta_a = delta_a[APR_index:APR_index+(APR_mt/step)]


#Spiral
SPRL_time =3600.*1. + 60.*21. + 50.
SPRL_mt = 400
SPRL_index = np.where(time==APR_time)[0][0]
SPRL_delta_r = delta_r[SPRL_index:SPRL_index+(SPRL_mt/step)]
SPRL_delta_a = delta_a[SPRL_index:SPRL_index+(SPRL_mt/step)]








