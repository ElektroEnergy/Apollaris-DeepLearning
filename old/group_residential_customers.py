import numpy as np
    
def group_residential_customers(mod1 = None,area = None): 
    mod3 = input_('Enter the total number of units \n')
    if mod3 > 300:
        print('THE LIGHT CRITEREA CONSIDER MAXIMMUM 300 UNITS. CHOOSE LESS UNITS')
        demand = 0
        return demand
    
    print('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
    print('The demand for one residential unit according to Light RECON is sorted by 6 criterea: Air conditioners; Central air conditioners;')
    print('heating devices; lightning and outlets; electric motors equipments; power transformer and weld and x-ray machines')
    print('Split the total power load into these criteria and alocate the total amount into each criterea')
    print('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
    dd1 = input_('Enter the total power of lighting and outlets (in kVA) for one residential unit. If no device enter "0" \n')
    dd2 = input_('Enter the total power of the heating devices, shower, electric tap and heating (in kVA) for one residential unit. If no device enter "0" \n')
    n2 = input_('Enter the total number of the heating devices, shower, electric tap and heating for one residential unit. If no device enter "0" \n')
    dd3 = input_('Enter the total power of the air conditioners, split and window model (in kVA) for one residential unit. If no device enter "0" \n')
    n3 = input_('Enter the total number of the air conditioners, split and window model for one residential unit. If no device enter "0" \n')
    dd4 = input_('Enter the total power of central air conditioners (in kVA) for one residential unit. If no device enter "0" \n')
    n4 = input_('Enter the total number of central air conditioners for one residential unit. If no device enter "0" \n')
    dd5 = input_('Enter the total power of electric motors and motor-generator weld machines (in kVA) for one residential unit. If no device enter "0" \n')
    n5 = input_('Enter the total number of electric motors and motor-generator weld machines for one residential unit. If no device enter "0" \n')
    dd6 = input_('Enter the total power of electric weld machines and power transformers (in kVA) for one residential unit. If no device enter "0" \n')
    n6 = input_('Enter the total number of electric weld machines and power transformers for one residential unit. If no device enter "0" \n')
    dd7 = input_('Enter the total power of x-ray, tomography, mammography and magnetic image equipments (in kVA). If no device enter "0" \n')
    n7 = input_('Enter the total number of x-ray, tomography, mammography and magnetic image equipments. If no device enter "0" \n')
    print('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
    print('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
    ddd1 = input_('Enter the total power of lighting and outlets (in kVA) for service area. If no device enter "0" \n')
    ddd2 = input_('Enter the total power of the heating devices, shower, electric tap and heating (in kVA) for service area. If no device enter "0" \n')
    nn2 = input_('Enter the total number of the heating devices, shower, electric tap and heating for service area. If no device enter "0" \n')
    ddd3 = input_('Enter the total power of the air conditioners, split and window model (in kVA) for service area. If no device enter "0" \n')
    nn3 = input_('Enter the total number of the air conditioners, split and window model for service area. If no device enter "0" \n')
    ddd4 = input_('Enter the total power of central air conditioners (in kVA) for service area. If no device enter "0" \n')
    nn4 = input_('Enter the total number of central air conditioners for service area. If no device enter "0" \n')
    ddd5 = input_('Enter the total power of electric motors and motor-generator weld machines (in kVA) for service area. If no device enter "0" \n')
    nn5 = input_('Enter the total number of electric motors and motor-generator weld machines for service area. If no device enter "0" \n')
    ddd6 = input_('Enter the total power of electric weld machines and power transformers (in kVA) for service area. If no device enter "0" \n')
    nn6 = input_('Enter the total number of electric weld machines and power transformers for service area. If no device enter "0" \n')
    ddd7 = input_('Enter the total power of x-ray, tomography, mammography and magnetic image equipments (in kVA). If no device enter "0" \n')
    nn7 = input_('Enter the total number of x-ray, tomography, mammography and magnetic image equipments. If no device enter "0" \n')
    print('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
    fi1 = np.array([1,2,3,4,4.84,5.8,6.76,7.72,8.68,9.64,10.42,11.2,11.98,12.76,13.54,14.32,15.1,15.88,16.66,17.44,18.05,18.66,19.27,19.88,20.49])
    fi2 = np.array([21.1,21.71,22.32,22.93,23.54,24.14,24.74,25.34,25.94,26.54,27.14,27.74,28.34,28.94,29.54,30.14,30.74,31.34,31.94,32.54,33.1,33.66,34.22,34.78,35.34])
    fi3 = np.array([35.9,36.46,37.02,37.58,38.14,38.7,39.26,39.82,40.38,40.94,41.5,42.06,42.62,43.18,43.74,44.3,44.86,45.42,45.98,46.54,47.1,47.66,48.22,48.78,49.34,49.9])
    fi4 = np.array([50.46,51.02,51.58,52.14,52.7,53.26,53.82,54.38,54.94,55.5,56.06,56.62,57.18,57.74,58.3,58.86,59.42,59.98,60.54,61.1,61.66,62.22,62.78,63.34,63.59])
    fi5 = np.array([63.84,64.09,64.34,64.59,64.84,65.09,65.34,65.59,65.84,66.09,66.34,66.59,66.84,67.09,67.34,67.59,67.84,68.09,68.34,68.59,68.84,69.09,69.34,69.59,69.79])
    fi6 = np.array([69.99,70.19,70.39,70.59,70.79,70.99,71.19,71.39,71.59,71.79,71.99,72.19,72.39,72.59,72.79,72.99,73.19,73.39,73.59,73.79,73.99,74.19,74.39,74.59,74.74])
    fi7 = np.array([74.89,75.04,75.19,75.34,75.49,75.64,75.79,75.94,76.09,76.24,76.39,76.54,76.69,76.84,76.99,77.14,77.29,77.44,77.59,77.74,77.89,78.04,78.19,78.34,78.44,78.54])
    fi8 = np.array([78.65,78.74,78.84,78.94,79.04,79.14,79.24,79.34,79.44,79.54,79.64,79.74,79.84,79.94,80.04,80.14,80.24,80.34,80.44,80.5,80.64,80.74,80.84,80.89,80.94])
    fi8a = np.array([80.99,81.04,81.09,81.14,81.19,81.24,81.29,81.34,81.39,81.44,81.49,81.54,81.59,81.64,81.69,81.74,81.79,81.84,81.89,81.94,81.99,82.04,82.09,82.12,82.15])
    fi9 = np.array([82.18,82.21,82.24,82.27,82.3,82.33,82.36,82.39,82.42,82.45,82.48,82.5,82.52,82.54,82.56,82.58,82.6,82.62,82.64,82.66,82.68,82.7,82.72,82.73,82.74])
    fi10 = np.array([82.75,82.76,82.77,82.78,82.79,82.8,82.81,82.82,82.83,82.84,82.85,82.86,82.87,82.88,82.89,82.9,82.91,82.92,82.93,82.94,82.95,82.96,82.97,82.98,82.99])
    fi11 = np.array([83.0,83.0,83.0,83.0,83.0,83.0,83.0,83.0,83.0,83.0,83.0,83.0,83.0,83.0,83.0,83.0,83.0,83.0,83.0,83.0,83.0,83.0,83.0])
    fdiv = np.array([fi1,fi2,fi3,fi4,fi5,fi5,fi7,fi8,fi8a,fi9,fi10,fi11])
    FDIV = fdiv(mod3)
    # Demand for one residential unit
    d1 = light_outlet_demand(mod1,area,dd1)
    f2,f3,f4,f5,f6,f7 = demand_factor(n2,n3,n4,n5,n6,n7,mod1)
    # Service factor for heating devices
    dn2 = dd2 / n2
    if dn2 < 4.4:
        fs = 1
    else:
        if ((dn2 > 4.4) and (dn2 <= 6)):
            fs = 1.1
        else:
            if dn2 > 6:
                fs = 1.2
    
    d2 = dd2 * f2 * fs
    d3 = dd3 * f3
    d4 = dd4 * f4
    d5 = dd5 * f5
    d6 = dd6 * f6
    d7 = dd7 * f7
    Dru = FDIV * (d1 + d2 + d3 + d4 + d5 + d6 + d7)
    # Demand for the service area
    ds1 = light_outlet_demand(mod1,area,ddd1)
    fs2,fs3,fs4,fs5,fs6,fs7 = demand_factor(nn2,nn3,nn4,nn5,nn6,nn7,mod1)
    # Service factor for heating devices
    dns2 = ddd2 / nn2
    if dns2 < 4.4:
        fss = 1
    else:
        if ((dns2 > 4.4) and (dns2 <= 6)):
            fss = 1.1
        else:
            if dns2 > 6:
                fss = 1.2
    
    ds2 = ddd2 * fs2 * fss
    ds3 = ddd3 * fs3
    ds4 = ddd4 * fs4
    ds5 = ddd5 * fs5
    ds6 = ddd6 * fs6
    ds7 = ddd7 * fs7
    Ds = ds1 + ds2 + ds3 + ds4 + ds5 + ds6
    demand = (Dru + Ds) * 0.9
    return demand