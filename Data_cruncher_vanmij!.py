# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 10:06:39 2017

@author: Robin
"""

import numpy as np
import matplotlib.pyplot as plt


time = np.genfromtxt('data/time[sec].txt', delimiter = ',')
v_tas = np.genfromtxt('data/V_tas[ms].txt', delimiter = '\n')
pitch_angle = np.genfromtxt('data/pitch_angle_[deg].txt', delimiter = '\n')
pitch_rate = np.genfromtxt('data/pitch_rate[degpers].txt', delimiter = '\n')
Wfl = np.genfromtxt('data/F_used_l[lbs].txt', delimiter = '\n')
Wfr = np.genfromtxt('data/F_used_r[lbs].txt', delimiter = '\n')

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
y_phugoid = v_tas[phugoid_index:phugoid_index+(mt_phugoid/step)]

x_short = np.arange(0, mt_short, step)
y_short = pitch_angle[short_index:short_index+(mt_short/step)]


plt.close()
plt.plot(x_phugoid,y_phugoid)
plt.show()



