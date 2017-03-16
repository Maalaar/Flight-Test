# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 11:53:33 2017

@author: rensv
"""

#imports
import numpy as np
from cog import *
from Cit_par import *

#inputs #this example: third drag polar measurement
Wf     = [805.]
V      = 194.
a      = np.pi/180.
gamma0 = 0 #flight path = straight forward, no altitude change
rho    = 0.675127 #19000ft
deda   = 0 #downwash??????

#basic forces
W = float(cog(Wf)[0])
xcg = float(cog(Wf)[1])

CL = W/(0.5 * rho * V**2 * S)
CD = CD = CD0 + (CLa * a) ** 2 / (np.pi * A * e)

Tc = -CD #level flight, thrust = drag

CN = CL*np.cos(a) + CD*np.sin(a)
CT = CD*np.cos(a) - CL*np.sin(a)

#longitudinal stability, as done in staticstability.py as well, but now for one value
from staticstability import Cmalphale, CNalphale
Cmle = -CN*(e/c)
xle = 0.0254*261.56 #appendix C
xac = xle - c*Cmalphale/CNalphale
Cmac = -Cmle + CN*(xle-xac)/c
CTw = CT
xh = lh + xac
CNa = np.array([[1           , Vh_V**2*Sh_S           ],\
                [(xcg-xac)/c , Vh_V**2*Sh_S*(xcg-xh)/c]])
CNb = np.array([CN,-Cmac])
CNw = np.linalg.solve(CNa,CNb)[0]
CNh = np.linalg.solve(CNa,CNb)[1]
  
  
######################################
##### SYMMETRIC FLIGHT CONSTANTS #####
##### from the FD lecture notes  #####
##### starting at page 161       #####
######################################


CX0 = CL*np.sin(gamma0) 
#notes page 163
#this is zero if the flight path angle is 0 at 0 AoA
#which should be true because we don't gain altitude during this part of the flight test


CZ0 = CL*np.sin(gamma0) 
#notes page 163
#this is equal to CL if the flight path angle is 0 at 0 AoA
#which should be true because we don't gain altitude during this part of the flight test


Cm0 = 0
#notes page 163
#balanced flight, zo no moments around CG


CXu = -2*CD
CZu = -2*CL
CMu = 0
#notes page 168 & 187
#assumptions: 
#   flight path angle 0 
#   Tc = CD
#   dCm/dTc = 0, moment does not change if thrust changes
#   subsonic, neglecting compressibility (p166)
#   neglecting slipstream effect (p166)
#   power produced independent of airspeed at constant throttle setting (p167)


CXa = CL*(1-2*CLa/(np.pi*A*e))
#notes page 170
#pretty straightforward


CZa = -CNwa - CNha*(1-deda)*(Vh_V**2)*Sh_S
#notes page 170
#can be simplified to: CZa = -CLa - CD
#but this version is more complete, including the tail
#also: DOWNASH??????


from staticstability import CNwa, CNha
CMa    = CNwa*(xcg-xac)/c - CNha*(1-deda)*(Vh_V**2)*(Sh*lh)/(S*c)
#notes page 173
#using data from drag polar measurements during flight test
#DOWNWASH?????????


CXq = 0
#notes page 179
#literally says: is always neglected


CZq = -2*CNha*(Vh_V**2)*Sh*lh/(S*c)
#notes page 181
#"a rough estimate"


Cmq = -1.15*CNha*(Vh_V**2)*Sh*(lh**2)/(S*(c**2))
#notes page 181
#assuming straight slender wing
#"for conventional aircraft"


CZadot = -CNha*(Vh_V**2)*deda*Sh*lh     /(S*c)
Cmadot = -CNha*(Vh_V**2)*deda*Sh*(lh**2)/(S*(c**2))
#notes page 185
#neglecting higher order derivatives of alpha
#DOWNWASH???????


CXde = 0
#notes page 185
#"commonly neglected" in subsonic flight


CNhde = 1 #<-- PLACEHOLDER! 
CZde = -CNhde*(Vh_V**2)*Sh_S
#notes page 186


CNde = 1 #<-- PLACEHOLDER! 
Cmde = -CNde*(Vh_V**2)*Sh*lh/(S*c)
#notes page 186



#######################################
##### ASYMMETRIC FLIGHT CONSTANTS #####
##### from the FD lecture notes   #####
##### starting at page 188        #####
#######################################

#most of the derivatives were taken from figures with expirimental data of the Citation
#why? because deriving them analytically takes a lot of time, and we only have 3 weeks
#also, a lot of assumptions are made when calculating them analytically
#which would result in a lot of errors anyway


blist = (np.pi/180.)*np.array([-10., -7.75, -4.5, -2.25, 0, 2.25, 4.5, 7.75, 10.])
CYlist = [0.08, 0.06, 0.04, 0.02, 0, -0.02, -0.04, -0.06, -0.08]
CYb = stats.linregress(blist,CYlist)[0]
#notes page 295
#data taken from figure 8-6


CYbdot = 0
#figure used above shows a linear relation, so first derivative constant, so second derivative = 0


Cllist = [0.02, 0.15, 0.01, 0.005, 0, -0.005, -0.01, -0.015, -0.02]
Clb = stats.linregress(blist,Cllist)[0]
#notes page 204
#data taken from figure 8-14


Cnlist = [-0.015, -0.012, -0.007, -0.004, 0, 0.004, 0.007, 0.012, 0.015]
Cnb = stats.linregress(blist,Cnlist)[0]
#notes page 212
#data taken from figure 8-24


Cnbdot = 0
#notes page 212
#neglected for A > 5


CYlist2 = [0.014, 0.011, 0.007, 0, -0.008, -0.012, -0.015]
pb2Vlist = [-0.17, -0.12, -0.08, 0, 0.08, 0.12, 0.17]
CYp = (2.*V/b)*stats.linregress(pb2Vlist,CYlist2)[0]
#notes page 218
#data taken from figure 8-28


Cllist2 = [0.09, 0.065, 0.045, 0, -0.045, -0.07, -0.9]
Clp = (2.*V/b)*stats.linregress(pb2Vlist,Cllist2)[0]
#notes page 221
#data taken from figure 8-32


Cnlist2 = [2.2, 1.6, 1.1, 0, -1.1, -1.6, -2.2]
Clp = (2.*V/b)*stats.linregress(pb2Vlist,Cnlist2)[0]
#notes page 225
#data taken from figure 8-35


Cnlist2 = [2.2, 1.6, 1.1, 0, -1.1, -1.6, -2.2]
Clp = (2.*V/b)*stats.linregress(pb2Vlist,Cnlist2)[0]
#notes page 229
#data taken from figure 8-35


CYr    = +0.8495
CYda   = -0.0400
CYdr   = +0.2300

Clr    = +0.23760
Clda   = -0.23088
Cldr   = +0.03440
  
Cnr    =  -0.2061
Cnda   =  -0.0120
Cndr   =  -0.0939