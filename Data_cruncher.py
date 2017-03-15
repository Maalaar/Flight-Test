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

#plt.plot(time, v_tas)
#plt.show()

time_phugoid = 3600.*1. + 60.*15. + 40.
time_short = 3600.*1. + 60.*14. + 32.

x = []
y = []

mt_short = 6
mt_phugoid = 200
step = 0.1

phugoid_index = np.where(time==time_phugoid)[0][0]
short_index = np.where(time==time_short)[0][0]



x_phugoid = np.arange(0, mt_phugoid, step)
y_phugoid = pitch_angle[phugoid_index:phugoid_index+(mt_phugoid/step)]

x_short = np.arange(0, mt_short, step)
y_short = pitch_rate[short_index:short_index+(mt_short/step)]



plt.plot(x_short,y_short)
plt.show()



