import numpy as np
    
def pv2(area = None,M_tilt = None,sunN1 = None,froN = None): 
    
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
    voc_max = np.multiply(sunN1(:,2),(1 + (np.multiply((sunN1(:,26) - 25),sunN1(:,8)))))
    vmp_min = np.multiply(sunN1(:,4),(1 + (np.multiply((sunN1(:,26) - 25),sunN1(:,9)))))
    isc_max = np.multiply(sunN1(:,3),(1 + (np.multiply((sunN1(:,27) - 25),sunN1(:,10)) / 100)))
    
    pcor_min = np.multiply(vmp_min,sunN1(:,5))
    
    pcor_max = np.multiply(voc_max,sunN1(:,5))
    
    # area  = Area (m) area=(len+0.1m+0.1m)*(wid+0.1m+0.1m)
    a = np.multiply(((sunN1(:,13) / 1000) + 0.1 + 0.1),((sunN1(:,14) / 1000) + 0.1 + 0.1))
    minTemp = sunN1(:,28)
    maxTemp = sunN1(:,27)
    # Calculate the number of PV and the Power of the PV
    x = 1
    y = 1
    z = 1
    w = 1
    xx = 1
    yy = 1
    zz = 1
    ww = 1
    l,c = sunN1.shape
    ll,cc = froN.shape
    for i in np.arange(1,l+1).reshape(-1):
        for j in np.arange(1,ll+1).reshape(-1):
            NN_tilt[j,i] = np.ceil(M_tilt(j) / pcor_min(i))
            # Viable PVs according to the area of the PV System
            if (np.multiply(a(i,1),NN_tilt(j,i)) < area):
                if ((sunN1(i,22) <= minTemp(i)) and (sunN1(i,23) >= maxTemp(i))):
                    # if (1.5*isc_max(i))<=sunN1(i,25)
                    pt[xx,:] = sunN1(i,:)
                    p[x,:] = froN(j,:)
                    Ntt[x,xx] = NN_tilt(j,i)
                    x = x + 1
                    #end
        x = 1
        y = 1
        z = 1
        w = 1
        xx = xx + 1
        yy = yy + 1
        zz = zz + 1
        ww = ww + 1
    
    if len(pt)==0 == 1:
        print('NO AVALIABLE PVs FOR THE SPECIFIED AREA OR TEMPERATURE BOUNDARY')
        Ntt = 0
    else:
        # to eliminte null elements
        pto = pt
        Ntto = Ntt
        li,ci = pt.shape
        for i in np.arange(1,li+1).reshape(-1):
            if sum(pt(li + 1 - i,:)) == 0:
                pto[li + 1 - i,:] = []
                Ntto[:,li + 1 - i] = []
        pt = pto
        Ntt = Ntto
    
    return Ntt,pt,p