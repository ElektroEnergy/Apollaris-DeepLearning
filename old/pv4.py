import numpy as np
    
def pv4(area = None,M_tilt = None,sunN = None,froN = None,pv_mo = None): 
    
    # Prepared by: Gustavo Dill - 25/07/2017
    
    pt = []
    pd = []
    pdf = []
    pg = []
    p = []
    p1 = []
    p2 = []
    p3 = []
    # Voltage correction for the ambient temperature
    voc_max = sunN(pv_mo,2) * (1 + (np.multiply((sunN(pv_mo,26) - 25),sunN(pv_mo,8))))
    vmp_min = sunN(pv_mo,4) * (1 + (np.multiply((sunN(pv_mo,26) - 25),sunN(pv_mo,9))))
    isc_max = np.multiply(sunN(pv_mo,3),(1 + (np.multiply((sunN(pv_mo,27) - 25),sunN(pv_mo,10)) / 100)))
    
    pcor_min = np.multiply(vmp_min,sunN(pv_mo,5))
    
    pcor_max = np.multiply(voc_max,sunN(pv_mo,5))
    
    # area  = Area (m) area=(len+0.1m+0.1m)*(wid+0.1m+0.1m)
    a = np.multiply(((sunN(pv_mo,13) / 1000) + 0.1 + 0.1),((sunN(pv_mo,14) / 1000) + 0.1 + 0.1))
    #extra=extra(pv_mo,:)
    minTemp = sunN(pv_mo,28)
    maxTemp = sunN(pv_mo,27)
    # Calculate the number of PV and the Power of the PV
    u,v = froN.shape
    x = 1
    y = 1
    z = 1
    w = 1
    for i in np.arange(1,u+1).reshape(-1):
        NN_tilt[i,1] = np.ceil(M_tilt(i) / pcor_min)
        # Viable PVs according to the area of the PV System
        if (np.multiply(a,NN_tilt(i,1)) < area):
            if ((sunN(i,22) <= minTemp) and (sunN(i,23) >= maxTemp)):
                #if (isc_max.*1.5)<=sunN(i,25)
                p[x,:] = froN(i,:)
                Nttt[x,1] = NN_tilt(i,1)
                x = x + 1
                #end
    
    if len(p)==0 == 1:
        print('NO AVALIABLE PVs FOR THE SPECIFIED AREA OR TEMPERATURE BOUNDARY')
        Ntt = 0
    else:
        Ntt = Nttt
        pt = sunN(pv_mo,:)
    
    return Ntt,pt,p