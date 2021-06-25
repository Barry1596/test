
import datetime
import requests
from GUI import GUI_Config

#Configuring Current datetime for Live Plot
current_date_Time = datetime.datetime.now().replace(microsecond=0, second=0)
current_date_Time = current_date_Time - datetime.timedelta(seconds = current_date_Time.second%GUI_Config.TIMING['Period_Time'])

#Accesing data for common type sensor for Live plot
def Acces_Live_Common(node_id, N_data, step):
    
    #Configure requests data with specified http, data, header from server and send into json form
    http = GUI_Config.REQUESTS['http_common']+GUI_Config.REQUESTS['server_id']+'/'+GUI_Config.REQUESTS['gateway_common_id']+'/'+node_id
    GUI_Config.PARAM_Live_Common['options[filterNumberBefore]'] = N_data
    GUI_Config.PARAM_Live_Common['options[filterStep]'] = step*GUI_Config.TIMING['Period_Time']
    data = GUI_Config.PARAM_Live_Common
    headers = GUI_Config.REQUESTS['Auth']
    Request_Data = requests.get(http, params = data, headers=headers)
    Data_json = Request_Data.json()
    datetime_list = [current_date_Time - datetime.timedelta(seconds=(GUI_Config.TIMING['Period_Time']*step*x)) for x in range(N_data)]
    
    #Define empty array for data plot
    time = []
    data0 = []
    data1 = []
    data2 = []
    battery = []
    
    #Appending time array for live plot
    for j in range(len(datetime_list)):
        datetime_ = datetime_list[j].strftime("%Y-%m-%d %H:%M:%S")
        datetime_ = datetime_.split(' ')
        datetime_ = datetime_[1]
        time.append(datetime_)
        
    #Appending array of data sensor for common sensor in live plot
    for i in range(len(range(N_data))):
        data0_plot = float(Data_json['data'][i]['data0'])
        data0.append(data0_plot)
        data1_plot = float(Data_json['data'][i]['data1'])
        data1.append(data1_plot)
        data2_plot = float(Data_json['data'][i]['data2'])
        data2.append(data2_plot)
        battery_plot = float(Data_json['data'][i]['battery'])
        battery.append(battery_plot)
    
    return [time, data0, data1, data2, battery]

#Accesing data for common single type sensor for Live plot
def Acces_Live_Common_Single(node_id, N_data, step):
    
    #Configure requests data with specified http, data, header from server and send into json form
    http = GUI_Config.REQUESTS['http_common']+GUI_Config.REQUESTS['server_id']+'/'+GUI_Config.REQUESTS['gateway_common_id']+'/'+node_id
    GUI_Config.PARAM_Live_Common_Single['options[filterNumberBefore]'] = N_data
    GUI_Config.PARAM_Live_Common_Single['options[filterStep]'] = step*GUI_Config.TIMING['Period_Time']
    data = GUI_Config.PARAM_Live_Common_Single
    headers = GUI_Config.REQUESTS['Auth']
    Request_Data = requests.get(http, params = data, headers=headers)
    Data_json = Request_Data.json()
    datetime_list = [current_date_Time - datetime.timedelta(seconds=(GUI_Config.TIMING['Period_Time']*step*x)) for x in range(N_data)]
    
    #Define empty array for data plot
    time = []
    data0 = []
    battery = []
    
    #Appending time array for live plot
    for j in range(len(datetime_list)):
        datetime_ = datetime_list[j].strftime("%Y-%m-%d %H:%M:%S")
        datetime_ = datetime_.split(' ')
        datetime_ = datetime_[1]
        time.append(datetime_)
        
    #Appending array of data sensor for common single sensor in live plot
    for i in range(len(range(N_data))):
        data0_plot = float(Data_json['data'][i]['data0'])
        data0.append(data0_plot)
        battery_plot = float(Data_json['data'][i]['battery'])
        battery.append(battery_plot)
        
    return [time, data0, battery]

#Accesing Battery volt from API for live monitoring plot
def Acces_Battery(node_id):
    
    #Configure requests data with specified http, data, header from server and send into json form
    http = GUI_Config.REQUESTS['http_common']+GUI_Config.REQUESTS['server_id']+'/'+GUI_Config.REQUESTS['gateway_common_id']+'/'+node_id
    data = GUI_Config.PARAM_Live_BATTERY
    headers = GUI_Config.REQUESTS['Auth']
    Request_Data = requests.get(http, params = data, headers=headers)
    Data_json = Request_Data.json() 
    
    #Accessing batttery voltage
    battery = float(Data_json['data'][0]['battery'])
    
    return(battery)

#Accesing data for common type sensor for History plot
def Acces_History_Common(node_id, datetime_begin, datetime_end):
    
    #Configure requests data with specified http, data, header from server and send into json form
    http = GUI_Config.REQUESTS['http_common']+GUI_Config.REQUESTS['server_id']+'/'+GUI_Config.REQUESTS['gateway_common_id']+'/'+node_id
    GUI_Config.PARAM_History_Common['options[filterBegin]'] = datetime_begin
    GUI_Config.PARAM_History_Common['options[filterEnd]'] = datetime_end
    GUI_Config.PARAM_History_Common['options[filterStep]'] = GUI_Config.TIMING['Period_Time']
    data = GUI_Config.PARAM_History_Common
    headers = GUI_Config.REQUESTS['Auth']
    Request_Data = requests.get(http, params = data, headers=headers)
    Data_json = Request_Data.json()
    
    #Define empty array for data plot
    time = []
    data0 = []
    data1 = []
    data2 = []
    battery = []
    
    #Appending array of data sensor for common sensor in history plot
    for i in range(len(Data_json['data'])):
        time_plot = Data_json['data'][i]['time']
        time_plot = datetime.datetime.strptime(time_plot,"%Y-%m-%d %H:%M:%S")
        time.append(time_plot)
        data0_plot = float(Data_json['data'][i]['data0'])
        data0.append(data0_plot)
        data1_plot = float(Data_json['data'][i]['data1'])
        data1.append(data1_plot)
        data2_plot = float(Data_json['data'][i]['data2'])
        data2.append(data2_plot)
        battery_plot = float(Data_json['data'][i]['battery'])
        battery.append(battery_plot)
    
    return[time, data0, data1, data2, battery]

#Accesing data for common single type sensor for History plot        
def Acces_History_Common_Single(node_id, datetime_begin, datetime_end):
    
    #Configure requests data with specified http, data, header from server and send into json form
    http = GUI_Config.REQUESTS['http_common']+GUI_Config.REQUESTS['server_id']+'/'+GUI_Config.REQUESTS['gateway_common_id']+'/'+node_id
    GUI_Config.PARAM_History_Common_Single['options[filterBegin]'] = datetime_begin
    GUI_Config.PARAM_History_Common_Single['options[filterEnd]'] = datetime_end
    GUI_Config.PARAM_History_Common_Single['options[filterStep]'] = GUI_Config.TIMING['Period_Time']
    data = GUI_Config.PARAM_History_Common_Single
    headers = GUI_Config.REQUESTS['Auth']
    Request_Data = requests.get(http, params = data, headers=headers)
    Data_json = Request_Data.json()
    
    #Define empty array for data plot
    time = []
    data0 = []
    battery = []
    
    #Appending array of data sensor for common single sensor in history plot
    for i in range(len(Data_json['data'])):
        time_plot = Data_json['data'][i]['time']
        time_plot = datetime.datetime.strptime(time_plot,"%Y-%m-%d %H:%M:%S")
        time.append(time_plot)
        data0_plot = float(Data_json['data'][i]['data0'])
        data0.append(data0_plot)
        battery_plot = float(Data_json['data'][i]['battery'])
        battery.append(battery_plot)
        
    return[time, data0, battery]


    
