import numpy as np
    
def optm2ttopsis(ptt = None,Nt = None,Ct = None,pit = None,Nit = None,Cit = None,froN = None,sunN = None,Npit = None,Nft = None,Npt1 = None,tt = None,NS = None,pro = None): 
    nl,csun = sunN.shape
    ll,cfro = froN.shape
    if ((len(ptt)==0 == 1) or (len(pit)==0 == 1)):
        Nt = 0
        Nit = 0
        Npit = 0
        Nft = 0
        Npt1 = 0
        tt = 0
        NFT = 0
        lt = 0
        Mt = 0
        xt = 0
        NSt = 0
        dist = 0
        dmax = 0
        TMmax = 0
        pt = np.zeros((1,csun - 5))
        pit = np.zeros((1,cfro))
        pat = np.zeros((1,69))
    else:
        # Writting a commun matrix for the PV and inverters
        l3,c3 = pit.shape
        a = 1
        b = 1
        c = 1
        for a in np.arange(1,c3+1).reshape(-1):
            for b in np.arange(1,l3+1).reshape(-1):
                if pit(b,a) != 0:
                    #pat(c,:)=[ptt(a,:) froN(pit(b,a),:) Nt(b,a) Nit(b,a) Npit(b,a) Nft(b,a) Npt1(b,a) tt(b,a)]  #each row represent one combination of pv and inverter
                    pat[c,:] = np.array([ptt(a,:),froN(pit(b,a),:),Nt(b,a),Nit(b,a),Npit(b,a),Npt1(b,a),tt(b,a),NS(b,a)])
                    Nftt[c] = Nft(b,a)
                    b = b + 1
                    c = c + 1
            a = a + 1
            c = c + 1
            b = 1
        #pat( all(~pat,2), : ) = []  #rows
        pat[pat == 0] = nan
        # Selection of TR>=5
        m1,nll = pat.shape
        a = 1
        b = 1
        patp = []
        ppb = []
        for k in np.arange(1,m1+1).reshape(-1):
            if ((pat(k,21) > 1) and (pat(k,63) > 1)):
                patp[a,:] = pat(k,:)
                Nftp[a] = Nftt(k)
                a = a + 1
            else:
                ppb[k,:] = pat(k,:)
                Nftb[b] = Nftt(k)
                b = b + 1
        if (len(patp)==0 == 1):
            patp = ppb
            if (len(ppb)==0 == 1):
                Nt = 0
                Nit = 0
                Npit = 0
                Nft = 0
                Npt1 = 0
                tt = 0
                NFT = 0
                lt = 0
                Mt = 0
                xt = 0
                NSt = 0
                dist = 0
                dmax = 0
                TMmax = 0
                pt = np.zeros((1,cs))
                pit = np.zeros((1,cc))
                pat = np.zeros((1,69))
                return Nt,Nit,pt,pit,Npit,Nft,Npt1,tt,NFT,NSt,pat,dist,dmax
        a,b,cc = topsis(patp,pro)
        # Optimum Solution (Minimum Cost C)
        pt = patp(b,np.arange(1,csun - 5+1))
        pit = patp(b,np.arange(csun + 1,cfro + csun+1))
        Nt = patp(b,cfro + csun + 1)
        Nit = patp(b,cfro + csun + 2)
        Npit = patp(b,cfro + csun + 3)
        # Nft=patp(b,cfro+csun+4);
# Npt1=patp(b,cfro+csun+5);
# tt=patp(b,cfro+csun+6);
        Npt1 = patp(b,cfro + csun + 4)
        tt = patp(b,cfro + csun + 5)
        NSt = patp(b,cfro + csun + 6)
        dist = patp(b,csun - 1)
        dmax = patp(b,csun)
        if np.isnan(tt) == 1:
            tt = 0
        NFT = Nftp(b)
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
    
    return Nt,Nit,pt,pit,Npit,Nft,Npt1,tt,NFT,NSt,pat,dist,dmax