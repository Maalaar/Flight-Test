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

#forces
CL = 2 * W / (rho * V ** 2 * S)   
CD = CD0 + (CLa * alpha) ** 2 / (np.pi * A * e)
CN = CL*np.cos(alpha) + CD*np.sin(alpha)
CT = CD*np.cos(alpha) - CL*np.sin(alpha)

#lecture 2 slide 17 & 22
Cmle = -CN*(e/c) 
Cmalphale = stats.linregress(alpha,Cmle)[0]
CNalphale = stats.linregress(alpha,CN)[0]
xle = 0.0254*261.56
xac = xle - c*Cmalphale/CNalphale
Cmac = -Cmle + CN*(xle-xac)/c

#more forces, lecture 3 slide 13 & 15
CTw = CT
xh = lh + xac
CNw = []
CNh = []

for j in range(1,len(xcg)):
    CNa = np.array([[1              , Vh_V**2*Sh_S           ],\
                    [(xcg[j]-xac)/c , Vh_V**2*Sh_S*(xcg[j]-xh)/c]])
    CNb = np.array([CN,-Cmac])
    CNw = np.linalg.solve(CNa,CNb)[0]
    CNh = np.linalg.solve(CNa,CNb)[1]

print CN
print CNw
print CNh