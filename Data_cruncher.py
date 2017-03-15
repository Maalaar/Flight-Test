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

x = []
y = []

mt = 200
step = 0.1

j = np.where(time==time_phugoid)
j = j[0]
j=j[0]

x = np.arange(0, mt, step)
y = pitch_angle[j:j+(mt/step)]

#for i in time:
#    if time_phugoid-5 <= time[i] <= time_phugoid + 5:
#        j = np.arange(i,mt+i,step)
#        while i <= i+mt:
#            x.append(time[i])
#            y.append(v_tas[i])
#            i = i + step
#        i = i + mt
#    else:
#        print 'noobie'


plt.plot(x,y)
plt.show()



