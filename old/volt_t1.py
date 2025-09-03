import numpy as np
    
def volt_t1(pos_t = None,vfn = None,nf = None,Ntt_t = None): 
    # Viable Inverters for the distribution system, voltage and number of
# phases
    n = 1
    lv,cv = pos_t.shape
    for i in np.arange(1,lv+1).reshape(-1):
        if ((pos_t(i,28) == nf) and (vfn == 127) and (nf == 1)):
            pos_v[n,:] = pos_t(i,:)
            Ntt_v[n,:] = Ntt_t(i,:)
            ttt[n,1] = 1
            ft = 1 / 8
            n = n + 1
        else:
            if ((pos_t(i,28) == nf) and (vfn == 220) and (nf == 1)):
                pos_v[n,:] = pos_t(i,:)
                Ntt_v[n,:] = Ntt_t(i,:)
                ttt[n,1] = 0
                ft = 1 / 8
                n = n + 1
            else:
                if ((pos_t(i,28) == nf) and (vfn != 220) and (vfn != 127) and (nf == 1)):
                    pos_v[n,:] = pos_t(i,:)
                    Ntt_v[n,:] = Ntt_t(i,:)
                    ttt[n,1] = 1
                    ft = 1 / 8
                    n = n + 1
                else:
                    if ((nf == 2) and (vfn == 127) and (pos_t(i,28) == 1)):
                        pos_v[n,:] = pos_t(i,:)
                        Ntt_v[n,:] = Ntt_t(i,:)
                        ttt[n,1] = 1
                        ft = 1 / 8
                        n = n + 1
                    else:
                        if ((nf == 2) and (vfn == 220) and (pos_t(i,28) == 1)):
                            pos_v[n,:] = pos_t(i,:)
                            Ntt_v[n,:] = Ntt_t(i,:)
                            ttt[n,1] = 0
                            ft = 1 / 8
                            n = n + 1
                        else:
                            if ((nf == 3) and (vfn == 127) and (pos_t(i,14) <= 220) and (pos_t(i,15) >= 220)):
                                pos_v[n,:] = pos_t(i,:)
                                Ntt_v[n,:] = Ntt_t(i,:)
                                ttt[n,1] = 0
                                ft = 1 / 7
                                n = n + 1
                            else:
                                if ((nf == 3) and (vfn == 220) and (pos_t(i,14) <= 380) and (pos_t(i,15) >= 380)):
                                    pos_v[n,:] = pos_t(i,:)
                                    Ntt_v[n,:] = Ntt_t(i,:)
                                    ttt[n,1] = 0
                                    ft = 1 / 8
                                    n = n + 1
                                else:
                                    if ((nf == 3) and (vfn == 220) and (pos_t(i,16) == 1) and (pos_t(i,14) <= 220) and (pos_t(i,15) >= 220)):
                                        pos_v[n,:] = pos_t(i,:)
                                        Ntt_v[n,:] = Ntt_t(i,:)
                                        ttt[n,1] = 0
                                        ft = 1 / 8
                                        n = n + 1
                                    else:
                                        if ((nf == 3) and (vfn != 220) and (vfn != 127)):
                                            pos_v[n,:] = pos_t(i,:)
                                            Ntt_v[n,:] = Ntt_t(i,:)
                                            ttt[n,1] = 1
                                            ft = 3
                                            n = n + 1
    
    ############################################################################
    return pos_v,ttt,ft,Ntt_v