import numpy as np
    
def optm4ttopsis(pt = None,Nt = None,Ct = None,pit = None,Nit = None,Cit = None,froN = None,sunN = None,Npit = None,Nft = None,Npt1 = None,tt = None,NS = None,pro = None): 
    nl,cs = sunN.shape
    ll,cc = froN.shape
    if ((len(pt)==0 == 1) or (len(pit)==0 == 1)):
        Nt = 0
        Nit = 0
        Npit = 0
        Nft = 0
        Npt1 = 0
        tt = 0
        NFT = 0
        Niito = 0
        piito = 0
        NSt = 0
        dist = 0
        dmax = 0
        TMmax = 0
        pt = np.zeros((1,cs - 5))
        piito = np.zeros((1,cc))
        pit = np.zeros((1,cc))
        piat = np.zeros((1,cc + 1))
        print('NO AVAILABLE INVERTERS FOR THE POWER DEMAND CHOSED')
    else:
        # Selection of TR>=3. At the moment considering TR>1
        m1,n1 = pit.shape
        a = 1
        piat = []
        for k in np.arange(1,m1+1).reshape(-1):
            if pit(k,33) > 1:
                piat[a,:] = pit(k,:)
                Niat[a] = Nit(k)
                Npiat[a] = Npit(k)
                Npt1a[a] = Npt1(k)
                tta[a] = tt(k)
                Nftt[a] = Nft(k)
                NSt[a] = NS(k)
                a = a + 1
            else:
                pibt[k,:] = pit(k,:)
        if (len(piat)==0 == 1):
            piat = pit
            Niat = Nit
            Npiat = Npit
            Nfta = Nft
            Npt1a = Npt1
            Nfta = Nft
            NSt = NS
            tta = tt
        piad = np.array([piat,np.transpose(Niat)])
        a,b,cc = topsis(piad,pro)
        #### Sorting the inverter options
#### Sorting the inverter options
        loz,coz = sortrows(1.0 / np.transpose(cc))
        Niito = Nit(np.transpose(coz))
        piito = pit(coz,:)
        # Optimum Solution (Minimum Cost C)
        Nt = Nt(b)
        dist = pt(1,cs - 1)
        dmax = pt(1,cs)
        pt = pt(1,np.arange(1,cs - 5+1))
        Nit = Niat(b)
        pit = piat(b,:)
        Npit = Npiat(b)
        NFT = Nftt(b)
        Npt1 = Npt1a(b)
        tt = tta(b)
        if np.isnan(tt) == 1:
            tt = 0
        NSt = NSt(b)
        # #Distribution of strings by inverter
# if (Nft==floor(Nft))==1
#     NFT=Nft;
# else
# g=0;
# h=1;
# hg=0;
# Npt=Nit.*(Npt1);
#     for i=1:Npt
#     NFt(h)=ceil((Nt-hg)/(Npt-g));
#     g=i;
#     hg=hg+NFt(h);
#     h=h+1;
#     end
#     NFT=num2str(NFt);
# end
    
    return Nt,Nit,pt,pit,Npit,Nft,Npt1,tt,NFT,NSt,Niito,piito,dist,dmax