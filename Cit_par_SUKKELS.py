import numpy as np
# Citation 550 - Linear simulation

# aerodynamic properties
e      =  0.87745470146438931  # Oswald factor [ ]
CD0    =  0.025563672225735336 # Zero lift drag coefficient [ ]
CLa    =  4.3517004179616956   # Slope of CL-alpha curve [ ]

# Longitudinal stability
Cma    =  -0.31562082555776361 # longitudinal stabilty [ ]
Cmde   =  -0.71816783630216641 # elevator effectiveness [ ]

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

# Constant values concerning atmosphere and gravity

rho0   = 1.2250          # air density at sea level [kg/m^3] 
lambda1 = -0.0065         # temperature gradient in ISA [K/m]
Temp0  = 288.15          # temperature at sea level in ISA [K]
R      = 287.05          # specific gas constant [m^2/sec^2K]
g      = 9.81            # [m/sec^2] (gravity constant)

KX2    = 0.019
KZ2    = 0.042
KXZ    = 0.002
KY2    = 1.25 * 1.114

# Aerodynamic constants

Cmac   = 0.5                      # Moment coefficient about the aerodynamic centre [ ]
CNwa   = CLa                    # Wing normal force slope [ ]
CNha   = 2 * np.pi * Ah / (Ah + 2) # Stabiliser normal force slope [ ]
depsda = 4 / (A + 2)            # Downwash gradient [ ]

CXu    = -0.02792
CXa    = -0.47966
CXadot = +0.08330
CXq    = -0.28170
CXde   = -0.03728
    
CZu    = -0.37616
CZa    = -5.74340
CZadot = -0.00350
CZq    = -5.66290
CZde   = -0.69612

Cmu    = +0.06990
Cmadot = +0.17800
Cmq    = -8.79415

CYb    = -0.7500
CYbdot =  0     
CYp    = -0.0304
CYr    = +0.8495
CYda   = -0.0400
CYdr   = +0.2300

Clb    = -0.10260
Clp    = -0.71085
Clr    = +0.23760
Clda   = -0.23088
Cldr   = +0.03440

Cnb    =  +0.1348
Cnbdot =   0     
Cnp    =  -0.0602
Cnr    =  -0.2061
Cnda   =  -0.0120
Cndr   =  -0.0939

def kutmaarten(V0,alpha0,th0,W,hp):
    # air density [kg/m^3]
    hp0     = hp*0.3048
    alpha0  *= (np.pi/180)
    th0     *= (np.pi/180)
    rho     =  rho0 * np.power( ((1+(lambda1 * int(hp0) / Temp0))), (-((g / (lambda1*R)) + 1)))
    m       =  W/g

    # Constant values concerning aircraft inertia

    muc    = m / (rho * S * c) 
    mub    = m / (rho * S * b) 

    # Lift and drag coefficient
<<<<<<< HEAD
#    print m, V0, rho, W, S, hp0
    CL = 2 * W / (rho * (V0**2) * S)              # Lift coefficient [ ]
=======
    #print m, V0, rho, W, S, hp0
    CL = 2 * W / (rho * V0 ** 2 * S)              # Lift coefficient [ ]
>>>>>>> f70bb088f9838384a3ce93586e45659c39da9148
    CD = CD0 + (CLa * alpha0) ** 2 / (np.pi * A * e) # Drag coefficient [ ]

    # Stabiblity derivatives

    CX0    = W * np.sin(th0) / (0.5 * rho * V0 ** 2 * S)


    CZ0    = -W * np.cos(th0) / (0.5 * rho * V0 ** 2 * S)

<<<<<<< HEAD
    print rho,muc,mub,CL,CD,CX0,CZ0
    return rho,muc,mub,CL,CD,CX0,CZ0

=======
    
    return "FUCK JOU"
>>>>>>> f70bb088f9838384a3ce93586e45659c39da9148
