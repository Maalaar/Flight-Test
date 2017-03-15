# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 11:53:33 2017

@author: rensv
"""

#imports
import numpy as np
from Cit_par import *
from staticstability import *

#inputs
a0 = 0
ip = 0
gamma0 = 0 #flight path = straight foreward
rho = rho19000

#basics, notes eq 7-1
Tc = T/(0.5*rho*V**2*S)

CX = CL*np.sin(a) - CD*np.cos(a) + Tc
CZ = -CL*np.cos(a) - CD*np.sin(a) - Tc*(a0+ip)


###
### All the constants
### 

#CM-alpha
from scipy import stats
CNwa   = stats.linregress(alpha,CNw)[0]
CNha   = stats.linregress(alpha,CNh)[0]
CNa    = stats.linregress(alpha,CN)[0]
deda   = 0 #downwash??????
Cma    = CNwa*(xcg-xac)/c - CNha*(1-de/da)*(Vh_V**2)*(Sh*lh)/(S*c) #notes page 173, downwash???? 

#constants in X direction
CX0    = -CD + Tc #notes page 187
CXu    = 2*CL*tan(gamma0) #notes page 187
CXa    = CL*(1-2*CLa/(np.pi*A*e)) #notes eq 7-16 and below
CXadot = 0 #notes page 187, neglected
CXq    = 0 #notes page 179, negligible contribution
CXde   = 0 #notes page 185, neglecting drag change wrt elevator angle

#constants in Z direction
CZ0    = -CL #notes page 187
CZu    = -2*CL #notes page 168
CZa    = CNa #notes page 187
CZadot = -CNha*(Vh_V**2)*deda*Sh*lh/(S*c) #notes page 185, downwash???
CZq    = -2*CNha*(Vh_V**2)*Sh*lh/(S*c) #notes page 181
CNhde  = 1 #page 186, I have no clue
CZde   = -CNhde*(Vh_V**2)*(Sh/S)

#more moment constants
Cm0    = 0 #page 187
Cmu    = 0 #page 187
Cmadot = -CNha*(Vh_V**2)*deda*Sh*lh**2/(S*(c**2)) #notes page 185, downwash???
Cmq    = -1.15*CNha*(Vh_V**2)*Sh*lh**2/(S*(c**2)) #notes page 181
Cmde   = -CNhde*(Vh_V**2)*Sh*lh/(S*c) #not necessary i think, but anyway, notes page 187

#constants in Y direction
CYb    = -0.7500
CYbdot =  0     
CYp    = -0.0304
CYr    = +0.8495
CYda   = -0.0400
CYdr   = +0.2300

#constants in l direction
Clb    = -0.10260
Clp    = -0.71085
Clr    = +0.23760
Clda   = -0.23088
Cldr   = +0.03440

#constants in n direction
Cnb    =  +0.1348
Cnbdot =   0     
Cnp    =  -0.0602
Cnr    =  -0.2061
Cnda   =  -0.0120
Cndr   =  -0.0939