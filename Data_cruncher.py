import numpy as np
from Eq_airspeed import *
from Cit_par_Corne import *
import matplotlib.pyplot as plt

#importing all measured data from text files into numpy arrays
time        = np.genfromtxt('data/time[sec].txt', delimiter = ',')              #sec
v_tas       = np.genfromtxt('data/V_tas[kts].txt', delimiter = '\n')            #kts
v_ias       = np.genfromtxt('data/V_cas[kts].txt', delimiter = '\n')            #kts
pitch_angle = np.genfromtxt('data/pitch_angle_[deg].txt', delimiter = '\n')     #deg
pitch_rate  = np.genfromtxt('data/pitch_rate[degpers].txt', delimiter = '\n')   #deg/s
Wfl         = np.genfromtxt('data/F_used_l[lbs].txt', delimiter = '\n')         #lbs
Wfr         = np.genfromtxt('data/F_used_r[lbs].txt', delimiter = '\n')         #lbs
AoA         = np.genfromtxt('data/AOA[deg].txt', delimiter ='/n')               #deg
deltae      = np.genfromtxt('data/delta_e[deg].txt', delimiter ='/n')           #deg
roll_rate   = np.genfromtxt('data/roll_rate[degpers].txt', delimiter ='/n')     #deg/s
yaw_rate    = np.genfromtxt('data/yaw_rate[degpers].txt', delimiter ='/n')      #deg/s
delta_r     = np.genfromtxt('data/delta_r[deg].txt', delimiter ='/n')           #deg
delta_a     = np.genfromtxt('data/delta_a[deg].txt', delimiter ='/n')           #deg
h_p         = np.genfromtxt('data/h_p[ft].txt', delimiter ='/n')                #ft
TAT         = np.genfromtxt('data/TAT[degc].txt', delimiter ='/n')              #degrees celsius
roll_angle  = np.genfromtxt('data/roll_angle[deg].txt', delimiter ='/n')           #deg
pitch_rate  = np.genfromtxt('data/pitch_rate[degpers].txt', delimiter ='/n')      #deg/s
#Total fuel usage
Wf = Wfl + Wfr 

#step size for computation
step = 0.1

#class definition for  start time and total measured time in seconds

class Motion:
    def __init__(self,stime,mt):
        self.index                              =       np.where(time==(stime))[0][0]
        self.deltae                             =       deltae[self.index:self.index+(mt/step)]/180*np.pi
        self.deltae0                            =       np.average(self.deltae[0:5])
        self.deltae_stab                        =       self.deltae-self.deltae0
        self.height                             =       h_p[self.index:self.index+(mt/step)]
        self.height0                            =       np.average(self.height[0:5])
        self.TAT                                =       TAT[self.index:self.index+(mt/step)]
        self.IASkts                             =       v_ias[self.index:self.index+(mt/step)]
        self.EAS, self.TAS, self.rho, self.M    =       equivalentspeed(self.height, self.TAT, self.IASkts)
        self.IAS                                =       self.IASkts*kts_to_ms
        self.AoA                                =       AoA[self.index:self.index+(mt/step)]
        self.time                               =       np.linspace(self.index,self.index+(mt/step), num=len(self.deltae), endpoint=True, retstep=False)
        self.mt                                 =       mt
        self.delta_r                            =       delta_r[self.index:self.index+(mt/step)]/-180*np.pi
        self.delta_r0                           =       np.average(self.delta_r[0:5])
        self.delta_r_stab                       =       self.delta_r-self.delta_r0
        self.delta_a                            =       delta_a[self.index:self.index+(mt/step)]/180*np.pi
        self.delta_a0                           =       np.average(self.delta_a[0:5])
        self.delta_a_stab                       =       self.delta_a-self.delta_a0
        self.weightf                            =       Wf[self.index:self.index+(mt/step)]
        self.weightf0                           =       [np.average(self.weightf[0:5])]
        self.weight                             =       np.subtract(66183,self.weightf0)[0]
        self.V0                                 =       np.average(self.EAS[0:5])
        self.AoA0                               =       np.average(self.AoA[0:5])
        self.PitchAngle                         =       pitch_angle[self.index:self.index+(mt/step)]
        self.PitchAngle0                        =       np.average(self.PitchAngle[0:5])
        self.PitchRate                          =       pitch_rate[self.index:self.index+(mt/step)]
        self.RollRate                           =       roll_rate[self.index:self.index+(mt/step)]
        self.RollRate0                          =       np.average(self.RollRate[0:5])
        self.RollAngle                          =       roll_angle[self.index:self.index+(mt/step)]
        self.RollAngle0                         =       np.average(self.RollAngle[0:5])
        self.YawRate                            =       yaw_rate[self.index:self.index+(mt/step)]
        self.YawRate0                           =       np.average(self.YawRate[0:5])
        self.rho,self.muc,self.mub,self.CL,self.CD,self.CX0,self.CZ0        =       kutmaarten(self.V0, self.AoA0, self.PitchAngle0, self.weight, self.height0)                              
#symetric motions

#phugoid motion
phugoid_time    =   3600.*1. + 60.*15. + 40.
phugoid_mt      =   150
Phugoid        =   Motion(phugoid_time,phugoid_mt)

#short period
short_time      =   3600.*1. + 60.*14. + 33.
short_mt        =   14
Short_Period          =   Motion(short_time, short_mt)
#       assymetric motion

#dutch roll
DutchRoll_time  =   3600.*1. + 60.*10. + 50.
DutchRoll_mt    =   30
DutchRoll      =   Motion(DutchRoll_time, DutchRoll_mt)      

#dutch roll YD
DutchRollY_time =   3600.*1. + 60.*12. + 5.    
DutchRollY_mt   =   12
DutchRollY    =   Motion(DutchRollY_time, DutchRollY_mt)

#aper roll
APR_time        =   3600.*1. + 60.*19. + 10.
APR_mt          =   25
AperiodicRollP  =   Motion(APR_time, APR_mt)


#Spiral
SPRL_time       =   3600.*1. + 60.*22
SPRL_mt         =   50
Spiral         =   Motion(SPRL_time,SPRL_mt)


