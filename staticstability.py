# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 09:58:52 2017

@author: rens
"""

#modules
import numpy as np

#imputs from drag polar measurements!
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
xcg = weightstuff[1] #meters

#forces
CL = 2 * W / (rho * V ** 2 * S)   
CD = CD0 + (CLa * alpha) ** 2 / (np.pi * A * e)
CN = CL*np.cos(alpha) + CD*np.sin(alpha)
CT = CD*np.cos(alpha) - CL*np.sin(alpha)

#lecture 2 slides 17 & 22
Cmle = -CN*(e/c)
from scipy import stats
Cmalphale = stats.linregress(alpha,Cmle)[0]
CNalphale = stats.linregress(alpha,CN)[0]
xle = 0.0254*261.56
xac = xle - c*Cmalphale/CNalphale
Cmac = -Cmle + CN*(xle-xac)/c

#introducing tail, lecture 3 slides 13 & 15
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

#some derivatives
from scipy import stats
CNwa   = stats.linregress(alpha,CNw)[0]
CNha   = stats.linregress(alpha,CNh)[0]
CNa    = stats.linregress(alpha,CN)[0]

#elevator stuff
#using the second measurement series instead of the first
#and a lot of the same stuff as done above, repeated
W_f2 = np.array([956., 1000., 1020., 1037., 1063., 1081., 1105.]) #lbs
V2 = 0.5144444*np.array([158., 170., 180., 188., 149., 140., 130.])
alpha2 = (np.pi/180.)*np.array([4.8, 4., 3.3, 2.8, 5.7, 6.6, 7.9])
de = (np.pi/180.)*np.array([-0.4, 0., 0.3, 0.5, -0.8, -1.2, -1.7]) #rad

weightstuff2 = cog(W_f2)
W2 = weightstuff2[0] #Newton
xcg2 = weightstuff2[1] #meters

CL2 = 2 * W2 / (rho * V2 ** 2 * S)   
CD2 = CD0 + (CLa * alpha2) ** 2 / (np.pi * A * e)
CN2 = CL2*np.cos(alpha2) + CD2*np.sin(alpha2)
CT2 = CD2*np.cos(alpha2) - CL2*np.sin(alpha2)

Cmle2 = -CN2*(e/c)
from scipy import stats
Cmalphale2 = stats.linregress(alpha2,Cmle2)[0]
CNalphale2 = stats.linregress(alpha2,CN2)[0]
xac2 = xle - c*Cmalphale2/CNalphale2
Cmac2 = -Cmle2 + CN2*(xle-xac2)/c

CTw2 = CT2
CNw2 = []
CNh2 = []
for j in range(1,len(xcg2)):
    CNa2 = np.array([[1               , Vh_V**2*Sh_S               ],\
                    [(xcg2[j]-xac2)/c , Vh_V**2*Sh_S*(xcg2[j]-xh)/c]])
    CNb2 = np.array([CN2,-Cmac2])
    CNw2 = np.linalg.solve(CNa2,CNb2)[0]
    CNh2 = np.linalg.solve(CNa2,CNb2)[1]

CNhde = stats.linregress(de,CNh2)[0]
CNde  = stats.linregress(de,CN2)[0]