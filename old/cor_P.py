import numpy as np
    
def cor_P(pit = None,P_tilt = None): 
    
    if pit(1) == 0:
        P_tilt = np.zeros((1,12))
    else:
        P_tilt = P_tilt(pit(1),:)
    
    return P_tilt