import numpy as np
    
def month_hour(y = None): 
    #    jan fev mar apr mai jun jul ago set out nov dez
    mon = np.array([31,28,31,30,31,30,31,31,30,31,30,31])
    ml,mc = mon.shape
    for i in np.arange(1,mc+1).reshape(-1):
        h[1,i] = np.multiply(mon(i),y(1,i))
    
    return h