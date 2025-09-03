import numpy as np
    
def optm2tc(ptt = None,Nt = None,Ct = None,pit = None,Nit = None,Cit = None,froN = None,sunN = None,Npit = None,Nft = None,Npt1 = None,tt = None,NS = None): 
    nl,cs = sunN.shape
    ll,cc = froN.shape
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
        pt = np.zeros((1,cs - 5))
        pit = np.zeros((1,cc))
        pat = np.zeros((1,71))
    else:
        li,ci = pit.shape
        for i in np.arange(1,li+1).reshape(-1):
            for j in np.arange(1,ci+1).reshape(-1):
                if Ct(i,j) == 0:
                    Ctt[i,j] = NaN
                else:
                    Ctt[i,j] = Ct(i,j)
                if Cit(i,j) == 0:
                    Citt[i,j] = NaN
                else:
                    Citt[i,j] = Cit(i,j)
        #C=Ct+Cinv
        C = 1.0 / (Ctt + Citt)
        # Writting a commun matrix for the PV and inverters
        l3,c3 = pit.shape
        a = 1
        b = 1
        c = 1
        for a in np.arange(1,c3+1).reshape(-1):
            for b in np.arange(1,l3+1).reshape(-1):
                if pit(b,a) != 0:
                    #pat(c,:)=[ptt(a,:) froN(pit(b,a),:) Nt(b,a) Nit(b,a) Npit(b,a) Nft(b,a) Npt1(b,a) tt(b,a) Ctt(b,a) Citt(b,a)];
                    pat[c,:] = np.array([ptt(a,:),froN(pit(b,a),:),Nt(b,a),Nit(b,a),Npit(b,a),Npt1(b,a),tt(b,a),NS(b,a),Ctt(b,a),Citt(b,a)])
                    Nftt[c] = Nft(b,a)
                    b = b + 1
                    c = c + 1
            a = a + 1
            c = c + 1
            b = 1
        # Optimum Solution (Minimum Cost C)
        if li == 1:
            a,copt = np.amin(C)
            pt = ptt(copt,np.arange(1,cs - 5+1))
            dist = ptt(copt,cs - 1)
            dmax = ptt(copt,cs)
            dist = ptt(copt,cs - 1)
            dmax = ptt(copt,cs)
            pit = froN(pit(1,copt),:)
            Nt = Nt(1,copt)
            Nit = Nit(1,copt)
            Npit = Npit(1,copt)
            #Nft=Nft(1,copt);
            NFT = Nft(1,copt)
            Npt1 = Npt1(1,copt)
            tt = tt(1,copt)
            NSt = NS(1,copt)
        else:
            if ci == 1:
                a,copt = np.amin(C)
                pt = ptt(1,np.arange(1,cs - 5+1))
                dist = ptt(1,cs - 1)
                dmax = ptt(1,cs)
                pit = froN(pit(copt,1),:)
                Nt = Nt(copt,1)
                Nit = Nit(copt,1)
                Npit = Npit(copt,1)
                #Nft=Nft(copt,1);
                NFT = Nft(copt,1)
                Npt1 = Npt1(copt,1)
                tt = tt(copt,1)
                NSt = NS(copt,1)
            else:
                a,b = np.amin(C)
                c,copt = np.amin(a)
                lopt = b(copt)
                pt = ptt(copt,np.arange(1,cs - 5+1))
                dist = ptt(copt,cs - 1)
                dmax = ptt(copt,cs)
                pit = froN(pit(lopt,copt),:)
                Nt = Nt(lopt,copt)
                Nit = Nit(lopt,copt)
                Npit = Npit(lopt,copt)
                NFT = Nft(lopt,copt)
                Npt1 = Npt1(lopt,copt)
                tt = tt(lopt,copt)
                if np.isnan(tt) == 1:
                    tt = 0
                NSt = NS(lopt,copt)
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