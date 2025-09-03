import numpy as np
    
def optm4t(pt = None,Nt = None,Ct = None,pit = None,Nit = None,Cit = None,froN = None,sunN = None,Npit = None,Nft = None,Npt1 = None,tt = None,NS = None): 
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
        Niit = 0
        piit = 0
        NSt = 0
        dist = 0
        dmax = 0
        TMmax = 0
        pt = np.zeros((1,cs - 5))
        piit = np.zeros((1,cc))
        pit = np.zeros((1,cc))
    else:
        # C=Ct+Cinv
        C = Ct + Cit
        #### Sorting the inverter options
        loz,coz = sortrows(np.transpose(C))
        Niit = Nit(np.transpose(coz))
        piit = pit(coz,:)
        # Optimum Solution (Maximum performance)
        a,b = np.amin(C)
        Nt = Nt(b)
        Nit = Nit(b)
        dist = pt(1,cs - 1)
        dmax = pt(1,cs)
        pt = pt(1,np.arange(1,cs - 5+1))
        pit = pit(b,:)
        Npit = Npit(b)
        NFT = Nft(b)
        Npt1 = Npt1(b)
        tt = tt(b)
        if np.isnan(tt) == 1:
            tt = 0
        NSt = NS(b)
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
    
    return Nt,Nit,pt,pit,Npit,Nft,Npt1,tt,NFT,NSt,Niit,piit,dist,dmax