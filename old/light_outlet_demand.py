    
def light_outlet_demand(mod1 = None,area = None,dd1 = None): 
    # Auditorios e Igrejas
    if ((mod1 == 1) or (mod1 == 6) or (mod1 == 9)):
        cm = 0.015
        fd = 0.8
        a1 = area * cm
        if a1 > dd1:
            d1 = a1
        else:
            d1 = fd * dd1
    
    # Escritórios
    if mod1 == 2:
        cm = 0.05
        fd1 = 0.8
        fd2 = 0.6
        D = 20
        a1 = area * cm
        if a1 > dd1:
            if a1 > D:
                c = a1 - D
                d1 = fd1 * D + fd2 * c
            else:
                d1 = fd1 * a1
        else:
            if dd1 > D:
                c = dd1 - D
                d1 = fd1 * D + fd2 * c
            else:
                d1 = fd1 * dd1
    
    # Barbearia, cluble, lojas, restaurante e bares
    if ((mod1 == 3) or (mod1 == 4) or (mod1 == 10) or (mod1 == 13) or (mod1 == 15)):
        cm = 0.02
        fd = 0.8
        a1 = area * cm
        if a1 > dd1:
            d1 = a1
        else:
            d1 = fd * dd1
    
    # Escolas
    if mod1 == 5:
        cm = 0.03
        fd1 = 0.8
        fd2 = 0.5
        D = 12
        a1 = area * cm
        if a1 > dd1:
            if a1 > D:
                c = a1 - D
                d1 = fd1 * D + fd2 * c
            else:
                d1 = fd1 * a1
        else:
            if dd1 > D:
                c = dd1 - D
                d1 = fd1 * D + fd2 * c
            else:
                d1 = fd1 * dd1
    
    # Hospitais
    if mod1 == 7:
        cm = 0.02
        fd1 = 0.4
        fd2 = 0.2
        D = 50
        a1 = area * cm
        if a1 > dd1:
            if a1 > D:
                c = a1 - D
                d1 = fd1 * D + fd2 * c
            else:
                d1 = fd1 * a1
        else:
            if dd1 > D:
                c = dd1 - D
                d1 = fd1 * D + fd2 * c
            else:
                d1 = fd1 * dd1
    
    # Hoteis
    if mod1 == 8:
        cm = 0.02
        fd1 = 0.5
        fd2 = 0.4
        fd3 = 0.3
        D = 20
        D1 = 100
        a1 = area * cm
        if a1 > dd1:
            if a1 > D:
                c = a1 - D
                if c > (D1 - D):
                    d1 = fd1 * D + fd2 * (D1 - D) + fd3 * (a1 - D1)
                else:
                    d1 = fd1 * D + fd2 * c
            else:
                d1 = fd1 * a1
        else:
            if dd1 > D:
                c = dd1 - D
                if c > (D1 - D):
                    d1 = fd1 * D + fd2 * (D1 - D) + fd3 * (dd1 - D1)
                else:
                    d1 = fd1 * D + fd2 * c
            else:
                d1 = fd1 * dd1
    
    # Bancos
    if mod1 == 14:
        cm = 0.05
        fd = 0.8
        a1 = area * cm
        if a1 > dd1:
            d1 = a1
        else:
            d1 = fd * dd1
    
    # Residencias e Apartamentos
    if ((mod1 == 11) or (mod1 == 12)):
        cm = 0.03
        fd1 = 0.8
        fd2 = 0.75
        fd3 = 0.65
        fd4 = 0.6
        fd5 = 0.5
        fd6 = 0.45
        fd7 = 0.4
        fd8 = 0.35
        fd9 = 0.3
        fd10 = 0.27
        fd11 = 0.24
        D = 1
        a1 = area * cm
        if a1 > dd1:
            if a1 > D:
                c2 = dd1 - 1
                if c2 > D:
                    c3 = c2 - D
                    if c3 > D:
                        c4 = c3 - D
                        if c4 > D:
                            c5 = c4 - D
                            if c5 > D:
                                c6 = c5 - D
                                if c6 > D:
                                    c7 = c6 - D
                                    if c7 > D:
                                        c8 = c7 - D
                                        if c8 > D:
                                            c9 = c8 - D
                                            if c9 > D:
                                                c10 = c9 - D
                                                if c10 > D:
                                                    c11 = c10 - D
                                                    d1 = fd1 + fd2 + fd3 + fd4 + fd5 + fd6 + fd7 + fd8 + fd9 + fd10 + fd11 * c11
                                                else:
                                                    d1 = fd1 + fd2 + fd3 + fd4 + fd5 + fd6 + fd7 + fd8 + fd9 + f10 * c10
                                            else:
                                                d1 = fd1 + fd2 + fd3 + fd4 + fd5 + fd6 + fd7 + fd8 + fd9 * c9
                                        else:
                                            d1 = fd1 + fd2 + fd3 + fd4 + fd5 + fd6 + fd7 + fd8 * c8
                                    else:
                                        d1 = fd1 + fd2 + fd3 + fd4 + fd5 + fd6 + fd7 * c7
                                else:
                                    d1 = fd1 + fd2 + fd3 + fd4 + fd5 + fd6 * c6
                            else:
                                d1 = fd1 + fd2 + fd3 + fd4 + fd5 * c5
                        else:
                            d1 = fd1 + fd2 + fd3 + fd4 * c4
                    else:
                        d1 = fd1 + fd2 + fd3 * c3
                else:
                    d1 = fd1 + fd2 * c2
            else:
                d1 = fd1 * dd1
        else:
            if dd1 > D:
                c2 = dd1 - 1
                if c2 > D:
                    c3 = c2 - D
                    if c3 > D:
                        c4 = c3 - D
                        if c4 > D:
                            c5 = c4 - D
                            if c5 > D:
                                c6 = c5 - D
                                if c6 > D:
                                    c7 = c6 - D
                                    if c7 > D:
                                        c8 = c7 - D
                                        if c8 > D:
                                            c9 = c8 - D
                                            if c9 > D:
                                                c10 = c9 - D
                                                if c10 > D:
                                                    c11 = c10 - D
                                                    d1 = fd1 + fd2 + fd3 + fd4 + fd5 + fd6 + fd7 + fd8 + fd9 + fd10 + fd11 * c11
                                                else:
                                                    d1 = fd1 + fd2 + fd3 + fd4 + fd5 + fd6 + fd7 + fd8 + fd9 + f10 * c10
                                            else:
                                                d1 = fd1 + fd2 + fd3 + fd4 + fd5 + fd6 + fd7 + fd8 + fd9 * c9
                                        else:
                                            d1 = fd1 + fd2 + fd3 + fd4 + fd5 + fd6 + fd7 + fd8 * c8
                                    else:
                                        d1 = fd1 + fd2 + fd3 + fd4 + fd5 + fd6 + fd7 * c7
                                else:
                                    d1 = fd1 + fd2 + fd3 + fd4 + fd5 + fd6 * c6
                            else:
                                d1 = fd1 + fd2 + fd3 + fd4 + fd5 * c5
                        else:
                            d1 = fd1 + fd2 + fd3 + fd4 * c4
                    else:
                        d1 = fd1 + fd2 + fd3 * c3
                else:
                    d1 = fd1 + fd2 * c2
            else:
                d1 = fd1 * dd1
    
    # Garagen residencial
    if mod1 == 16:
        cm = 0.005
        fd1 = 0.8
        fd2 = 0.25
        D = 10
        a1 = area * cm
        if a1 > dd1:
            if a1 > D:
                c = a1 - D
                d1 = fd1 * D + fd2 * c
            else:
                d1 = fd1 * a1
        else:
            if dd1 > D:
                c = dd1 - D
                d1 = fd1 * D + fd2 * c
            else:
                d1 = fd1 * dd1
    
    # Garagen não residencial
    if mod1 == 17:
        cm = 0.005
        fd1 = 0.8
        fd2 = 0.6
        fd3 = 0.4
        D = 30
        D1 = 100
        a1 = area * cm
        if a1 > dd1:
            if a1 > D:
                c = a1 - D
                if c > (D1 - D):
                    d1 = fd1 * D + fd2 * (D1 - D) + fd3 * (a1 - D1)
                else:
                    d1 = fd1 * D + fd2 * c
            else:
                d1 = fd1 * a1
        else:
            if dd1 > D:
                c = dd1 - D
                if c > (D1 - D):
                    d1 = fd1 * D + fd2 * (D1 - D) + fd3 * (dd1 - D1)
                else:
                    d1 = fd1 * D + fd2 * c
            else:
                d1 = fd1 * dd1
    
    return d1