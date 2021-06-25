import requests
from GUI import GUI_Config

#Accesing annotation for common type sensor for Live plot
def Annotation_Common(node_id):
    
    #Configure requests data with specified http, data, header from server and send into json form
    http = GUI_Config.REQUESTS['http_annotation_common']+GUI_Config.REQUESTS['server_id']+'/'+GUI_Config.REQUESTS['gateway_common_id']+'/'+node_id
    data = GUI_Config.BODY_DEVICE_COMMON
    headers = GUI_Config.REQUESTS['Auth']
    Request_Data = requests.get(http, params = data, headers=headers)
    Data_json = Request_Data.json()
    
    #Accesing tittle
    title = Data_json['device'][0]['name']
    
    #Acessing scale and symbol
    scale_0 = Data_json['device'][0]['data0']['scale']
    symbol_0 = Data_json['device'][0]['data0']['symbol']
    
    scale_1 = Data_json['device'][0]['data1']['scale']
    symbol_1 = Data_json['device'][0]['data1']['symbol']
    
    scale_2 = Data_json['device'][0]['data2']['scale']
    symbol_2 = Data_json['device'][0]['data2']['symbol']
    
    #Annotation array with scale and symbol
    Annotation_0 = [scale_0, symbol_0]
    Annotation_1 = [scale_1, symbol_1]
    Annotation_2 = [scale_2, symbol_2]
    
    return[title, Annotation_0, Annotation_1, Annotation_2]
     
#Accesing annotation for common single type sensor for Live plot
def Annotation_Common_Single(node_id):
    
    #Configure requests data with specified http, data, header from server and send into json form
    http = GUI_Config.REQUESTS['http_annotation_common']+GUI_Config.REQUESTS['server_id']+'/'+GUI_Config.REQUESTS['gateway_common_id']+'/'+node_id
    data = GUI_Config.BODY_DEVICE_COMMON
    headers = GUI_Config.REQUESTS['Auth']
    Request_Data = requests.get(http, params = data, headers=headers)
    Data_json = Request_Data.json()
    
    #Accesing tittle
    title = Data_json['device'][0]['name']
    
    #Acessing scale and symbol
    scale_0 = Data_json['device'][0]['data0']['scale']
    symbol_0 = Data_json['device'][0]['data0']['symbol']
    
    #Annotation array with scale and symbol
    Annotation_0 = [scale_0, symbol_0]
    
    title = 'This is common single'
    
    return(title)

#Accesing annotation for fast type sensor for Live plot
def Annotation_Fast(node_id):
    
    #Configure requests data with specified http, data, header from server and send into json form
    http = GUI_Config.REQUESTS['http_annotation_fast']+GUI_Config.REQUESTS['server_id']+'/'+GUI_Config.REQUESTS['gateway_fast_id']+'/'+node_id
    data = GUI_Config.BODY_DEVICE_FAST
    headers = GUI_Config.REQUESTS['Auth']
    Request_Data = requests.get(http, params = data, headers=headers)
    Data_json = Request_Data.json()
    
    #Accesing tittle
    title = Data_json['device'][0]['name']
     
    #Acessing scale and symbol
    scale_0 = Data_json['device'][0]['data0']['scale']
    symbol_0 = Data_json['device'][0]['data0']['symbol']
    
    scale_1 = Data_json['device'][0]['data1']['scale']
    symbol_1 = Data_json['device'][0]['data1']['symbol']
    
    scale_2 = Data_json['device'][0]['data2']['scale']
    symbol_2 = Data_json['device'][0]['data2']['symbol']
    
    #Annotation array with scale and symbol
    Annotation_0 = [scale_0, symbol_0]
    Annotation_1 = [scale_1, symbol_1]
    Annotation_2 = [scale_2, symbol_2]
    
    return[title, Annotation_0, Annotation_1, Annotation_2]