import numpy as np
    
def pv_inv_string4(pt = None,pta = None,pto = None,ptc = None,sunS = None,piit = None,piita = None,piitc = None,piito = None,froS = None): 
    if pt == 0:
        St = np.array(['0'])
    else:
        St = sunS(pt(1))
    
    if piit == 0:
        Sit = np.array(['0'])
    else:
        l,c = piit.shape
        for i in np.arange(1,l+1).reshape(-1):
            Sit[i] = froS(piit(i,1))
    
    if pta == 0:
        Sta = np.array(['0'])
    else:
        Sta = sunS(pta(1))
    
    if piita == 0:
        Sita = np.array(['0'])
    else:
        l,c = piita.shape
        for i in np.arange(1,l+1).reshape(-1):
            Sita[i] = froS(piita(i,1))
    
    if ptc == 0:
        Stc = np.array(['0'])
    else:
        Stc = sunS(ptc(1))
    
    if piitc == 0:
        Sitc = np.array(['0'])
    else:
        l,c = piitc.shape
        for i in np.arange(1,l+1).reshape(-1):
            Sitc[i] = froS(piitc(i,1))
    
    if pto == 0:
        Sto = np.array(['0'])
    else:
        Sto = sunS(pto(1))
    
    if piito == 0:
        Sito = np.array(['0'])
    else:
        l,c = piito.shape
        for i in np.arange(1,l+1).reshape(-1):
            Sito[i] = froS(piito(i,1))
    
    return St,Sit,Sta,Sita,Sto,Sito,Stc,Sitc