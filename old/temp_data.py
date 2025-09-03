import numpy as np
    
def temp_data(x_temp = None): 
    if x_temp == 1:
        options.Resize = 'On'
        options.WindowStyle = 'modal'
        options.Interpreter = 'tex'
        prompt = np.array(['Enter the average temperature in January (in ºC) \n','Enter the average temperature in February (in ºC) \n','Enter the average temperature in March (in ºC) \n','Enter the average temperature in April (in ºC) \n','Enter the average temperature in May (in ºC) \n','Enter the average temperature in June (in ºC) \n','Enter the average temperature in July (in ºC) \n','Enter the average temperature in August (in ºC) \n','Enter the average temperature in September (in ºC) \n','Enter the average temperature in October (in ºC) \n','Enter the average temperature in November (in ºC) \n','Enter the average temperature in December (in ºC) \n'])
        dlg_title = 'Average temperature per month'
        num_lines = np.array([1,100])
        defaultans = np.array(['26.1','26','25.2','23.6','21.8','20.9','20.6','21','21.7','22.5','23.8','24.6'])
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
        x_temp = np.array([january,february,march,april,may,june,july,august,september,october,november,december])
    
    if x_temp == 2:
        options.Resize = 'On'
        options.WindowStyle = 'modal'
        options.Interpreter = 'tex'
        prompt = np.array(['Enter the average temperature per year (in ºC) \n'])
        dlg_title = 'Average temperature per month'
        num_lines = np.array([1,100])
        defaultans = np.array(['23'])
        DadosForm = inputdlg(prompt,dlg_title,num_lines,defaultans)
        dem = str2double(DadosForm(1))
        x_temp = dem * np.ones((1,12))
    
    return x_temp