import numpy as np
    
def Nstrings(Nitt = None,Nttt = None,NoDC = None,Nmpp = None,VmpptM = None,Vmpptm = None,voc = None,vmp = None): 
    # clc
# clear all
# Nitt=3; Nttt=71; NoDC=14; Nmpp=1; vmp=31.79; voc=38.38; VmpptM=850; Vmpptm=570;
    
    ###########################################################################
#                                                                         #
# CODE USED TO SELECT AND SUPPLY SEVERAL OPTIONS OF STRINGS AVAILABLE FOR #
#EACH COMBINATION OF SOLAR MODULE AND INVERTERS                           #
#                                                                         #
# PREPARED BY: GUSTAVO KAEFER DILL - MARCH 2020                           #
#                                                                         #
# Preferencia de uma string por mppt para evitar que caso uma string tenha#
# menos irradiação que a outra de de prob na tensao do inv, segunda prefe #
# rencia é de uma string por inversor. caso não seja possível, combinações#
# entre os NoDC e MPPT podem ser feitas para alocar os módulos adequados  #
# para cada inversor. O objetivo é evitar strings em paralelo em um mesmo #
# mppt porque havendo sombreamento em uma string inviabiliza-se a produção#
# da outra                                                                #
#                                                                         #
###########################################################################
    Nff = []
    NS = np.multiply(np.multiply(Nitt,Nmpp),NoDC)
    
    NSS = np.multiply(Nmpp,NoDC)
    
    Npvi = Nttt / Nitt
    
    Nf = Nttt / NS
    
    ND = np.zeros((5,NS))
    ####################### CASO 4 ########################################
    a = 1
    b = 1
    c = 1
    d = NoDC + 1
    e = 1
    f = NoDC
    g = NoDC + 1
    h = NoDC + Nmpp
    m = 1
    n = NoDC
    o = NoDC + 1
    for k in np.arange(1,Nitt+1).reshape(-1):
        if int(np.floor(Nf)) == np.ceil(Nf):
            ND[4,np.arange[c,[k * Nmpp * NoDC]+1]] = Nf
            c = c + (Nmpp * NoDC)
    
    ###########################################################################
    
    #################### CASO 3 ###############################################
    if (Nitt * Nmpp) < Nttt:
        if ((Nmpp > 1) and (NoDC == 1)):
            Nffy = Nttt / (Nitt * Nmpp)
            runsum = 0
            a3 = 1
            b3 = 1
            for i in np.arange(1,Nitt+1).reshape(-1):
                for j in np.arange(1,(Nmpp)+1).reshape(-1):
                    if rem(Nffy,1) <= 0.5:
                        ND[3,a3] = int(np.floor(Nffy))
                    else:
                        ND[3,a3] = np.ceil(Nffy)
                    int_ = ND(3,a3)
                    runsum = runsum + int_
                    Nffy = (Nttt - runsum) / ((Nitt * Nmpp) - (b3))
                    a3 = a3 + 1
                    b3 = b3 + 1
                a3 = i * Nmpp + 1
    
    # ###########
    if (Nitt * NoDC) < Nttt:
        if ((Nmpp == 1) and (NoDC > 1)):
            Nffy = Nttt / (Nitt * NoDC)
            Nffz = Npvi
            runsum = 0
            a3 = 1
            b3 = 2
            c3 = 1
            if int(np.floor(Nffy)) == np.ceil(Nffy):
                for j in np.arange(1,(Nitt * NoDC)+1).reshape(-1):
                    ND[3,c3] = Nffy
                    c3 = c3 + 1
            if ((int(np.floor(Nffy)) != np.ceil(Nffy)) and (Nitt == 1)):
                ND[3,1] = Nttt
            if ((int(np.floor(Nffy)) != np.ceil(Nffy)) and (Nitt > 1)):
                for k in np.arange(1,Nitt+1).reshape(-1):
                    if rem(Nffz,1) <= 0.5:
                        ND[3,a3] = int(np.floor(Nffz))
                    else:
                        ND[3,a3] = np.ceil(Nffz)
                    int_ = ND(3,a3)
                    runsum = runsum + int_
                    Nffz = (Nttt - runsum) / (Nitt - k)
                    a3 = a3 + NoDC
                    b3 = b3 - 1
    
    ##############
    if (Nitt * ((Nmpp * NoDC) - 1)) < Nttt:
        if ((Nmpp > 1) and (NoDC > 1)):
            Nffx = Nttt / (Nitt * Nmpp * NoDC)
            Nffw = Nttt / (Nitt * ((Nmpp * NoDC) - 1))
            runsum = 0
            runsum1 = 0
            a3 = 1
            b3 = 1
            c3 = 1
            aa3 = NoDC * (Nmpp - 1) + 1
            bb3 = 1
            if int(np.floor(Nffx)) == np.ceil(Nffx):
                for j in np.arange(1,(Nitt * NoDC * Nmpp)+1).reshape(-1):
                    ND[3,c3] = Nffx
                    c3 = c3 + 1
            else:
                for i in np.arange(1,Nitt+1).reshape(-1):
                    for j in np.arange(1,NoDC * (Nmpp - 1)+1).reshape(-1):
                        if rem(Nffw,1) <= 0.5:
                            ND[3,a3] = int(np.floor(Nffw))
                        else:
                            ND[3,a3] = np.ceil(Nffw)
                        int_ = ND(3,a3)
                        runsum = runsum + int_
                        a3 = a3 + 1
                    a3 = i + i * ((Nmpp * NoDC) - 1) + 1
                Nffw = (Nttt - runsum) / Nitt
                for i in np.arange(1,Nitt+1).reshape(-1):
                    if rem(Nffw,1) <= 0.5:
                        ND[3,aa3] = int(np.floor(Nffw))
                    else:
                        ND[3,aa3] = np.ceil(Nffw)
                    int1 = ND(3,aa3)
                    runsum1 = runsum1 + int1
                    Nffw = (((Nttt - runsum) - runsum1) / ((Nitt - (bb3))))
                    aa3 = aa3 + NoDC * Nmpp
                    bb3 = bb3 + 1
    
    ##########################################################################
    
    ################# CASO 1 ##################################################
# Alocar uma string por mppt
    if (Nitt * Nmpp) < Nttt:
        if Nmpp > 1:
            Nffv = Nttt / (Nitt * Nmpp)
            runsum = 0
            a4 = 1
            b4 = 1
            c4 = 1
            if int(np.floor(Nffv)) == np.ceil(Nffv):
                for j in np.arange(1,(Nitt * Nmpp)+1).reshape(-1):
                    ND[1,c4] = Nffv
                    c4 = c4 + NoDC
            else:
                for j in np.arange(1,Nitt * Nmpp+1).reshape(-1):
                    if rem(Nffv,1) <= 0.5:
                        ND[1,a4] = int(np.floor(Nffv))
                    else:
                        ND[1,a4] = np.ceil(Nffv)
                    int_ = ND(1,a4)
                    runsum = runsum + int_
                    Nffv = (Nttt - runsum) / (Nitt * Nmpp - j)
                    a4 = a4 + NoDC
    
    ###########################################################################
    
    #########################  CASO 5  ########################################
    if Nitt < Nttt:
        runsum = 0
        Nffu = Npvi
        a5 = 1
        b5 = 1
        c5 = 1
        if int(np.floor(Nffu)) == np.ceil(Nffu):
            for j in np.arange(1,(Nitt)+1).reshape(-1):
                ND[2,c5] = Nffu
                c5 = c5 + Nmpp * NoDC
        else:
            for j in np.arange(1,Nitt+1).reshape(-1):
                if rem(Nffu,1) <= 0.5:
                    ND[2,a5] = int(np.floor(Nffu))
                else:
                    ND[2,a5] = np.ceil(Nffu)
                int_ = ND(2,a5)
                runsum = runsum + int_
                Nffu = (Nttt - runsum) / (Nitt - j)
                a5 = a5 + (NoDC * Nmpp)
    
    ###########################################################################
    
    ########################  CASO 2  #########################################
    if (((Nitt * Nmpp * NoDC) < Nttt) and ((NoDC > 1))):
        if (((np.mod(NoDC,2) != 1)) and (Nmpp > 1)):
            Nffz = Nttt / NS
            runsum = 0
            a2 = 1
            b2 = NoDC + 1
            c2 = 1
            bb2 = NoDC + 1
            if int(np.floor(Nffz)) != np.ceil(Nffz):
                for i in np.arange(1,Nitt+1).reshape(-1):
                    for j in np.arange(1,NoDC+1).reshape(-1):
                        if rem(Nffz,1) <= 0.5:
                            ND[5,a2] = int(np.floor(Nffz))
                        else:
                            ND[5,a2] = np.ceil(Nffz)
                        int_ = ND(5,a2)
                        runsum = runsum + int_
                        a2 = a2 + 1
                    a2 = (NoDC * Nmpp) + i
                Nffzz = (Nttt - runsum) / (NS - Nitt * NoDC)
                if int(np.floor(Nffzz)) == np.ceil(Nffzz):
                    for i in np.arange(1,Nitt+1).reshape(-1):
                        for j in np.arange(1,NoDC+1).reshape(-1):
                            ND[5,b2] = Nffzz
                            b2 = b2 + 1
                        b2 = (NoDC * Nmpp) + bb2 * i
                else:
                    ND[5,:] = np.zeros((1,Nitt * Nmpp * NoDC))
    
    ND = ND(not np.all(ND == 0,2) ,:)
    # if Nttt >=50
#     NDa(1,:)=ND(4,:);
#     NDa(4,:)=ND(1,:);
#     NDa(2,:)=ND(5,:);
#     NDa(5,:)=ND(2,:);
#     ND=NDa;
# end
    
    NDA = ND
    NDA[NDA == 0] = nan
    NDmin = np.amin(NDA,[],2)
    NDmax = np.transpose(np.amax(np.transpose(ND)))
    # for i=1:length(NDmin)
#    if ((NDmin(i).*vmp > Vmpptm) && (NDmax(i).*voc < VmpptM))
#         Nff=ND(i,:);
#         return
#    end
# end
    
    lNDA,cNDA = NDA.shape
    for i in np.arange(1,lNDA+1).reshape(-1):
        if ((np.multiply((np.amin(NDA(i,:))),vmp) > Vmpptm) and (np.multiply((np.amax(NDA(i,:))),voc) < VmpptM)):
            Nff = ND(i,:)
            return Nff
    
    if len(Nff)==0 == 1:
        Nff = 0
    
    return Nff