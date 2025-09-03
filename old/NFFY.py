import numpy as np
clear('all')
# Nitt=[1; 2]
# Nttt=[11 15 20 10 19; 12 16 21 11 20]
# NoDC=[2 2 2 2 2; 2 2 2 2 2]
# Nmpp=[2 1 1 2 2; 2 1 1 2 2]

Nitt = 1
Nttt = 34
NoDC = 2
Nmpp = 2
NS = np.multiply(np.multiply(Nitt,Nmpp),NoDC)
NSS = np.multiply(Nmpp,NoDC)
Npvi = Nttt / Nitt
Nf = Nttt / NS
ND = np.zeros((6,NS))
####################### CASO 1, 2 ########################################
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
        ND[1,np.arange[c,[k * Nmpp * NoDC]+1]] = Nf
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

################# CASO 4 ##################################################
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
                ND[4,c4] = Nffv
                c4 = c4 + NoDC
        else:
            for j in np.arange(1,Nitt * Nmpp+1).reshape(-1):
                if rem(Nffv,1) <= 0.5:
                    ND[4,a4] = int(np.floor(Nffv))
                else:
                    ND[4,a4] = np.ceil(Nffv)
                int_ = ND(4,a4)
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
            ND[5,c5] = Nffu
            c5 = c5 + Nmpp * NoDC
    else:
        for j in np.arange(1,Nitt+1).reshape(-1):
            if rem(Nffu,1) <= 0.5:
                ND[5,a5] = int(np.floor(Nffu))
            else:
                ND[5,a5] = np.ceil(Nffu)
            int_ = ND(5,a5)
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
                        ND[2,a2] = int(np.floor(Nffz))
                    else:
                        ND[2,a2] = np.ceil(Nffz)
                    int_ = ND(2,a2)
                    runsum = runsum + int_
                    a2 = a2 + 1
                a2 = (NoDC * Nmpp) + i
            Nffzz = (Nttt - runsum) / (NS - Nitt * NoDC)
            if int(np.floor(Nffzz)) == np.ceil(Nffzz):
                for i in np.arange(1,Nitt+1).reshape(-1):
                    for j in np.arange(1,NoDC+1).reshape(-1):
                        ND[2,b2] = Nffzz
                        b2 = b2 + 1
                    b2 = (NoDC * Nmpp) + bb2 * i
            else:
                ND[2,:] = np.zeros((1,Nitt * Nmpp * NoDC))

ND = ND(not np.all(ND == 0,2) ,:)
NDA = ND
NDA[NDA == 0] = nan
NDmim = np.amin(NDA,[],2)
NDmax = np.transpose(np.amax(np.transpose(ND)))
Nff = ND(1,:)
A = np.random.rand(1,4)
x = cell2mat(Nff)
y = mat2cell(Nff)
A[1,3] = 'Nff'