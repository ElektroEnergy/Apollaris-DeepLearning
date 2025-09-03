import numpy as np
    
def optm4ta(pt = None,Nt = None,Ct = None,pit = None,Nit = None,Cit = None,froN = None,sunN = None,Npit = None,Nft = None,Npt1 = None,tt = None,NS = None): 
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
        lt = 0
        Ct = 0
        Niita = 0
        piita = 0
        NSt = 0
        dist = 0
        dmax = 0
        TMmax = 0
        pt = np.zeros((1,cs - 5))
        piita = np.zeros((1,cc))
        pit = np.zeros((1,cc))
        pat = np.zeros((1,71))
    else:
        # Selection of TR>=5
# Writting a commun matrix for the PV and inverters
        l3,c3 = pit.shape
        ptt = np.multiply(np.ones((l3,1)),pt(1,:))
        pat = np.array([ptt,pit,np.transpose(Nt),np.transpose(Nit),np.transpose(Npit),np.transpose(Npt1),np.transpose(tt),np.transpose(NS),np.transpose(Ct),np.transpose(Cit)])
        Nftt = np.transpose(Nft)
        #pat( all(~pat,2), : ) = [];#rows
        pat[pat == 0] = nan
        # Selection of TR>=3
        m1,nll = pat.shape
        a = 1
        patp = []
        for k in np.arange(1,m1+1).reshape(-1):
            if pat(k,63) >= 3:
                patp[a,:] = pat(k,:)
                Nftp[a] = Nftt(k)
                a = a + 1
            else:
                ppb[k,:] = pat(k,:)
                Nftb[a] = Nftt(k)
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
                Ct = 0
                Niita = 0
                piita = 0
                NSt = 0
                dist = 0
                dmax = 0
                TMmax = 0
                pt = np.zeros((1,cs))
                piita = np.zeros((1,cc))
                pit = np.zeros((1,cc))
                pat = np.zeros((1,71))
        # C=Ct+Cinv
        Ct = patp(:,(nll - 1)) + patp(:,nll)
        # MEAN
        Mt = mean(nanmean(Ct))
        a,index = np.amin(np.abs(Ct - Mt))
        b,col = np.amin(a)
        row = index(1,col)
        #### Sorting the inverter options
        lct,cct = Ct.shape
        if lct > 2:
            for i in np.arange(1,lct+1).reshape(-1):
                DMt[i] = np.abs(Ct(i) - Mt)
            loz,coz = sortrows(np.transpose(DMt))
            Niita = patp(np.transpose(coz),cs + cc + 2)
            piita = patp(coz,np.arange(cs + 1,cs + cc+1))
        else:
            loz,coz = sortrows(Ct)
            Niita = patp(np.transpose(coz),cs + cc + 2)
            piita = patp(coz,np.arange(cs + 1,cs + cc+1))
        # Optimum Solution
        dist = patp(row,cs - 1)
        dmax = patp(row,cs)
        pt = patp(row,np.arange(1,cs - 5+1))
        pit = patp(row,np.arange(cs + 1,cs + cc+1))
        Nt = patp(row,cs + cc + 1)
        Nit = patp(row,cs + cc + 2)
        Npit = patp(row,cs + cc + 3)
        NFT = Nftp(row)
        Npt1 = patp(row,cs + cc + 4)
        tt = patp(row,cs + cc + 5)
        if np.isnan(tt) == 1:
            tt = 0
        NSt = patp(row,cs + cc + 6)
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
    
    return Nt,Nit,pt,pit,Npit,Nft,Npt1,tt,NFT,NSt,Ct,Niita,piita,dist,dmax