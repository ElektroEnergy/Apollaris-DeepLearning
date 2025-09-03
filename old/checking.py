    
def checking(Nt = None,Nto = None,Ntc = None,Nta = None,NFT = None,NFTa = None,NFTo = None,NFTc = None): 
    if Nt <= 0.5:
        nft = 0
    else:
        nft = num2str(NFT[0])
    
    if Nta <= 0.5:
        nfta = 0
    else:
        nfta = num2str(NFTa[0])
    
    if Nto <= 0.5:
        nfto = 0
    else:
        nfto = num2str(NFTo[0])
    
    if Ntc <= 0.5:
        nftc = 0
    else:
        nftc = num2str(NFTc[0])
    
    return nft,nfta,nftc,nfto