import numpy as np
    
def pv_inv_string2(pt = None,pta = None,pto = None,ptc = None,sunS = None,pit = None,pita = None,pito = None,pitc = None,froS = None): 
    if pt == 0:
        St = np.array(['0'])
    else:
        St = sunS(pt(1))
    
    if pit == 0:
        Sit = np.array(['0'])
    else:
        Sit = froS(pit(1))
    
    if pta == 0:
        Sta = np.array(['0'])
    else:
        Sta = sunS(pta(1))
    
    if pita == 0:
        Sita = np.array(['0'])
    else:
        Sita = froS(pita(1))
    
    if ptc == 0:
        Stc = np.array(['0'])
    else:
        Stc = sunS(ptc(1))
    
    if pitc == 0:
        Sitc = np.array(['0'])
    else:
        Sitc = froS(pitc(1))
    
    if pto == 0:
        Sto = np.array(['0'])
    else:
        Sto = sunS(pto(1))
    
    if pito == 0:
        Sito = np.array(['0'])
    else:
        Sito = froS(pito(1))
    
    return St,Sit,Sta,Sita,Sto,Sito,Stc,Sitc