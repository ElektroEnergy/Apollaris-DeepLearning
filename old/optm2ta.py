import numpy as np
    
def optm2ta(ptt = None,Nt = None,Ct = None,pit = None,Nit = None,Cit = None,froN = None,sunN = None,Npit = None,Nft = None,Npt1 = None,tt = None,NS = None): 
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
        # Writting a commun matrix for the PV and inverters
        l3,c3 = pit.shape
        a = 1
        b = 1
        c = 1
        for a in np.arange(1,c3+1).reshape(-1):
            for b in np.arange(1,l3+1).reshape(-1):
                if pit(b,a) != 0:
                    #pat(c,:)=[ptt(a,:) froN(pit(b,a),:) Nt(b,a) Nit(b,a) Npit(b,a) Nft(b,a) Npt1(b,a) tt(b,a) Ctt(b,a) Citt(b,a)];    #each row represent one combination of pv and inverter
                    pat[c,:] = np.array([ptt(a,:),froN(pit(b,a),:),Nt(b,a),Nit(b,a),Npit(b,a),Npt1(b,a),tt(b,a),NS(b,a),Ctt(b,a),Citt(b,a)])
                    Nftt[c] = Nft(b,a)
                    b = b + 1
                    c = c + 1
            a = a + 1
            c = c + 1
            b = 1
        #pat( all(~pat,2), : ) = [];#rows
        pat[pat == 0] = nan
        # Selection of TR>=3
        m1,nll = pat.shape
        a = 1
        b = 1
        patp = []
        ppb = []
        #Nftp=[];
        for k in np.arange(1,m1+1).reshape(-1):
            if ((pat(k,21) >= 3) and (pat(k,63) >= 3)):
                patp[a,:] = pat(k,:)
                Nftp[a] = Nftt(1,k)
                a = a + 1
            else:
                ppb[k,:] = pat(k,:)
                Nftb[b] = Nftt(1,k)
                b = b + 1
        if (len(patp)==0 == 1):
            patp = ppb
            Nftp = Nftb
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
                pat = np.zeros((1,71))
                return Nt,Nit,pt,pit,Npit,Nft,Npt1,tt,NFT,NSt,pat,Mt,lt,xt,dist,dmax
        # C=Ct+Cinv
        Ct = patp(:,(nll - 1)) + patp(:,nll)
        #MEAN
        Mt = mean(nanmean(Ct))
        a,index = np.amin(np.abs(Ct - Mt))
        b,col = np.amin(a)
        row = index(1,col)
        # # MIN
# [Mt,row]=max(Ct);
        xt = patp(row,:)
        #[lt,cp]=find((xt(:,55)+xt(:,56)+xt(:,3)+xt(:,4))==(pat(:,55)+pat(:,56)+pat(:,3)+pat(:,4)));
#[lt,cp]=find(pat(:,1)==pat(row,1));
        lt,cp = find((pat(:,(nll - 1)) + pat(:,nll)) == Mt)
        # Optimum Solution
        pt = patp(row,np.arange(1,cs - 5+1))
        pit = patp(row,np.arange(cs + 1,cs + cc+1))
        Nt = patp(row,cs + cc + 1)
        Nit = patp(row,cs + cc + 2)
        Npit = patp(row,cs + cc + 3)
        # Nft=patp(row,cs+cc+4);
# Npt1=patp(row,cs+cc+5);
# tt=patp(row,cs+cc+6);
        NFT = Nftp(row)
        Npt1 = patp(row,cs + cc + 4)
        tt = patp(row,cs + cc + 5)
        NSt = patp(row,cs + cc + 6)
        if np.isnan(tt) == 1:
            tt = 0
        dist = patp(row,cs - 1)
        dmax = patp(row,cs)
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
    
    return Nt,Nit,pt,pit,Npit,Nft,Npt1,tt,NFT,NSt,pat,Mt,lt,xt,dist,dmax