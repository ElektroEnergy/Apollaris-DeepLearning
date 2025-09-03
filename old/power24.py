import numpy as np
    
def power24(demand = None,h = None,froN = None,Fc = None): 
    # Data obtained from http://www.cresesb.cepel.br/index.php?section=sundata&#sundata
    
    #FC(:,1)=(froN(:,12)./froN(:,10)).*Fc # Evaluate considering the real efficiency
    n_inv = froN(:,21)
    
    m,n = n_inv.shape
    for i in np.arange(1,m+1).reshape(-1):
        D[i,:] = (demand) / (n_inv(i) / 100)
        P_tilt[i,:] = D(i,:) / (np.multiply(h(1,:),Fc))
        # if proj==1
        M_tilt[i,1] = sum(P_tilt(i,:)) / 12
        # end
        # if proj==2
# M_tilt(i,1)=max(P_tilt(i,:));
# end
    
    return P_tilt,M_tilt