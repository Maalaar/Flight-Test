import numpy as np
from Eq_airspeed import *
from alltheconstants import *
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

#Total fuel usage
Wf = Wfl + Wfr 

#step size for computation
step = 0.1

#class definition for  start time and total measured time in seconds

class Motion:
    def __init__(self,stime,mt):
        self.index                              =       np.where(time==stime)[0][0]
        self.deltae                             =       deltae[self.index:self.index+(mt/step)]/180*np.pi
        self.height                             =       h_p[self.index:self.index+(mt/step)]
        self.TAT                                =       TAT[self.index:self.index+(mt/step)]
        self.IASkts                             =       v_ias[self.index:self.index+(mt/step)]
        self.EAS, self.TAS, self.rho, self.M    =       equivalentspeed(self.height, self.TAT, self.IASkts)
        self.IAS                                =       self.IASkts*kts_to_ms
        self.AoA                                =       AoA[self.index:self.index+(mt/step)]
        self.time                               =       np.linspace(self.index,self.index+(mt/step), num=len(self.deltae), endpoint=True, retstep=False)
        self.mt                                 =       mt
        self.delta_r                            =       delta_r[self.index:self.index+(mt/step)]
        self.delta_a                            =       delta_a[self.index:self.index+(mt/step)]
        self.weightf                            =       Wf[self.index:self.index+(mt/step)]
        self.weightf0                           =       [np.average(self.weightf[0:5])]
        self.V0                                 =       np.average(self.EAS[0:5])
        self.AoA0                               =       np.average(self.AoA[0:5])
        self.PitchAngle                         =       pitch_angle[self.index:self.index+(mt/step)]
        self.PitchAngle0                        =       np.average(self.PitchAngle[0:5])
        self.RollRate                           =       roll_rate[self.index:self.index+(mt/step)]
        self.RollAngle                          =       roll_angle[self.index:self.index+(mt/step)]
        self.YawRate                            =       yaw_rate[self.index:self.index+(mt/step)]
        self.CX0, self.CZ0, self.Cm0, self.CXu, self.CZu, self.Cmu, self.CXa, self.CZa,\
        self.Cma, self.CXq, self.CZq, self.Cmq, self.CZadot, self.Cmadot, self.CXde,\
        self.CZde, self.Cmde, self.CYb, self.CYbdot, self.Clb, self.Cnb, self.Cnbdot, \
        self.CYp, self.Clp, self.Cnp, self.CYr, self.Clr, self.Cnr, self.CYda, self.Clda, \
        self.Cnda, self.CYdr, self.Cldr, self.Cndr, self.muc, self.mub        =       constants(self.weightf0, self.V0, self.AoA0, rho0, 0)
        self.allconstants                 =       constants(self.weightf0, self.V0, self.AoA0, rho0, 0)                                  
#symetric motions

#phugoid motion
phugoid_time    =   3600.*1. + 60.*15. + 30.
phugoid_mt      =   200
phugoidP        =   Motion(phugoid_time,phugoid_mt)

#short period
short_time      =   3600.*1. + 60.*14. + 24.
short_mt        =   6
shortP          =   Motion(short_time, short_mt)
#       assymetric motion

#dutch roll
DutchRoll_time  =   3600.*1. + 60.*10. + 40.
DutchRoll_mt    =   400
DutchRollP      =   Motion(DutchRoll_time, DutchRoll_mt)      

#dutch roll YD
DutchRollY_time =   3600.*1. + 60.*12. + 0.    
DutchRollY_mt   =   400
DutchRollYP    =   Motion(DutchRollY_time, DutchRollY_mt)

#aper roll
APR_time        =   3600.*1. + 60.*19. + 0.
APR_mt          =   400
AperiodicRollP  =   Motion(APR_time, APR_mt)

#Spiral
SPRL_time       =   3600.*1. + 60.*21. + 50.
SPRL_mt         =   400
SpiralP         =   Motion(SPRL_time,SPRL_mt)


