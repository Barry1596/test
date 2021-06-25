import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
import requests
from GUI import GUI_Config

#Accesing data for fast type sensor for Live plot
def Access_Live_Fast(node_id):
    
    #Configure requests data with specified http, data, header from server and send into json form
    http = GUI_Config.REQUESTS['http_fast']+GUI_Config.REQUESTS['server_id']+'/'+GUI_Config.REQUESTS['gateway_fast_id']+'/'+node_id
    data = GUI_Config.PARAM_Live_Fast
    headers = GUI_Config.REQUESTS['Auth']
    Request_Data = requests.get(http, params = data, headers=headers)
    Data_json = Request_Data.json()
    
    #Define empty array for data plot
    time = []
    battery = []
    data0 = []
    data1 = []
    data2 = []
    
    #Appending array of data sensor for fast sensor in live plot
    for i in range(len(Data_json['data'])):
        print('j')
        
        
    return [time, battery, data0, data1, data2]


