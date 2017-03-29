# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 10:45:10 2017

@author: Maarten
"""

from Numerical_Analysis_assymettric import *

namem = "AperiodicRollP [Ik Haat Jari omdat hij kk laat hier mee komt en johan omdat hij hier vanochtend niks over te whinen had]"

def plot(name):

    y11,y12,y13,y14,t1 = Asymetric(name)

#    plotting the total grpahs
    plt.figure(0)
#    plt.gca().set_ylim([-1,0])
#    plt.gca().set_xlim([0,140])    
    plt.tick_params(axis="x", labelsize=15)
    plt.tick_params(axis="y", labelsize=15)    
    plt.title('Angle of Sideslip ')
    plt.plot(t1, y11, label="Numerical Optimized", color="blue")
    plt.ylabel(r"$\beta$ [deg]")
    plt.xlabel("t [s]")
    plt.legend(loc=2)
    plt.savefig((namem + "Angle of Sideslip"))
    plt.show()
    
    plt.figure(1)
#    plt.gca().set_ylim([-1,0])
#    plt.gca().set_xlim([0,140])    
    plt.tick_params(axis="x", labelsize=15)
    plt.tick_params(axis="y", labelsize=15)
    plt.title('Roll Angle ')
    plt.plot(t1, y12, label="Numerical Optimized", color="blue")
    plt.ylabel("$\phi$ [deg]")
    plt.xlabel("t [s]")
    plt.plot(t1, name.RollAngle, label="Experimental", color="green")
    plt.legend(loc=2)
    plt.savefig((namem + "RollAngle"))
    plt.show()
    
    plt.figure(2)
#    plt.gca().set_ylim([-1,0])
#    plt.gca().set_xlim([0,140])    
    plt.tick_params(axis="x", labelsize=15)
    plt.tick_params(axis="y", labelsize=15)
    plt.title('Roll Rate')
    plt.plot(t1, y13, label="Numerical Optimized", color="blue")
    plt.ylabel("p [deg/s]")
    plt.xlabel("t [s]")
    plt.plot(t1, name.RollRate, label="Experimental", color="green")
    plt.legend(loc=3)
    plt.savefig((namem + "RollRate"))
    plt.show()

    plt.figure(3)
#    plt.gca().set_ylim([-1,0])
#    plt.gca().set_xlim([0,140])    
    plt.tick_params(axis="x", labelsize=15)
    plt.tick_params(axis="y", labelsize=15)
    plt.title('Yaw Rate')
    plt.plot(t1, y14, label="Numerical Optimized", color="blue")
    plt.ylabel("r [deg/s]")
    plt.xlabel("t [s]")
    plt.plot(t1, name.YawRate, label="Experimental", color="green")
    plt.legend(loc=2)
    plt.savefig((namem + "YawRate"))
    plt.show()   
    
    plt.figure(4)
    plt.gca().set_ylim([-6,6])
#    plt.gca().set_xlim([0,140])    
    plt.tick_params(axis="x", labelsize=15)
    plt.tick_params(axis="y", labelsize=15)
    plt.title("Aileron Deflection")
    plt.plot(t1, (name.delta_a_stab*180/np.pi), color="green")
    plt.ylabel("$\delta_a$ [deg]")
    plt.xlabel("t [s]")
    plt.savefig((namem + "Ailerondeflection"))

    
    plt.figure(5)
    plt.gca().set_ylim([-6,6])
#    plt.gca().set_xlim([0,140])    
    plt.tick_params(axis="x", labelsize=15)
    plt.tick_params(axis="y", labelsize=15)
    plt.title("Rudder Deflection")
    plt.plot(t1, (name.delta_r_stab*180/np.pi), color="green")
    plt.ylabel("$\delta_r$ [deg]")
    plt.xlabel("t [s]")
    plt.savefig((namem + "Rudder Deflection"))
    
def plotfirst(name):
    
    y11,y12,y13,y14,t1 = Asymetric(name)
    #    plotting the total grpahs
    plt.figure(0)
    plt.plot(t1, y11, label="Numerical", color="red")
    plt.show()
    
    plt.figure(1)
    plt.plot(t1, y12, label="Numerical", color="red")
    plt.show()
    
    plt.figure(2)
    plt.plot(t1, y13, label="Numerical", color="red")
    plt.show()

    plt.figure(3)
    plt.plot(t1, y14, label="Numerical", color="red")
    plt.show()   
    
#from Cit_par_Corne import *
#    y21,y22,y23,y24,t2 = Asymetric(name)