import numpy as np
    
def consumption(sel = None,area = None): 
    # clc
# clear all
# sel=3;
# #area=400;
# area=60;
    
    #Prepared by Gustavo K. Dill - 26/07/2017
    
    if sel == 1:
        options.Resize = 'On'
        options.WindowStyle = 'modal'
        options.Interpreter = 'tex'
        prompt = np.array(['Enter the average consumption of eletricity in January (in kWh) \n','Enter the average consumption of eletricity in February (in kWh) \n','Enter the average consumption of eletricity in March (in kWh) \n','Enter the average consumption of eletricity in April (in kWh) \n','Enter the average consumption of eletricity in May (in kWh) \n','Enter the average consumption of eletricity in June (in kWh) \n','Enter the average consumption of eletricity in July (in kWh) \n','Enter the average consumption of eletricity in August (in kWh) \n','Enter the average consumption of eletricity in September (in kWh) \n','Enter the average consumption of eletricity in October (in kWh) \n','Enter the average consumption of eletricity in November (in kWh) \n','Enter the average consumption of eletricity in December (in kWh) \n'])
        dlg_title = 'Average eletricity consumption per month'
        num_lines = np.array([1,100])
        defaultans = np.array(['300','300','300','300','300','300','300','300','300','300','300','300'])
        DadosForm = inputdlg(prompt,dlg_title,num_lines,defaultans)
        january = str2double(DadosForm(1))
        february = str2double(DadosForm(2))
        march = str2double(DadosForm(3))
        april = str2double(DadosForm(4))
        may = str2double(DadosForm(5))
        june = str2double(DadosForm(6))
        july = str2double(DadosForm(7))
        august = str2double(DadosForm(8))
        september = str2double(DadosForm(9))
        october = str2double(DadosForm(10))
        november = str2double(DadosForm(11))
        december = str2double(DadosForm(12))
        demand = np.array([january,february,march,april,may,june,july,august,september,october,november,december])
    
    if sel == 2:
        options.Resize = 'On'
        options.WindowStyle = 'modal'
        options.Interpreter = 'tex'
        prompt = np.array(['Enter the average consumption of eletricity per year (in kWh) \n'])
        dlg_title = 'Average eletricity consumption per month'
        num_lines = np.array([1,100])
        defaultans = np.array(['300'])
        DadosForm = inputdlg(prompt,dlg_title,num_lines,defaultans)
        dem = str2double(DadosForm(1))
        demand = dem * np.ones((1,12))
    
    if sel == 3:
        options.Resize = 'On'
        options.WindowStyle = 'modal'
        options.Interpreter = 'tex'
        prompt = np.array(['Enter [1]-AUDITORIOS; [2]-ESCRITÓRIOS; [3]-SALÃO DE BELEZA; [4]-CLUBES; [5]-ESCOLAS; [6]-SALÕES; [7]-HOSPITAIS; [8]-HOTEIS; [9]-IGREJAS; [10]-LOJAS; [11]-RESIDENCIAS; [12]-APARTAMENTO; [13]-RESTAURANTE; [14]-BANCOS; [15]-BARES; [16]-GARAGEM RESID.; [17]-GARAGEM N.RES;','Enter [1] for individual customers and [2] for a group of customers \n'])
        dlg_title = 'Average eletricity consumption per month'
        num_lines = np.array([1,100])
        defaultans = np.array(['11','1'])
        DadosForm = inputdlg(prompt,dlg_title,num_lines,defaultans)
        mod1 = str2double(DadosForm(1))
        mod2 = str2double(DadosForm(2))
        if mod2 == 1:
            demand = individual_customers(mod1,area)
        else:
            demand = group_residential_customers(mod1,area)
    
    demand = np.multiply(demand,1000)
    return demand