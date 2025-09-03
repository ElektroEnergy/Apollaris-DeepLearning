import numpy as np
    
def demand_factor(n2 = None,n3 = None,n4 = None,n5 = None,n6 = None,n7 = None,mod1 = None): 
    fd2 = np.array([1,0.75,0.7,0.66,0.62,0.59,0.56,0.53,0.51,0.49,0.47,0.45,0.43,0.41,0.4,0.39,0.38,0.37,0.36,0.35,0.34,0.33,0.32,0.31,0.3])
    fd3a = np.array([1,0.7,0.6,0.55,0.53,0.52,0.5])
    fd3b = np.array([1,0.75,0.7,0.65,0.6,0.55,0.5])
    fd4 = np.array([1,0.75,0.7,0.65,0.6,0.55,0.5])
    fd5 = np.array([1,0.75,0.6333,0.575,0.54,0.5,0.4714,0.45,0.4333,0.42])
    fd6 = np.array([1,0.7,0.6,0.5])
    fd7 = np.array([1,0.6,0.5,0.4])
    if n2 == 0:
        f2 = 0
    else:
        if n2 <= 25:
            f2 = fd2(n2)
        else:
            f2 = fd2(25)
    
    if n3 == 0:
        f3 = 0
    else:
        if ((mod1 == 11) or (mod1 == 12) or (mod1 == 16)):
            if n3 <= 4:
                f3 = fd3a(1)
            else:
                if ((n3 >= 5) and (n3 <= 10)):
                    f3 = fd3a(2)
                else:
                    if ((n3 >= 11) and (n3 <= 20)):
                        f3 = fd3a(3)
                    else:
                        if ((n3 >= 21) and (n3 <= 30)):
                            f3 = fd3a(4)
                        else:
                            if ((n3 >= 31) and (n3 <= 40)):
                                f3 = fd3a(5)
                            else:
                                if ((n3 >= 41) and (n3 <= 50)):
                                    f3 = fd3a(6)
                                else:
                                    if n3 > 50:
                                        f3 = fd3a(7)
        else:
            if n3 <= 10:
                f3 = fd3b(1)
            else:
                if ((n3 >= 11) and (n3 <= 20)):
                    f3 = fd3b(2)
                else:
                    if ((n3 >= 21) and (n3 <= 30)):
                        f3 = fd3b(3)
                    else:
                        if ((n3 >= 31) and (n3 <= 40)):
                            f3 = fd3b(4)
                        else:
                            if ((n3 >= 41) and (n3 <= 50)):
                                f3 = fd3b(5)
                            else:
                                if ((n3 >= 51) and (n3 <= 80)):
                                    f3 = fd3b(6)
                                else:
                                    if n3 > 80:
                                        f3 = fd3b(7)
    
    if n4 == 0:
        f4 = 0
    else:
        if n4 <= 10:
            f4 = fd4(1)
        else:
            if ((n4 >= 11) and (n4 <= 20)):
                f4 = fd4(2)
            else:
                if ((n4 >= 21) and (n4 <= 30)):
                    f4 = fd4(3)
                else:
                    if ((n4 >= 31) and (n4 <= 40)):
                        f4 = fd4(4)
                    else:
                        if ((n4 >= 41) and (n4 <= 50)):
                            f4 = fd4(5)
                        else:
                            if ((n4 >= 51) and (n5 <= 80)):
                                f4 = fd4(6)
                            else:
                                if n4 > 80:
                                    f4 = fd4(7)
    
    if n5 == 0:
        f5 = 0
    else:
        if n5 <= 10:
            f5 = fd5(n5)
        else:
            f5 = fd5(10)
    
    if n6 == 0:
        f6 = 0
    else:
        if n6 == 1:
            f6 = fd6(1)
        else:
            if ((n6 >= 2) and (n4 <= 3)):
                f6 = fd6(2)
            else:
                if ((n6 >= 4) and (n6 <= 7)):
                    f6 = fd6(3)
                else:
                    if n6 > 7:
                        f6 = fd6(4)
    
    if n7 == 0:
        f7 = 0
    else:
        if n7 == 1:
            f7 = fd7(1)
        else:
            if ((n7 >= 2) and (n7 <= 5)):
                f7 = fd7(2)
            else:
                if ((n7 >= 6) and (n7 <= 10)):
                    f7 = fd7(3)
                else:
                    if n7 > 10:
                        f7 = fd7(4)
    
    return f2,f3,f4,f5,f6,f7