import numpy as np
    
def protection_system(pvv = None,inv = None,nft = None,max_atemp = None,Nt = None,Nit = None,wind_speed = None,NSt = None): 
    if np.all(pvv < 0.01):
        #disp('NO AVALIABLE INVERTERS FOR THE NUMBER OF SOLAR PAINEL NEEDED')
        voc_string = nan
        sec_string = nan
        Is_min = nan
        Is_max = nan
        Vdio = nan
        Idio = nan
        voc_arranjo = nan
        sec_arranjo = nan
        Ia_min = nan
        Ia_max = nan
        dps_ca = nan
        sec_ca = nan
        Id_min = nan
        Id_max = nan
        txt = 'nan'
        return voc_string,sec_string,Is_min,Is_max,Vdio,Idio,voc_arranjo,sec_arranjo,Ia_min,Ia_max,dps_ca,sec_ca,Id_min,Id_max,txt
    
    TA = max_atemp
    nr = pvv(1,16)
    beta = pvv(1,10)
    Tr = 25
    E1 = 1290
    upv_min = 17.1 + np.multiply(np.multiply(5.7,wind_speed),0.1)
    # correcting the temperature for isc
    max_temp = (np.multiply(upv_min,max_atemp) + np.multiply(E1,(0.81 - nr - (np.multiply(np.multiply(beta,nr),Tr))))) / (upv_min - np.multiply(np.multiply(beta,nr),E1))
    isc = np.multiply(pvv(1,3),(1 + (np.multiply((max_temp - Tr),pvv(1,10)) / 100)))
    nft = str2num(nft)
    Nt = Nt
    Nit = Nit
    inop = pvv(1,25)
    voc = pvv(1,2)
    Nmppt = inv(1,3)
    NoDc = NSt
    Pinv = inv(1,12)
    FCT = np.array([10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,1.15,1.12,1.8,1.04,0.96,0.91,0.87,0.82,0.76,0.71,0.65,0.58,0.5,0.41,0.4])
    # Finding the nearest value of FCT
    dist = np.abs(FCT(1,:) - TA)
    minDist = np.amin(dist)
    idx = find(dist == minDist)
    fct = FCT(2,idx)
    #     secao     cap    quedaVA/km Visol.   Ta
    CB_cc = np.array([1.5,25,38.17,1800,60,2.5,34,22.87,1800,60,4.0,45,14.18,1800,60,6.0,57,9.445,1800,60,10.0,79,5.433,1800,60,16.0,105,3.455,1800,60,25.0,140,2.215,1800,60,35.0,174,1.574,1800,60,50.0,219,1.095,1800,60,70.0,273,0.7717,1800,60,95.0,328,0.5851,1800,60,120.0,385,0.4569,1800,60,150.0,443,0.3678,1800,60,185.0,506,0.3009,1800,60,240.0,606,0.2276,1800,60,300.0,700,0.1822,1800,60,400.0,842,0.1379,1800,60])
    #     secao  2cond     3cond    Visol.    Ta
    CB_ca = np.array([1.5,17,15.5,600,30,2.5,24,21,600,30,4.0,32,28,600,30,6.0,41,36,600,30,10.0,57,50,600,30,16.0,76,68,600,30,25.0,101,89,600,30,35.0,125,111,600,30,50.0,151,134,600,30,70.0,192,171,600,30,95.0,232,207,600,30,120.0,269,239,600,30,150.0,307,275,600,30,185.0,353,314,600,30,240.0,415,369,600,30,300.0,472,420,600,30])
    ############################### STRING DESING #############################
# capacidade de conducao de corrente de cada string do lado CC
    for i in np.arange(1,len(nft)+1).reshape(-1):
        if nft(i) != 0:
            Is[i] = 1.5 * isc
            idx = find(CB_cc(:,2) > Is(i),1,'first')
            sec_string[i] = CB_cc(idx,1)
        else:
            Is[i] = 0
            sec_string[i] = 0
        voc_string[i] = nft(i) * voc
    
    sec_string = np.transpose(nonzeros(sec_string))
    voc_string = np.transpose(nonzeros(voc_string))
    Is_min = np.transpose(nonzeros(Is))
    Is_max = np.multiply(Is_min,1.6)
    for i in np.arange(1,len(Is_max)+1).reshape(-1):
        if Is_max(i) < inop:
            Is_max[i] = Is_max(i)
        else:
            Is_max[i] = inop
    
    # Dimensionamento do diodo de bloqueio para cada string
    Vdio = voc_string * 2
    
    Idio = 1.4 * isc * np.ones((1,len(sec_string)))
    
    ########################### ARRANJO DE STRINGS ############################
# capacidade de conducao de corrente do arranjo do lado CC
    if sum(nft(np.arange(1,NoDc+1))) != nft(1):
        v = np.transpose(nonzeros(nft))
        x = len(v)
        y = len(nft)
        par_NoDc = np.ceil((y - x) / NoDc)
        NoDc = NoDc - par_NoDc
        a = 1
        b = NoDc
        for i in np.arange(1,Nmppt * Nit+1).reshape(-1):
            NFT[i,:] = v(1,np.arange(a,b+1))
            Ia[i] = 1.5 * isc * len(NFT(i,:))
            Ia_min[i] = Ia(i)
            Ia_max[i] = Ia(i) * 1.6
            voc_arranjo[i] = v(a) * voc
            idx = find(CB_cc(:,2) > Ia(i),1,'first')
            sec_arranjo[i] = CB_cc(idx,1)
            a = a + NoDc
            b = NoDc + b
    else:
        voc_arranjo = nan
        sec_arranjo = nan
        Ia_min = nan
        Ia_max = nan
    
    ################## LADO CA ################################################
# DPS CA
    dps_ca = inv(1,15)
    # Cable CA
    Iproj = inv(1,11) / fct
    if inv(1,28) == 1:
        idx = find(CB_ca(:,2) > Iproj,1,'first')
        Iz = CB_ca(idx,2)
    else:
        idx = find(CB_ca(:,3) > Iproj,1,'first')
        Iz = CB_ca(idx,3)
    
    sec_ca = CB_cc(idx,1)
    # Breaker CA
    Id_min = Iproj
    Id_max = Iz
    #cells
    sec_string = num2str(sec_string)
    voc_string = num2str(voc_string)
    sec_arranjo = num2str(sec_arranjo)
    voc_arranjo = num2str(voc_arranjo)
    Is_min = num2str(Is_min)
    Is_max = num2str(Is_max)
    Ia_min = num2str(Ia_min)
    Ia_max = num2str(Ia_max)
    Idio = num2str(Idio)
    Vdio = num2str(Vdio)
    sec_ca = num2cell(sec_ca)
    dps_ca = num2cell(dps_ca)
    Id_min = num2cell(Id_min)
    Id_max = num2cell(Id_max)
    txt = 'yes'
    return voc_string,sec_string,Is_min,Is_max,Vdio,Idio,voc_arranjo,sec_arranjo,Ia_min,Ia_max,dps_ca,sec_ca,Id_min,Id_max,txt