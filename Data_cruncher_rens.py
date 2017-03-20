# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 10:06:39 2017

@author: Robin
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

time = np.genfromtxt('data/time[sec].txt', delimiter = ',')
dr = np.genfromtxt('data/delta_r[deg].txt', delimiter = '\n')
LatAcc = np.genfromtxt('data/Ahrs1_bLatAcc[g].txt', delimiter = '\n')

#in deze tijdspan word er iets spannends gedaan met de rudder
#waarschijnlijk maakte hij een bochtje
time_dieikwil = time[4.6*10**4 : 4.7*10**4]
dr_dieikwil = (np.pi/180.)*dr[4.6*10**4 : 4.7*10**4]
LatAcc_dieikwil = 9.81*6381.44136805*LatAcc[4.6*10**4 : 4.7*10**4]

CYdr = stats.linregress(dr_dieikwil, LatAcc_dieikwil)[0]

plt.plot(time_dieikwil, dr_dieikwil)
plt.show()



