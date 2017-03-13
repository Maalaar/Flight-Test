# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 09:58:52 2017

@author: rens
"""

#modules
import numpy as np
from scipy import stats

#imputs from measurements
W_f = np.array([741., 778., 805., 829., 872., 896.]) #lbs
alpha = (np.pi/180.)*np.array([1.1, 1.5, 2.5, 4.5, 7.3, 10.8]) #rad
V = 0.5144444*np.array([240, 224, 194, 163, 136, 115]) #m/s
rho19000 = 0.675127

#parameters from data processing
from Cit_par import *

#weight & cg
from cog import *
weightstuff = cog(W_f)
W = weightstuff[0] #Newton
m = W/g #kg
xcg = weightstuff[1] #meters

print W
print xcg

#forces
CL = 2 * W / (rho * V ** 2 * S)   
CD = CD0 + (CLa * alpha) ** 2 / (np.pi * A * e)
CN = CL*np.cos(alpha) + CD*np.sin(alpha)
CT = CD*np.cos(alpha) - CL*np.sin(alpha)

#lecture 2 slide 17
Cmle = -CN*(e/c) 

#lecture 2 slide 22
Cmalphale = stats.linregress(alpha,Cmle)[0]
CNalphale = stats.linregress(alpha,CN)[0]
xle = 0.0254*261.56
xac = xle - c*Cmalphale/CNalphale
Cmac = -Cmle + CN*(xle-xac)/c