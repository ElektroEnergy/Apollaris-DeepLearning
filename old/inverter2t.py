import numpy as np
    
def inverter2t(M_tilt = None,min_atemp = None,max_atemp = None,p = None,pt = None,Ntt = None,vfn = None,nf = None,alt = None,hum = None,freq = None): 
    
    # Prepared by: Gustavo Dill - 25/07/2017
# # # the power transformer are not being considered in the cost function of
# the inverter in this new version - april/2019
    pos_t = []
    pos_atem = []
    pos_p = []
    pos_v = []
    pit = []
    ptt = []
    
    #########################################################################################
# FOR TILTED INSTALATION
    if len(p)==0 == 1:
        print('NO AVALIABLE INVERTERS FOR THE SPECIFIED AREA')
        Nit = 0
        Cit = 0
        Ct = 0
        Nt = 0
        Npit = 0
        Nft = 0
        Npt1 = 0
        tt = 0
        NS = 0
        return Nit,Cit,pit,Nt,Ct,ptt,Npit,Nft,Npt1,tt,NS
    else:
        # Viable Inverters with MPPT
        n = 1
        l,c = p.shape
        for i in np.arange(1,l+1).reshape(-1):
            if p(i,32) == 10:
                pos_t[n,:] = p(i,:)
                Ntt_t[n,:] = Ntt(i,:)
                n = n + 1
    
    ######################################################################################
    if len(pos_t)==0 == 1:
        print('NO AVALIABLE INVERTERS FOR ON-GRID SYSTEM')
        Nit = 0
        Cit = 0
        Ct = 0
        Nt = 0
        Npit = 0
        Nft = 0
        Npt1 = 0
        tt = 0
        NS = 0
        return Nit,Cit,pit,Nt,Ct,ptt,Npit,Nft,Npt1,tt,NS
    else:
        pos_v,ttt,ft,Ntt_v = volt_t1(pos_t,vfn,nf,Ntt_t)
    
    #################################################################################
    
    if len(pos_v)==0 == 1:
        print('NO AVALIABLE INVERTERS FOR THE VOLTAGE DISTRIBUTION SYSTEM CONNECTION')
        Nit = 0
        Cit = 0
        Cpt = 0
        Npt = 0
        Npit = 0
        Nft = 0
        Npt1 = 0
        tt = 0
        NS = 0
        return Nit,Cit,pit,Nt,Ct,ptt,Npit,Nft,Npt1,tt,NS
    else:
        # Viable Inverters according to the temperature, frequency, humidity and altitud of the System
        o = 1
        l1,c1 = pos_v.shape
        for i in np.arange(1,l1+1).reshape(-1):
            if ((pos_v(i,23) >= max_atemp) and (pos_v(i,22) <= min_atemp)):
                if ((pos_v(i,16) <= freq) and (pos_v(i,17) >= freq)):
                    if pos_v(i,30) >= hum:
                        if pos_v(i,31) >= alt:
                            pos_atem[o,:] = pos_v(i,:)
                            Ntt_atem[o,:] = Ntt_v(i,:)
                            Nittt[o,1] = np.ceil(M_tilt(pos_atem(o)) / pos_atem(o,10))
                            o = o + 1
    
    if len(pos_atem)==0 == 1:
        print('NO AVALIABLE INVERTERS FOR THE TEMPERATURE CHOOSEN')
        Nit = 0
        Cit = 0
        Ct = 0
        Nt = 0
        Npit = 0
        Nft = 0
        Npt1 = 0
        tt = 0
        NS = 0
        return Nit,Cit,pit,Nt,Ct,ptt,Npit,Nft,Npt1,tt,NS
    else:
        # Viable Inverters according to the maximum output power (bounded by 85# to 130#
# of the inverter power
        p = 1
        l2,c2 = pos_atem.shape
        for i in np.arange(1,l2+1).reshape(-1):
            if (((np.multiply(Nittt(i),pos_atem(i,10))) >= M_tilt(pos_atem(i)) * 0.85) and ((np.multiply(Nittt(i),pos_atem(i,10))) <= M_tilt(pos_atem(i)) * 1.3)):
                pos_p[p,:] = pos_atem(i,:)
                Ntt_p[p,:] = Ntt_atem(i,:)
                Nitt[p,1] = Nittt(i)
                # Computing Citt with or without power transformer cost
                if ttt(p,1) == 1:
                    Citt[p,1] = np.multiply(pos_atem(i,28),Nitt(p,1)) + (pos_atem(i,28) * ft)
                else:
                    Citt[p,1] = np.multiply(pos_atem(i,28),Nitt(p,1))
                p = p + 1
    
    if len(pos_p)==0 == 1:
        print('NO AVALIABLE INVERTERS FOR THE POWER NEEDED')
        Nit = 0
        Cit = 0
        Ct = 0
        Nt = 0
        Nt1 = 0
        Npit = 0
        Nft = 0
        Npt1 = 0
        tt = 0
        NS = 0
        return Nit,Cit,pit,Nt,Ct,ptt,Npit,Nft,Npt1,tt,NS
    
    # Number of PV strings in series
    voc_max = np.multiply(pt(:,2),(1 + (np.multiply((pt(:,26) - 25),pt(:,8)))))
    vmp_min = np.multiply(pt(:,4),(1 + (np.multiply((pt(:,26) - 25),pt(:,9)))))
    l3,c3 = pos_p.shape
    l4,c4 = pt.shape
    p = 1
    q = 1
    for j in np.arange(1,l4+1).reshape(-1):
        for i in np.arange(1,l3+1).reshape(-1):
            # Ns_max(i,j)=pos_p(i,4)/voc_max(j); #Maximum number of pv by string
# Ns_min(i,j)=pos_p(i,2)/vmp_min(j); #Minimum number of pv by string
            Np_max1[i,j] = pos_p(i,3)
            #Nttt(i,j)=Ntt(pos_p(i),j); #Number of Pvs
            Nttt[i,j] = Ntt_p(i,j)
            NN[i,j] = Nttt(i,j) / Nitt(i,1)
            Nfft[i,j] = np.ceil(Nttt(i,j) / (np.multiply(Nitt(i),Np_max1(i,j))))
            NSS[i,j] = int(np.floor(pos_p(i,2) / pt(j,5)))
            if NSS(i,j) != 0:
                NSS[i,j] = NSS(i,j)
            else:
                NSS[i,j] = 1
            if NSS(i,j) >= pos_p(i,9):
                NoDC[i,j] = pos_p(i,9)
            else:
                NoDC[i,j] = NSS(i,j)
            Nmpp = pos_p(i,3)
            VmpptM = pos_p(i,6)
            Vmpptm = pos_p(i,5)
            voc = voc_max(j)
            vmp = vmp_min(j)
            Nff = Nstrings(Nitt(i,1),Nttt(i,j),NoDC(i,j),Nmpp,VmpptM,Vmpptm,voc,vmp)
            #  if (ceil(NDmin(i,j)).*vmp_min(j) > pos_p(i,5)) && (ceil(NDmax(i,j)).*voc_max(j) < pos_p(i,6))
            if ((np.multiply(np.amin(Nff),vmp) > Vmpptm) and (np.multiply(np.amax(Nff),voc) < VmpptM)):
                if ((np.multiply(np.ceil(NN(i,j)),pt(j,6)) < pos_p(i,10)) and ((np.multiply(NoDC(i,j),pt(j,5))) <= pos_p(i,2))):
                    pit[p,j] = pos_p(i,1)
                    Npt1[p,j] = Np_max1(i,j)
                    Npit[p,j] = NN(i,j)
                    Nt[p,j] = Nttt(i,j)
                    NS[p,j] = NSS(i,j)
                    ptt[q,:] = pt(j,:)
                    Nit[p,j] = Nitt(i)
                    Cit[p,j] = Citt(i)
                    tt[p,j] = ttt(i)
                    #Nft(p,j)=Nff
                    Nft[p,j] = Nff
                    Ct[p,j] = np.multiply(Nt(p,j),pt(j,15))
                    p = p + 1
        p = 1
        q = q + 1
    
    if len(pit)==0 == 1:
        print('NO AVALIABLE INVERTERS FOR THE NUMBER OF SOLAR PAINEL NEEDED')
        Nit = 0
        Cit = 0
        Ct = 0
        Nt = 0
        Npit = 0
        Nft = 0
        Npt1 = 0
        tt = 0
        NS = 0
        return Nit,Cit,pit,Nt,Ct,ptt,Npit,Nft,Npt1,tt,NS
    
    return Nit,Cit,pit,Nt,Ct,ptt,Npit,Nft,Npt1,tt,NS