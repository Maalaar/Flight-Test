import numpy as np
from sympy import *
from Cit_par import *
#from alltheconstantsjohan import *
import matplotlib.pyplot as plt
x, y = symbols('x y')




#print CXu


def eigenvaluessym(Cxu,muc,Cxalpha,Cz0,Czu,Czalpha,Czalphadot,Cx0,Czq,Cmu,Cmalpha,Cmalphadot,Cmq,Ky2):
    

    A1=Cxu-2*muc*x
    A2=Cxalpha
    A3=Cz0
    A4=0
    A5=Czu
    A6=Czalpha+(Czalphadot-2*muc)*x
    A7=-Cx0
    A8=Czq+2*muc
    A9=0
    A10=0
    A11=-x
    A12=1
    A13=Cmu
    A14=Cmalpha+Cmalphadot*x
    A15=0
    A16=Cmq-2*muc*Ky2*x

    block1=  A1* ( A6*(A11*A16-A12*A15)-A7*(A10*A16-A12*A14)+A8*(A10*A15-A11*A14))
    block2= - A2* (A5*(A11*A16-A12*A15)-A7*(A9*A16-A12*A13)+A8*(A9*A15-A11*A13))
    block3= A3* ( A5*(A10*A16-A12*A14)-A6*(A9*A16-A12*A13)+A8*(A9*A14-A10*A13))
    block4= -A4*(A5*(A10*A15-A11*A14)-A6*(A9*A15-A11*A13)+A7*(A9*A14-A10*A13))

    return solve(Eq(block1+block2+block3+block4, 0), x)


def eigenvaluesasym(Cybeta,Cybetadot,mub,CL,Cyp,Cyr,Clbeta,Clp,Kx2,Clr,Kxz,Cnbeta,Cnbetadot,Cnp,Cnr,Kz2): 
    

    A1=Cybeta+(Cybetadot-2*mub)*x
    A2=CL
    A3=Cyp
    A4=Cyr-4*mub
    A5=0
    A6=-0.5*x
    A7=1
    A8=0
    A9=Clbeta
    A10=0
    A11=Clp-4*mub*Kx2*x
    A12=Clr+4*mub*Kxz*x
    A13=Cnbeta+Cnbetadot*x
    A14=0
    A15=Cnp+4*mub*Kxz*x
    A16=Cnr-4*mub*Kz2*x

    block1=  A1* ( A6*(A11*A16-A12*A15)-A7*(A10*A16-A12*A14)+A8*(A10*A15-A11*A14))
    block2= - A2* (A5*(A11*A16-A12*A15)-A7*(A9*A16-A12*A13)+A8*(A9*A15-A11*A13))
    block3= A3* ( A5*(A10*A16-A12*A14)-A6*(A9*A16-A12*A13)+A8*(A9*A14-A10*A13))
    block4= -A4*(A5*(A10*A15-A11*A14)-A6*(A9*A15-A11*A13)+A7*(A9*A14-A10*A13))

    return solve(Eq(block1+block2+block3+block4, 0), x)




Eigen1=eigenvaluessym(CXu,muc,CXa,CZ0,CZu,CZa,CZadot,CX0,CZq,Cmu,Cma,Cmadot,Cmq,KY2)
Eigen2=eigenvaluesasym(CYb,CYbdot,mub,CL,CYp,CYr,Clb,Clp,KX2,Clr,KXZ,Cnb,Cnbdot,Cnp,Cnr,KZ2)

#print eigenvaluesasym(-0.9896,0,15.5,1.136,-0.087,0.43,-0.0772,-0.3444,0.012,0.28,0.002,0.1638,0,-0.0108,-0.193,0.037)
#print eigenvaluessym(-0.2199,102.7,0.4653,-1.136,-2.2720,-5.16,-1.43,0,-3.86,0,-0.43,-3.7,-7.04,0.98)



V=120 ######################################################



#####SYMMETRIC


lambda1=Eigen1[0]
lambda2=Eigen1[1]
lambda3=Eigen1[2]
lambda4=Eigen1[3]





P1=abs(2*np.pi*c/im(lambda1)/V)
P2=abs(2*np.pi*c/im(lambda3)/V)

T1=abs(np.log(0.5)*c/V/re(lambda1))
T2=abs(np.log(0.5)*c/V/re(lambda3))

omega1=2*np.pi/P1
omega2=2*np.pi/P2

damping1=abs(re(lambda1)/((re(lambda1)**2+im(lambda1)**2))**0.5)
damping2=abs(re(lambda3)/((re(lambda3)**2+im(lambda3)**2))**0.5)

###############ASYMMETRIC

lambda5=Eigen2[0]
lambda6=Eigen2[1]
lambda7=Eigen2[2]
lambda8=Eigen2[3]

T3=abs(np.log(0.5)*b/V/re(lambda5))
T4=abs(np.log(0.5)*b/V/re(lambda6))

T5=abs(np.log(0.5)*b/V/re(lambda7))
P5=abs(2*np.pi*b/im(lambda7)/V)
omega5=2*np.pi/P5
damping5=abs(re(lambda7)/((re(lambda7)**2+im(lambda7)**2))**0.5)

print "SYMMETRIC"
print " "
print "Short Period"
print "Period            ",round(P1,2),"  s"
print "Half time         ",round(T1,2),"  s"
print "Frequency         ",round(omega1,2),"  rad/s"
print "Damping           ",round(damping1,2)
print " "
print "Fugoid"
print "Period            ",round(P2,2),"  s"
print "Half time         ",round(T2,2)," s"
print "Frequency         ",round(omega2,2),"   rad/s"
print "Damping           ",round(damping2,2)
print " "
print "ASYMMETRIC"
print " "
print "First Aperiodic"
print "Half time         ",round(T3,2),"  s"
print " "
print "Second Aperiodic"
print "Half time         ",round(T4,2),"s"
print " "
print "Periodic          "
print "Period            ",round(P5,2),"  s"
print "Half time         ",round(T5,2),"   s"
print "Frequency         ",round(omega5,2),"  rad/s"
print "Damping           ",round(damping5,2)
print " "
print " "
print "EIGENVALUES"
print "Short:            ",round(re(lambda1),4),"±",abs(round(im(lambda1),4)),"j"
print "Fugoid:           ",round(re(lambda3),4),"±",abs(round(im(lambda3),4)),"j"
print " "
print "First Aperiodic:  ",round(re(lambda5),4),"±",abs(round(im(lambda5),4)),"j"
print "Second Aperiodic: ",round(re(lambda6),4),"±",abs(round(im(lambda6),4)),"j"
print "Periodic:         ",round(re(lambda7),4),"±",abs(round(im(lambda7),4)),"j"



