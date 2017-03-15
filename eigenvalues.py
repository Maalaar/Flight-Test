
from sympy import *
x, y = symbols('x y')

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


def eigenvaluesasym(Cybeta,Cybetadot,mub,CL,Cyp,Cyr,Clbeta,Clp,Kx2,Clr,Kxz,Cnbeta,Cnbetadot,Cnp,Cnr,Kz2): #nog niet goed
    

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


print eigenvaluessym(-0.2199,102.7,0.4653,-1.1360,-2.2720,-5.16,-1.43,0,-3.86,0,-0.43,-3.7,-7.04,0.98)

print eigenvaluesasym(-0.9896,0,15.5,1.136,-0.0870,0.43,-0.0772,-0.3444,0.012,0.28,0.002,0.1638,0,-0.0108,-0.193,0.037)
