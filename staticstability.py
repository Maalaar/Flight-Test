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
CL =  W / (0.5 * rho * V ** 2 * S)   
CD = CD0 + (CLa * alpha) ** 2 / (np.pi * A * e)
CN = CL*np.cos(alpha) + CD*np.sin(alpha)
CT = CD*np.cos(alpha) - CL*np.sin(alpha)

#lecture 2 slides 17 & 22
xle = 0.0254*261.56
mac = 0.0254*80.98
xac = xle + 0.25*mac #assuming ac at 25% mac
Cmac = (xcg-xac)*CN #CG as reference point

#introducing tail, lecture 3 slides 13 & 15
CTw = CT
xh = lh + xac
CNh = (c / (Vh_V**2 * Sh_S * lh)) * (-Cmac - CN*(xcg-xac)/c)
CNw = CN - CNh * Vh_V**2 * Sh_S

#some derivatives
CNa = -CL*np.sin(alpha) + CD*np.cos(alpha)
CNha = CNa*(xcg-xac)/(Vh_V**2 * Sh_S * lh)
CNwa = CNa - CNha*Vh_V**2*Sh_S

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

Cmac2 = (xcg2-xac)*CN2

CTw2 = CT2
CNh2 = (c / (Vh_V**2 * Sh_S * lh)) * (-Cmac2 - CN2*(xcg2-xac)/c)
CNw2 = CN2 - CNh2 * Vh_V**2 * Sh_S

CNa2 = -CL2*np.sin(alpha2) + CD2*np.cos(alpha2)
CNha2 = CNa2*(xcg2-xac)/(Vh_V**2 * Sh_S * lh)
CNwa2 = CNa2 - CNha2*Vh_V**2*Sh_S

deda = 2*CLa/(np.pi*A)
#downwash derivative d(eta)/d(alpha) is required for some of these derivatives
#this formula comes from the notes page 325 and provides a "rough estimate"
#assumptions made: 
#   eliptical lift distribution
#   attached, non-separated flow
#   this is a nice approximation for A>5, which is true for the citation

alphah = alpha2 - (alpha2 - alpha0)*deda + ih
CNhde = CNha2*alphah/de 