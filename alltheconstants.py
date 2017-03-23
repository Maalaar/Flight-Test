# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 11:53:33 2017

@author: rensv
"""

#imports
import numpy as np
from cog import *
#from Cit_par import *
from scipy import stats

# Constant values concerning atmosphere and gravity

rho0   = 1.2250          # air density at sea level [kg/m^3] 
lambda1 = -0.0065         # temperature gradient in ISA [K/m]
Temp0  = 288.15          # temperature at sea level in ISA [K]
R      = 287.05          # specific gas constant [m^2/sec^2K]
g      = 9.81            # [m/sec^2] (gravity constant)
a0     = 0  #<--- PLACEHOLDER, IDK?

# Constant values concerning aircraft inertia

KX2    = 0.019
KZ2    = 0.042
KXZ    = 0.002
KY2    = 1.25 * 1.114

# Aircraft geometry

S      = 30.00	          # wing area [m^2]
Sh     = 0.2 * S         # stabiliser area [m^2]
Sh_S   = Sh / S	          # [ ]
lh     = 0.71 * 5.968    # tail length [m]
c      = 2.0569	          # mean aerodynamic cord [m]
lh_c   = lh / c	          # [ ]
b      = 15.911	          # wing span [m]
bh     = 5.791	          # stabilser span [m]
A      = b ** 2 / S      # wing aspect ratio [ ]
Ah     = bh ** 2 / Sh    # stabilser aspect ratio [ ]
Vh_V   = 1	          # [ ]
ih     = -2 * np.pi / 180   # stabiliser angle of incidence [rad]

# aerodynamic properties
e      =  0.87745470146438931  # Oswald factor [ ]
CD0    =  0.025563672225735336 # Zero lift drag coefficient [ ]
CLa    =  4.3517004179616956   # Slope of CL-alpha curve [ ]






### INPUTS:
#Wf = Fuel used in lbs
#V = equivalent airspeed in m/s
#a = angle of attack in rad
#rho = rho0 in kg/m3
#gamma0 = flight path angle (=0 when flying straight forward aka altitude does not change during experiment)
#de = elevator deflection in rad

### OUTPUTS:
#this function returns a matrix with:
#index - variable
#0  - CX0
#1  - CZ0
#2  - Cm0
#3  - CXu
#4  - CZu
#5  - Cmu
#6  - CXa
#7  - CZa
#8  - Cma
#9  - CXq
#10 - CZq
#11 - Cmq
#12 - CZadot
#13 - Cmadot
#14 - CXde
#15 - CZde
#16 - Cmde
#17 - CYb
#18 - CYbdot
#19 - Clb
#20 - Cnb
#21 - Cnbdot
#22 - CYp
#23 - Clp
#24 - Cnp
#25 - CYr
#26 - Clr
#27 - Cnr
#28 - CYda
#29 - Clda
#30 - Cnda
#31 - CYdr
#32 - Cldr
#33 - Cndr

# Constant values concerning aircraft inertia

def constants(Wf, V, a, rho, gamma0, de):
    
    #determining essential derivatives, just like in staticstability.py
    W = float(cog(Wf)[0])
    m = W/g
    xcg = float(cog(Wf)[1])
    
    CL = W/(0.5 * rho * V**2 * S)
    CD = CD = CD0 + (CLa * a) ** 2 / (np.pi * A * e)
    CN = CL*np.cos(a) + CD*np.sin(a)
    CT = CD*np.cos(a) - CL*np.sin(a)
    
    xle = 0.0254*261.56
    mac = 0.0254*80.98
    xac = xle + 0.25*mac #assuming ac at 25% mac
    Cmac = (xcg-xac)*CN #CG as reference point, neglecting tail for now
    
    CTw = CT
    xh = lh + xac
    CNh = (c / (Vh_V**2 * Sh_S * lh)) * (-Cmac - CN*(xcg-xac)/c)
    CNw = CN - CNh * Vh_V**2 * Sh_S
    
    CNa = -CL*np.sin(alpha) + CD*np.cos(alpha)
    CNha = CNa*(xcg-xac)/(Vh_V**2 * Sh_S * lh)
    CNwa = CNa - CNha*Vh_V**2*Sh_S
    
    deda = 2*CLa/(np.pi*A)
    #downwash derivative d(eta)/d(alpha) is required for some of these derivatives
    #this formula comes from the notes page 325 and provides a "rough estimate"
    #assumptions made: 
    #   eliptical lift distribution
    #   attached, non-separated flow
    #   this is a nice approximation for A>5, which is true for the citation
    
    ah = a - (a-a0)*deda + ih
    CNhde = CNha*ah/de
    
    #Aircraft Inertia
    muc    = m / (rho * S * c)
    mub    = m / (rho * S * b)
    
    ######################################
    ##### SYMMETRIC FLIGHT CONSTANTS #####
    ##### from the FD lecture notes  #####
    ##### starting at page 161       #####
    ######################################

    
    
    CX0 = CL*np.sin(gamma0) 
    #notes page 163
    #this is equal to zero if the flight path angle is 0 at 0 AoA
    #which should be true because we don't gain altitude during this part of the flight test
    
    
    CZ0 = CL*np.cos(gamma0) 
    #notes page 163
    #this is equal to CL if the flight path angle is 0 at 0 AoA
    #which should be true because we don't gain altitude during this part of the flight test
    
    
    Cm0 = 0
    #notes page 163
    #balanced flight, so no moments around CG
    
    
    CXu = -2*CD
    CZu = -2*CL
    Cmu = 0
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
    
    xh = xcg + lh
    Cma    = CNwa*(xcg-xac)/c - CNha*(1-deda)*(Vh_V**2)*(xh-xcg)/c
    #notes page 173
    #using data from drag polar measurements during flight test
    
    
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
    
    
    CXde = 0
    #notes page 185
    #"commonly neglected" in subsonic flight
    
    
    CZde = -CNhde*(Vh_V**2)*Sh_S
    #notes page 186
    
    
    Cmde = -(Cm0 + Cma(a-a0))/de
    #lecture 3 slide 37
    
    
    
    #######################################
    ##### ASYMMETRIC FLIGHT CONSTANTS #####
    ##### from the FD lecture notes   #####
    ##### starting at page 188        #####
    #######################################
    
    #most of the derivatives were taken from figures with expirimental data of the Citation
    #why? because deriving them analytically takes a lot of time, and we only have 3 weeks
    #also, a lot of assumptions are made when calculating them analytically
    #which would result in a lot of errors anyway
    #it's probably for a reason the lecture notes constantly mention: 
    #"trying this analytically will not be accurate, do experiments to find these derivatives"
    
    
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
    
    
    Cnlist2 = (10**-3)*np.array([2.2, 1.6, 1.1, 0, -1.1, -1.6, -2.2])
    Cnp = (2.*V/b)*stats.linregress(pb2Vlist,Cnlist2)[0]
    #notes page 225
    #data taken from figure 8-35
    
    
    rb2Vlist = [-0.17, -0.125, -0.08, 0, 0.08, 0.0125, 0.17]
    CYlist3 = [-0.025, -0.02, -0.015, 0, 0.015, 0.02, 0.025]
    CYr = (2.*V/b)*stats.linregress(rb2Vlist,CYlist3)[0]
    #notes page 229
    #data taken from figure 8-40
    
    
    Cllist3 = [-0.014, -0.011, -0.0075, 0, 0.007, 0.011, 0.014]
    Clr = (2.*V/b)*stats.linregress(rb2Vlist,Cllist3)[0]
    #notes page 231
    #data taken from figure 8-41
    
    
    Cnlist3 = [0.024, 0.018, 0.012, 0, -0.012, -0.018, -0.024]
    Cnr = (2.*V/b)*stats.linregress(rb2Vlist,Cnlist3)[0]
    #notes page 232
    #data taken from figure 8-43
    
    
    CYda = 0
    #notes page 234
    #"very small in magnitude, usually neglected"
    
    
    Clda = -0.23088 #<--- FROM APPENDIX C
    #notes page 235
    #probably leaving this as it is because:
    #   All sources provided in the notes are vague papers from the 1940's
    #   We know nothing about the Citation ailerons, size or shape
    #   We have no experimental data on ailerons
    #   Everywhere i look it says: theory is inaccurate, better to find this derivative experimentally
    #Combine these facts and I don't think we will have a reliable result
    #only source i didnt check [74] is in the UB and currently lend out
    
    
    Cnda = -0.0120 #<--- FROM APPENDIX C
    #notes page 236
    #leaving this as it is for now
    #only source to determine this [74] is in the UB and currently lend out
    
    
    CYdr = +0.2300 #<--- FROM APPENDIX C
    #notes page 239
    #keeping this the same as well because:
    #   Sources are vague
    #   Just like ailerons, we don't know shit about the rudder (dimensions, behavior)
    #   Many assumptions need to be made
    #   We only have three weeks, I don't have the time to do a literature study on rudders
    

    zcg = 1.6 #<--- EDUCATED GUESS, center of fuselage is about 1.5m, engines & tail slightly above, wings & fuel slightly below
    zv = 3. #<--- EDUCATED GUESS, total heigth citation 4.57m, tail starts at about 1.5m heigth
    Cldr = CYdr*(zv-zcg)/b
    #notes page 240
    
    
    Cndr = -CYdr*(xh-xcg)/b
    #notes page 240
    #assuming xv-xcg = xh-xcg
    
    return [CX0, CZ0, Cm0, CXu, CZu, Cmu, CXa, CZa, Cma, CXq, CZq, Cmq, CZadot, Cmadot, CXde, CZde, Cmde, \
            CYb, CYbdot, Clb, Cnb, Cnbdot, CYp, Clp, Cnp, CYr, Clr, Cnr, CYda, Clda, Cnda, CYdr, Cldr, Cndr, \
            muc, mub]
            