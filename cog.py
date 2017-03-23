#returns weight in Newton & x_cg in meters
import numpy as np

def cog (W_f):
    
    CitationW = 9165. #pounds
    CitationM = 2677847.5 #inchpounds
    CrewW = 1558.67 #pounds
    CrewM = 337047.12 #inchpounds
    
    from fuelmoment import fuelmoment
    StartFuelW = 4150. #pounds
    
    
    FuelM=[]
    FuelW=[]
    for i in range(len(W_f)):
        FuelM.append ( 100.*fuelmoment(W_f[i], StartFuelW)) #inchpounds
        FuelW.append( StartFuelW - W_f[i]) #pounds
    FuelM=np.array(FuelM)
    
    FuelW=np.array(FuelW)
    TotalW = CitationW + CrewW + FuelW #pounds
    g = 9.81
    lbstokg = 0.45359237
    W = TotalW*lbstokg*g #Newton
    TotalM=[]
    for i in range(len(FuelM)):
                   TotalM.append(CitationM + CrewM + FuelM[i]) #inchpounds
    
    #print TotalM
    #print TotalM
    
    x_cginch = TotalM / TotalW #inches
    inchtometers = 0.0254
    x_cg = x_cginch * inchtometers
    
    return (W, x_cg)
    
    
#als Rens voorin gaat zitten, gebruik deze
def cog2 (W_f):
    
    CitationW = 9165. #pounds
    CitationM = 2677847.5 #inchpounds
    CrewW = 1558.67 #pounds
    CrewM = 311186.89 #inchpounds #deze verschilt als Rens verplaatst, verder nieks
    
    from fuelmoment import fuelmoment
    StartFuelW = 4150. #pounds
    FuelM=[]
    FuelW=[]
    for i in range(len(W_f)):
        FuelM.append (100*fuelmoment(W_f[i], StartFuelW)) #inchpounds
        FuelW.append( StartFuelW - W_f[i]) #pounds
    FuelM=np.array(FuelM)
    FuelW=np.array(FuelW)
    
    TotalW = CitationW + CrewW + FuelW #pounds
    g = 9.81
    lbstokg = 0.45359237
    W = TotalW*lbstokg*g #Newton
    
    TotalM = CitationM + CrewM + FuelM #inchpounds
    x_cginch = TotalM / TotalW #inches
    inchtometers = 0.0254
    x_cg = x_cginch * inchtometers
    
    return (W, x_cg)


l3=[]
l4=[]
for i in range(4000):
    l1=[]
    l1.append(float(i))
    l3.append(i)
    jaja = cog([float(i)])
    
    l4.append(jaja[1])

import matplotlib.pyplot as plt

plt.plot(l3,l4)
plt.show()

    
