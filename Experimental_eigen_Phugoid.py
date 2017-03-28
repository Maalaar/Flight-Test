# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 13:07:05 2017

@author: Robin
"""

import numpy as np
from Data_cruncher import *
import matplotlib.pyplot as plt

pitch = phugoidP.PitchAngle
pitch = pitch[250:2000]
pitch = pitch - np.average(pitch)
time = phugoidP.time
time = time[250:2000]
time = time-time[0]
time = time / 10.
V0 = phugoidP.V0

#plt.plot(time, pitch)
#plt.show()

#4 Peaks#

#shape (2000,)

a1 = pitch[0:430]
b1 = pitch[430:860]
c1 = pitch[860:1290]
d1 = pitch[1290:1750]

e1 = time[0:430]
f1 = time[430:860]
g1 = time[860:1290]
h1 = time[1290:1750]

pitchmax = []
pitchmax.append(np.max(a1))
pitchmax.append(np.max(b1))
pitchmax.append(np.max(c1))
pitchmax.append(np.max(d1))

timemax = []
timemax.append(e1[np.where(pitchmax[0]==a1)[0][0]])
timemax.append(f1[np.where(pitchmax[1]==b1)[0][0]])
timemax.append(g1[np.where(pitchmax[2]==c1)[0][0]])
timemax.append(h1[np.where(pitchmax[3]==d1)[0][0]])

timemax = np.array(timemax)

## Eigenvalue calculations ##

Period = 0.5 * (timemax[3]-timemax[1])
logdecrement = 1/2. * np.log(pitchmax[1] / pitchmax[3])
damping = 1 / np.sqrt(1 + ((2 * np.pi) / np.log(timemax[1]/timemax[2]))**2)

Chalftest = 0.11*np.sqrt(1-damping**2)/damping
Chalf =  0.693/logdecrement
Thalf = Chalf * Period

Xi = - (0.693 * c)/(Thalf * V0)
Eta = (2 * np.pi * c) / (V0 * Period)

eig = Xi + Eta*1j

A = 2* pitchmax[2]/(np.exp(eig*timemax[2]))

t = np.arange(0,175,0.1)
test = A * np.exp(eig*(V0/c)*t)

plt.plot(t, test)
plt.plot(time, pitch)
plt.show()
