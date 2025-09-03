import numpy as np
    
def wind_data(wind_speed = None): 
    if wind_speed == 1:
        options.Resize = 'On'
        options.WindowStyle = 'modal'
        options.Interpreter = 'tex'
        prompt = np.array(['Enter the average wind speed in January (in m/s) \n','Enter the average wind speed in February (in m/s) \n','Enter the average wind speed in March (in m/s) \n','Enter the average wind speed in April (in m/s) \n','Enter the average wind speed in May (in m/s) \n','Enter the average wind speed in June (in m/s) \n','Enter the average wind speed in July (in m/s) \n','Enter the average wind speed in August (in m/s) \n','Enter the average wind speed in September (in m/s) \n','Enter the average wind speed in October (in m/s) \n','Enter the average wind speed in November (in m/s) \n','Enter the average wind speed in December (in m/s) \n'])
        dlg_title = 'average wind speed per month'
        num_lines = np.array([1,100])
        defaultans = str2double
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
        wind_speed = np.array([january,february,march,april,may,june,july,august,september,october,november,december])
    
    if wind_speed == 2:
        options.Resize = 'On'
        options.WindowStyle = 'modal'
        options.Interpreter = 'tex'
        prompt = np.array(['Enter the average wind speed per year (in m/s) \n'])
        dlg_title = 'average wind speed per month'
        num_lines = np.array([1,100])
        defaultans = np.array(['3'])
        DadosForm = inputdlg(prompt,dlg_title,num_lines,defaultans)
        dem = str2double(DadosForm(1))
        wind_speed = dem * np.ones((1,12))
    
    return wind_speed