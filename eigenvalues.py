
from sympy import *
x, y = symbols('x y')

def eigenvalues(Cxu,mu,Cxalpha,Cz0,Czu,Czalpha,Czalphadot,Cx0,Czq,Cmu,Cmalpha,Cmalphadot,Cmq,Ky2):
    

    A1=Cxu-2*mu*x
    A2=Cxalpha
    A3=Cz0
    A4=0
    A5=Czu
    A6=Czalpha+(Czalphadot-2*mu)*x
    A7=-Cx0
    A8=Czq+2*mu
    A9=0
    A10=0
    A11=-x
    A12=1
    A13=Cmu
    A14=Cmalpha+Cmalphadot*x
    A15=0
    A16=Cmq-2*mu*Ky2*x

    block1=  A1* ( A6*(A11*A16-A12*A15)-A7*(A10*A16-A12*A14)+A8*(A10*A15-A11*A14))
    block2= - A2* (A5*(A11*A16-A12*A15)-A7*(A9*A16-A12*A13)+A8*(A9*A15-A11*A13))
    block3= A3* ( A5*(A10*A16-A12*A14)-A6*(A9*A16-A12*A13)+A8*(A9*A14-A10*A13))
    block4= -A4*(A5*(A10*A15-A11*A14)-A6*(A9*A15-A11*A13)+A7*(A9*A14-A10*A13))

    return solve(Eq(block1+block2+block3+block4, 0), x)


