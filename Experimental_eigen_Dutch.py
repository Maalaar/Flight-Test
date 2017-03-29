# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 13:07:05 2017

@author: Robin
"""

import numpy as np
from Data_cruncher import *
import matplotlib.pyplot as plt

roll = DutchRollP.RollRate
roll = roll[325:525]
roll = roll - np.average(roll)
time = DutchRollP.time
time = time[325:525]
time = time-time[0]
time = time / 10.
V0 = DutchRollP.V0

#plt.plot(time, roll)
#plt.show()

#6 Peaks#

#shape (200,)

a1 = roll[0:33]
b1 = roll[33:66]
c1 = roll[66:99]
d1 = roll[99:132]
e1 = roll[132:165]
f1 = roll[165:200]

a2 = time[0:33]
b2 = time[33:66]
c2 = time[66:99]
d2 = time[99:132]
e2 = time[132:165]
f2 = time[165:200]

rollmax = []
rollmax.append(np.max(a1))
rollmax.append(np.max(b1))
rollmax.append(np.max(c1))
rollmax.append(np.max(d1))
rollmax.append(np.max(e1))
rollmax.append(np.max(f1))

timemax = []
timemax.append(a2[np.where(rollmax[0]==a1)[0][0]])
timemax.append(b2[np.where(rollmax[1]==b1)[0][0]])
timemax.append(c2[np.where(rollmax[2]==c1)[0][0]])
timemax.append(d2[np.where(rollmax[3]==d1)[0][0]])
timemax.append(e2[np.where(rollmax[4]==e1)[0][0]])
timemax.append(f2[np.where(rollmax[5]==f1)[0][0]])

timemax = np.array(timemax)

## Eigenvalue calculations ##

Period = 0.5 * (timemax[3]-timemax[1])
logdecrement = 1/2. * np.log(rollmax[2] / rollmax[4])
damping = 1 / np.sqrt(1 + ((2 * np.pi) / np.log(timemax[1]/timemax[2]))**2)

Chalftest = 0.11*np.sqrt(1-damping**2)/damping
Chalf =  0.693/logdecrement
Thalf = Chalf * Period

Xi = - (0.693 * c)/(Thalf * V0)
Eta = (2 * np.pi * c) / (V0 * Period)

eig = Xi + Eta*1j

A = 6 * rollmax[3]/(np.exp(eig*timemax[3]))

t = np.arange(0,20,0.1)
test = A * np.exp(eig*(V0/c)*t)

plt.plot(t, test)
plt.plot(timemax, rollmax)
plt.plot(time, roll)
plt.show()
