#returns weight in Newton & x_cg in meters
def cog (W_f):
    
    CitationW = 9165. #pounds
    CitationM = 2677847.5 #inchpounds
    CrewW = 1558.67 #pounds
    CrewM = 337047.12 #inchpounds
    
    from fuelmoment import fuelmoment
    StartFuelW = 4150. #pounds
    FuelW = StartFuelW - W_f #pounds
    FuelM=[]
    for i in range(len(W_f)):
        FuelM.append ( 100*fuelmoment(W_f[i], StartFuelW)) #inchpounds
    FuelM=np.array(FuelM)
    TotalW = CitationW + CrewW + FuelW #pounds
    g = 9.81
    lbstokg = 0.45359237
    W = TotalW*lbstokg*g #Newton
    
    TotalM = CitationM + CrewM + FuelM #inchpounds
    x_cginch = TotalM / TotalW #inches
    inchtometers = 0.0254
    x_cg = x_cginch * inchtometers
    
    return (W, x_cg)
    
    
#als Rens voorin gaat zitten, gebruik deze
def cog2 (W_f):
    
    CitationW = 9165. #pounds
    CitationM = 2677847.5 #inchpounds
    CrewW = 1558.67 #pounds
    CrewM = 311186.89 #inchpounds
    
    from fuelmoment import fuelmoment
    StartFuelW = 4150. #pounds
    FuelW = StartFuelW - W_f #pounds
    
    for i in range(len(W_f)):
        FuelM.append (100*fuelmoment(W_f[i], StartFuelW)) #inchpounds
    FuelM=np.array(FuelM)
    
    TotalW = CitationW + CrewW + FuelW #pounds
    g = 9.81
    lbstokg = 0.45359237
    W = TotalW*lbstokg*g #Newton
    
    TotalM = CitationM + CrewM + FuelM #inchpounds
    x_cginch = TotalM / TotalW #inches
    inchtometers = 0.0254
    x_cg = x_cginch * inchtometers
    
    return (W, x_cg)
