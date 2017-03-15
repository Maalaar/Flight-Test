# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 09:04:42 2017

@author: rensv
"""

#all the data
from Cit_par import *
from cog import *
from staticstability import *
import numpy as np

#find longitudinal eigenvalues, lecture 5 slide 32
muc = m/(rho19000*S*c)
labda = 1
leukematrix = np.array([[ CXu-2*muc*labda , CXa                     , CZ0    , 0                   ],\
                        [ CZu             , CZa+(CZadot-2*muc)*labda , -CX0   , CZq+2*muc           ],\
                        [ 0               , 0                       , -labda , 1                   ],\
                        [ Cmu             , Cma + Cmadot*labda      , 0      , Cmq-2*muc*KY2*labda ]])