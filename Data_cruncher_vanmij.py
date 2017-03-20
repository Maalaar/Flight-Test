# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 10:06:39 2017

@author: Robin
"""

import numpy as np
import matplotlib.pyplot as plt


time = np.genfromtxt('data/time[sec].txt', delimiter = ',')
v_tas = np.genfromtxt('data/V_tas[kts].txt', delimiter = '\n') #kts
pitch_angle = np.genfromtxt('data/pitch_angle_[deg].txt', delimiter = '\n') #deg
pitch_rate = np.genfromtxt('data/pitch_rate[degpers].txt', delimiter = '\n') #deg/s
Wfl = np.genfromtxt('data/F_used_l[lbs].txt', delimiter = '\n') #lbs
Wfr = np.genfromtxt('data/F_used_r[lbs].txt', delimiter = '\n') #lbs
AoA = np.genfromtxt('data/AOA[deg].txt', delimiter ='/n') #deg
deltae = np.genfromtxt('data/delta_e[deg].txt', delimiter ='/n') #deg

v_tas = 0.5144444*v_tas


Wfl = 0.45359237*Wfl
Wfr = 0.45359237*Wfr





Wf = Wfl + Wfr

#plt.plot(time, v_tas)
#plt.show()

time_phugoid = 3600.*1. + 60.*15. + 40.
time_short = 3600.*1. + 60.*14. + 34.

x = []
y = []

mt_short = 6
mt_phugoid = 200
step = 0.1

phugoid_index = np.where(time==time_phugoid)[0][0]
short_index = np.where(time==time_short)[0][0]



x_phugoid = np.arange(0, mt_phugoid, step)
deltae = deltae[phugoid_index:phugoid_index+(mt_phugoid/step)]
v_tas = v_tas[phugoid_index:phugoid_index+(mt_phugoid/step)]
pitch = pitch_angle[phugoid_index:phugoid_index+(mt_phugoid/step)]
rate = pitch_rate[phugoid_index:phugoid_index+(mt_phugoid/step)]
AOA = AoA[phugoid_index:phugoid_index+(mt_phugoid/step)]

x_short = np.arange(0, mt_short, step)
y_short = pitch_angle[short_index:short_index+(mt_short/step)]


#plt.close()
#plt.plot(x_phugoid,y_phugoid)
#plt.show()



