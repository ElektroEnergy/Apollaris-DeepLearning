import numpy as np
    
def brapv(sunS = None,brandpv = None): 
    list = np.array(['JINKO','CANADIAN','YINGLI','GLOBO BRASIL','KYOCERA'])
    bra,tf = listdlg('ListString',list)
    if bra == 1:
        list = brandpv.jinko(:,1)
    else:
        if bra == 2:
            list = brandpv.canadian(:,1)
        else:
            if bra == 3:
                list = brandpv.yingli(:,1)
            else:
                if bra == 4:
                    list = brandpv.brasilG(:,1)
                else:
                    if bra == 5:
                        list = brandpv.kyocera(:,1)
    
    pv_m,__ = listdlg('ListString',list)
    tf = str(list(pv_m)) == str(sunS(:,1))
    pv_mo,__ = find(tf == 1)
    return pv_mo