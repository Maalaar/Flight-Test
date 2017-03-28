import numpy as np
from sympy import *
from Cit_par_SUKKELS import *
#from alltheconstantsjohan import *
import matplotlib.pyplot as plt
x, y = symbols('x y')

V0 = 100.
alpha0=0.
th0=0.
#m=60532.81018594/9.80665
m=6500.
#print m
hp0=3000.
rho,muc,mub,CL,CD,CX0,CZ0 = kutmaarten(V0,alpha0,th0,m,hp0)

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



V=V0 ######################################################



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


print "logical", np.pi*2*re(lambda1)/im(lambda1)
print "logical", np.pi*2*re(lambda3)/im(lambda3)
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
print "Period            ",round(P1,4),"  s"
print "Half time         ",round(T1,4),"  s"
print "Frequency         ",round(omega1,4),"  rad/s"
print "Damping           ",round(damping1,4)
print " "
print "Fugoid"
print "Period            ",round(P2,4),"  s"
print "Half time         ",round(T2,4)," s"
print "Frequency         ",round(omega2,4),"   rad/s"
print "Damping           ",round(damping2,4)
print " "
print "ASYMMETRIC"
print " "
print "First Aperiodic"
print "Half time         ",round(T3,4),"  s"
print " "
print "Second Aperiodic"
print "Half time         ",round(T4,4),"s"
print " "
print "Periodic          "
print "Period            ",round(P5,4),"  s"
print "Half time         ",round(T5,4),"   s"
print "Frequency         ",round(omega5,4),"  rad/s"
print "Damping           ",round(damping5,4)
print " "
print " "
print "EIGENVALUES"
print "Short:            ",round(re(lambda1),6),"±",abs(round(im(lambda1),6)),"j"
print "Fugoid:           ",round(re(lambda3),6),"±",abs(round(im(lambda3),6)),"j"
print " "
print "First Aperiodic:  ",round(re(lambda5),6),"±",abs(round(im(lambda5),6)),"j"
print "Second Aperiodic: ",round(re(lambda6),6),"±",abs(round(im(lambda6),6)),"j"
print "Periodic:         ",round(re(lambda7),6),"±",abs(round(im(lambda7),6)),"j"



print " "
print "ANALYTICAL SIMPLIFICATION"
print " "
print "Symmetrical"
A = 2*muc*KY2*(2*muc-CZadot)
B = -2*muc*KY2*CZa - (2*muc+CZq)*Cmadot - (2*muc-CZadot)*Cmq
C = CZa * Cmq - (2*muc+CZq)*Cma
re=-B/(2*A)
im = abs((4*A*C-B**2)**0.5/(2*A))
print "Short Eigenvalue: ",re , "±",im ,"j"


print "Omega0: ", V/c*(C/A)**0.5,"rad/s"
print "Damping: ", abs(-B/(2*(A*C)**0.5))
print "Omegan: ", V/c*(C/A)**0.5* (1-(abs(-B/(2*(A*C)**0.5)))**2)**0.5
print "Period: ", 2*np.pi/((V/c*(C/A)**0.5)*(1-(-B/(2*(A*C)**0.5))**2)**0.5)
print "T1/2", -np.log(2)/re*c/V,"s"
A = 2*muc*(CZa*Cmq-2*muc*Cma)
B = 2*muc*(CXu*Cma- Cmu*CXa)+Cmq*(CZu*CXa - CXu*CZa)
C = CZ0*(Cmu*CZa-CZu*Cma)

re=-B/(2*A)
im = abs((4*A*C-B**2)**0.5/(2*A))

print "Phugoid Eigenvalue: ",re , "±", im,"j"
print "Omega0: ", V/c*(C/A)**0.5,"rad/s"
print "Omegan: ", V/c*(C/A)**0.5* (1-(abs(-B/(2*(A*C)**0.5)))**2)**0.5
print "Damping: ", abs(-B/(2*(A*C)**0.5))
print "Period: ", 2*np.pi/((V/c*(C/A)**0.5)*(1-(-B/(2*(A*C)**0.5))**2)**0.5)
print "T1/2", -np.log(2)/re*c/V,"s"

print " "
print "Asymmetrical"
print "Eigen1",Clp/(4*mub*KX2)









re = Clp/(4*mub*KX2)
print "T1/2", -np.log(2)/re*b/V,"s"




print "Eigen4",(2*CL*(Clb*Cnr-Cnb*Clr))    /     (  Clp*(CYb*Cnr+4*mub*Cnb) -  Cnp*(CYb*Clr+4*mub*Clb)  )
re = (2*CL*(Clb*Cnr-Cnb*Clr))    /     (  Clp*(CYb*Cnr+4*mub*Cnb) -  Cnp*(CYb*Clr+4*mub*Clb)  )
print "T1/2", -np.log(2)/re*b/V,"s"




A=8*mub**2*KZ2
B=-2*mub*(Cnr+2*KZ2*CYb)
C=4*mub*Cnb +CYb*Cnr

re=-B/(2*A)
im = abs((4*A*C-B**2)**0.5/(2*A))

print "Dutch Roll Eigenvalue: ",re , "±", im,"j"
print "Omega0: ", V/b*(C/A)**0.5,"rad/s"
print "Omegan: ", V/b*(C/A)**0.5* (1-(abs(-B/(2*(A*C)**0.5)))**2)**0.5
print "Damping: ", abs(-B/(2*(A*C)**0.5))
print "Period: ", 2*np.pi/((V/b*(C/A)**0.5)*(1-(-B/(2*(A*C)**0.5))**2)**0.5)
print "T1/2", -np.log(2)/re*b/V,"s"




