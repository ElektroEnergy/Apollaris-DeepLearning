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
Npvi = Nttt / Nitt
Nf = Nttt / NS
ND = np.zeros((6,NS))
k = 1
Npvi1 = 1
Nfa = 1
Nfb = 1
Nfd = 1
Nfg = 1
a = 1
for k in np.arange(1,Nitt+1).reshape(-1):
    if int(np.floor(Nf)) == np.ceil(Nf):
        ND[1,np.arange[1,[Nitt * [Nmpp * NoDC]]+1]] = Nf
    if int(np.floor(Npvi)) == np.ceil(Npvi):
        a = (k * Nmpp * NoDC) - ((Nmpp * NoDC) - 1)
        ND[6,a] = Npvi
    Nffy = np.ceil(Nttt / (NS - 1))
    if Nffy < (Nttt / (np.multiply(Nitt,Nmpp))):
        Nfe = Nffy
        ND[3,np.arange[1,k * Nmpp+1]] = Nfe
        Nfg = Nttt - (Nfe * Nmpp)
        ND[3,np.multiply[Nitt,[k + Nmpp]]] = Nfg
    Nffz = np.ceil(Nttt / NS)
    if (np.mod(Npvi,2) != 1 and (Nffz != Nttt / NS)):
        Nfh = Nffz
        ND[2,np.arange[1,np.multiply[Nitt,Nmpp]+1]] = Nfh
        Nfg = Nffz - 1
        ND[2,np.multiply[Nitt,[np.arange[k + Nmpp,Nmpp * NoDC+1]]]] = Nfg
    if np.ceil(Nf) > (Nf):
        Nfa = np.ceil(Npvi / Nmpp)
        ND[5,np.multiply[Nitt,k]] = Nfa
    if int(np.floor(Nf)) < (Nf):
        Nfb = int(np.floor(Npvi / Nmpp))
        ND[5,np.multiply[Nitt,[k + Nmpp]]] = Nfb
    Nffx = np.ceil(Nf)
    if Nffx > Nf:
        if k < Nmpp:
            Nfc = Nffx
            ND[4,np.arange[1,np.multiply[Nitt,Nmpp]+1]] = Nfc
        if Nfd > 0.01:
            Nfd = Nttt - (Nfc * Nmpp)
            ND[4,np.multiply[Nitt,[k + Nmpp]]] = Nfd
