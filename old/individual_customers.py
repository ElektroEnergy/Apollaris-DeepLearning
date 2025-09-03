import numpy as np
    
def individual_customers(mod1 = None,area = None): 
    print('The demand according to Light RECON is sorted by 6 criterea: Air conditioners; Central air conditioners;')
    print('heating devices; lightning and outlets; electric motors equipments; power transformer and weld and x-ray machines')
    print('Split the total power load into these criteria and alocate the total amount into each criterea')
    options.Resize = 'On'
    
    options.WindowStyle = 'modal'
    
    options.Interpreter = 'tex'
    
    prompt = np.array(['Enter the total power of lighting and outlets (in kVA)','Enter the total power of the heating devices, shower, electric tap and heating (in kVA)','Enter the total number of the heating devices, shower, electric tap and heating','Enter the total power of the air conditioners, split and window model (in kVA)','Enter the total number of the air conditioners, split and window model','Enter the total power of central air conditioners (in kVA)','Enter the total number of central air conditioners','Enter the total power of electric motors and motor-generator weld machines (in kVA)','Enter the total number of electric motors and motor-generator weld machines','Enter the total power of electric weld machines and power transformers (in kVA)','Enter the total number of electric weld machines and power transformers','Enter the total power of x-ray, tomography, mammography and magnetic image equipments (in kVA)','Enter the total number of x-ray, tomography, mammography and magnetic image equipments'])
    dlg_title = 'Location and System Information'
    num_lines = np.array([1,100])
    defaultans = np.array(['0','0','0','0','0','0','0','0','0','0','0','0','0'])
    DadosForm = inputdlg(prompt,dlg_title,num_lines,defaultans)
    dd1 = str2double(DadosForm(1))
    dd2 = str2double(DadosForm(2))
    n2 = str2double(DadosForm(3))
    dd3 = str2double(DadosForm(4))
    n3 = str2double(DadosForm(5))
    dd4 = str2double(DadosForm(6))
    n4 = str2double(DadosForm(7))
    dd5 = str2double(DadosForm(8))
    n5 = str2double(DadosForm(9))
    dd6 = str2double(DadosForm(10))
    n6 = str2double(DadosForm(11))
    dd7 = str2double(DadosForm(12))
    n7 = str2double(DadosForm(12))
    if dd1 != 0:
        d1 = light_outlet_demand(mod1,area,dd1)
    
    f2,f3,f4,f5,f6,f7 = demand_factor(n2,n3,n4,n5,n6,n7,mod1)
    # Service factor for heating devices
    dn2 = dd2 / n2
    fs = 0
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
    demand = d1 + d2 + d3 + d4 + d5 + d6 + d7
    return demand