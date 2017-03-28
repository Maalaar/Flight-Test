# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 10:02:52 2017

@author: Bart
"""
import numpy as np
import matplotlib.pyplot as plt
import cog
from constants import *
import Eq_airspeed_jari as Eq_airspeed
from scipy import stats

h_p     = np.array([18930.,17920.,17330.,16540.,17210.,17440.,17600.]) #ft
V_IAS   = np.array([158.,170.,180.,188.,149.,140.,130.]) #kts
a_deg       = np.array([4.8,4.,3.3,2.8,5.7,6.6,7.9]) #deg
de      = np.array([-0.4,0.,0.3,0.5,-0.8,-1.2,-1.7]) #deg
detr    = np.array([3.1,3.1,3.1,3.1,3.1,3.1,3.1]) #deg
Fe      = np.array([-2.,19.,36.,59.,-23.,-30.,-42.]) #N
FFl     = np.array([389.,401.,405.,418.,402.,394.,393.]) #lbs/hr
FFr     = np.array([413.,426.,436.,446.,431.,425.,421.]) #lbs/hr
Fused   = np.array([956.,1000.,1020.,1037.,1063.,1081.,1105.]) #lbs
TAT     = np.array([-16.9,-13.8,-11.8,-9.7,-13.8,-14.8,-15.8]) #deg C
m_pass  = np.array([99.,73.,60.,72.,73.,81.,79.,85.,85.]) #mass of pilots and passengers
Fused_cg= 1140. #lbs
hp_cg   = 16700. #ft
V_IAS_cg= 158. #kts
TAT_cg  = -12.2 #degrees C
Thrust  = np.genfromtxt('ThrustElevator.dat')
ThrustS = np.genfromtxt('ThrustStandard.dat')

OEW     = OEW*lbs_to_kg
Fused   = Fused*lbs_to_kg
m_pass  = m_pass*lbs_to_kg
m_fuel_0 = m_fuel_0*lbs_to_kg
de      = de*np.pi/180.
detr    = detr*np.pi/180.
a       = a_deg*np.pi/180.

V_e, M = Eq_airspeed.equivalentspeed(h_p, TAT, V_IAS)

m       = OEW + m_fuel_0 + m_pass.sum() - Fused
W       = m*g
V_e_red = V_e*np.sqrt(W_s/W)

#shift in centre of gravity
W1,cog1 = cog.cog([1140.])
W2,cog2 = cog.cog2([1174.])

dxcg    = float(cog2-cog1)
de1     = (-0.9--0.4)*np.pi/180.

V_e_cg, M_cg  = Eq_airspeed.equivalentspeed(hp_cg, TAT_cg, V_IAS_cg)

m_cg    = OEW + m_fuel_0 + m_pass.sum() - Fused_cg
W_cg    = m_cg*g
C_N_cg  = W_cg/(0.5*rho0*S*V_e_cg**2.)

Cmde    = -(C_N_cg*dxcg)/(de1*c) #elevator efectiveness

#continue for Cma
Thrust  = np.sum(Thrust,axis=1)
ThrustS = np.sum(ThrustS,axis=1)

T_c     = Thrust/(0.5*rho0*V_e**2.*S)
T_cs    = ThrustS/(0.5*rho0*V_e**2.*S)

de_red  = de - (C_mTc*(T_cs-T_c))/Cmde

slope, intercept, r_value, p_value, std_err = stats.linregress(a,de_red)

Cma = -slope*Cmde

#Reduced Control Force curve
Fe_red = Fe*(W_s/W)
#


V_e_red_s =np.sort(V_e_red)
Fe_red_s = np.sort(Fe_red)
de_red_s = np.sort(de_red)
a_s = np.sort(a)

terms = np.polyfit(V_e_red_s,Fe_red_s, 2)

linspace = np.linspace(60,100,num = 50)

keke = terms[2] + terms[1] * linspace + terms[0] * linspace**2

plt.close()
plt.gca().invert_yaxis()
plt.scatter(V_e_red_s, Fe_red_s)
plt.title(r'Reduced Control Force')
plt.ylabel(r'$F_e^*$(-) in N')
plt.xlabel(r'$\tilde{V_{e}}$ in m/s')
plt.axhline(0, color='black')

for i, txt in enumerate(FFT):
    plt.annotate("{:6.4f}".format(txt), (V_e_red[i]+1,Fe_red[i]+0.0005))

plt.plot(linspace,keke,linestyle='dashed')
plt.show()

FFT = (FFl + FFr) * lbs_to_kg / 3600.

terms2 = np.polyfit(np.log(V_e_red_s), de_red_s, 1)

keke2 = terms2[0] * np.log(linspace) + terms2[1]


#plt.close()
#plt.gca().invert_yaxis()
#plt.scatter(V_e_red_s, de_red_s)
#plt.title(r'Reduced Elevator Deflection')
#plt.ylabel(r'$\delta_e^*$ [rad]')
#plt.xlabel(r'$\tilde{V_{e}}$ in m/s')
#plt.axhline(0, color='black')
#plt.plot(linspace,keke2,linestyle='dashed')
#for i, txt in enumerate(FFT):
#    plt.annotate("{:6.4f}".format(txt), (V_e_red[i]+1,de_red[i]+0.0005))
#plt.show()


terms3 = np.polyfit(a_s[::-1], de_red_s, 1)
linspace2 = np.linspace(0.04, 0.15, num=20)
keke3 = terms3[0] * linspace2 + terms3[1]
a_s_inv = a_s[::-1]

#plt.close()
#plt.gca().invert_yaxis()
#plt.scatter(a_s_inv, de_red_s)
#plt.title(r'Reduced Elevator Deflection')
#plt.ylabel(r'$\delta_e^*$ [rad]')
#plt.xlabel(r'$\alpha$ [rad]')
#plt.axhline(0, color='black')
#plt.plot(linspace2,keke3,linestyle='dashed')
#
#FFT_inv = FFT[::-1]
#for i, txt in enumerate(FFT):
#    plt.annotate("{:6.4f}".format(txt), (a[i]+0.005,de_red[i]+0.0005))
#
#plt.show()


cogstart = cog.cog([FFr[0]+FFl[0]])


cogend =  cog.cog([FFr[6]+FFl[6]])

cogdif = cogstart[1][0]-cogend[1][0]




