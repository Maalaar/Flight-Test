# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 10:06:39 2017

@author: Robin
"""

import numpy as np
import matplotlib.pyplot as plt
from Eq_airspeed.py import *


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

#converting to meric system
v_tas*=0.51444444 #kts to m/s
v_ias*=0.51444444 
Wfl = 0.45359237*Wfl #lbs to kg
Wfr = 0.45359237*Wfr

#Total fuel
Wf = Wfl + Wfr




#######    symetric motion  ########
step = 0.1

#phugoid motion
time_phugoid = 3600.*1. + 60.*15. + 40.
mt_phugoid = 200
phugoid_index = np.where(time==time_phugoid)[0][0]
deltae = deltae[phugoid_index:phugoid_index+(mt_phugoid/step)]

V_motion=equivalentspeed()

#short period
time_short = 3600.*1. + 60.*14. + 34.
mt_short = 6
short_index = np.where(time==time_short)[0][0]
deltae = deltae[short_index:short_index+(mt_short/step)]

#       assymetric motion

#dutch roll
time_DR =3600.*1. + 60.*10. + 50.
mt_DR = 400
DR_index = np.where(time==time_DR)[0][0]

#dutch roll YD
time_DRY =3600.*1. + 60.*12. + 10.    



#aper roll
time_APR =3600.*1. + 60.*19. + 10.



#Spiral
time_SPRL =3600.*1. + 60.*22. + 0.


x = []
y = []












v_tas = v_tas[phugoid_index:phugoid_index+(mt_phugoid/step)]
pitch = pitch_angle[phugoid_index:phugoid_index+(mt_phugoid/step)]
rate = pitch_rate[phugoid_index:phugoid_index+(mt_phugoid/step)]
AOA = AoA[phugoid_index:phugoid_index+(mt_phugoid/step)]
RR_DR=RR[DR_index:DR_index+(mt_DR/step)]
YR_DR=YR[DR_index:DR_index+(mt_DR/step)]
delta_r=delta_r[DR_index:DR_index+(mt_DR/step)]
delta_a=delta_a[DR_index:DR_index+(mt_DR/step)]

x_short = np.arange(0, mt_short, step)
y_short = pitch_angle[short_index:short_index+(mt_short/step)]

x_DR = np.linspace(0,len(delta_a)*0.1, num=len(delta_r), endpoint=True, retstep=False) #time step and range 
y_DR = delta_r

plt.close()
plt.plot(x_DR,y_DR)
plt.show()



