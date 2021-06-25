import datetime

current_date_Time = datetime.datetime.now().replace(microsecond=0)
c_str_datetime = str(current_date_Time)

#Analysis Parameter
INITIAL_NATURAL_FREQUENCY = 0 #At Hz
INITIAL_PEAK_AMPLITUDE = 0 #At m/s^2
BRIDGE_SPAN = 0 #At meter
TOTAL_MASS_BRIDGE = 0 #At Kilogram
WEIGHT_LIVE_LOAD = 0 #At Kilogram

#General Parameter
REQUESTS = {
    'server_id':'0',
    'gateway_fast_id':'102',
    'gateway_common_id':'101',
    'http_fast':'http://36.92.138.59/rmcs/data/fast/',
    'http_common':'http://36.92.138.59/rmcs/data/common/',
    'http_annotation_fast':'http://36.92.138.59/rmcs/device/fast/',
    'http_annotation_common':'http://36.92.138.59/rmcs/device/common/',
    'Auth':'bearer GYmjIVhAmsQKuAXnMb3TYJO4xoeCL9Q'
}

#Define Period Time
TIMING = {
    'Period_Time': 300,
    'Period_Time_History': 12000000  
}

#Alert Warning 
ALERT = {
    'Bridge_Condition_Rating': '',
    'Bridge_Load_Rating': '',
    'Bridge_Deflection_Limit': '',
    'Bridge_Desc_Condition': '',
    'Config_ID' : '',
    'Range_ID' : '',
    'Live_Sensor' :'',
    'History_Sensor' :'',
    'Battery' :''
}

#Input the sum of sensor for common type
SENSOR_COMMON = {
    'ATRH': 4,
    'Anemometer' : 4
}

#Input the sum of sensor for common single type
SENSOR_COMMON_SINGLE = {
    'Linear_Displacement' : 4,
    'Horizontal_Inclinometer': 8,
    'Vertical_Inclinometer' : 4,
    'Frame_Strain_Gauge'  : 4,
    'Hanger_Strain_Gauge' : 12,
    'Seismometer' : 2,
    'Thermistor': 2
}

#Input the sum of sensor for fast type
SENSOR_FAST = {
    'Frame_Vibrometer': 16,
    'Hanger_Vibrometer' : 16 
}

#Input Arrangement of ID Sensor 
CONFIG_ID = {
    'ATRH' : {
        'min_ID': 1,
        'max_ID': 4
    },
    
    'Anemometer' : {
        'min_ID': 5,
        'max_ID': 8
    },
    
    'Linear_Displacement' : {
        'min_ID': 9,
        'max_ID': 12
    },
    
    'Horizontal_Inclinometer' : {
        'min_ID': 13,
        'max_ID': 20
    },
    
    'Vertical_Inclinometer' : {
        'min_ID': 21,
        'max_ID': 24
    },
    
    'Frame_Strain_Gauge' : {
        'min_ID': 25,
        'max_ID': 28
    },
    
    'Hanger_Strain_Gauge' : {
        'min_ID': 29,
        'max_ID': 40
    },
    
    'Seismometer' : {
        'min_ID': 41,
        'max_ID': 42
    },
    
    'Thermistor' : {
        'min_ID': 43,
        'max_ID': 44
    },
    
    'Frame_Vibrometer' : {
        'min_ID': 45,
        'max_ID': 60
    },
    
    'Hanger_Vibrometer' : {
        'min_ID': 61,
        'max_ID': 76
    }
       
}

#Default sum of data for last live plot
DEFAULT = {
    'N_data':6,
}

#Define maximum and minimum operating voltage of battery
BATTERY = {
    'min_V': 2.5,
    'max_V': 4.2
}

#Parameter for time range plot
TIME_RANGE = ['30 minutes', '1 hour', '2 hours', '4 hours', '12 hours', '1 day']
N_DATA = [5, 5, 5, 5, 5]
STEP = [1, 2, 2, 2, 2]


#Description
DESCRIPTION = {
    'Bridge_Name':'Rumpiang Bridge',
    'General':'General graphical user interface for remote monitoring and control systems from PT.Gundala Telemtri Nusantara for',
    'ATRH':'ATRH are located at the central of the bridge (H14-H16) and corner of the bridge',
    'Anemometer':'Anemometer are located at the central of the bridge H15',
    'Linear_Displacement':'Linear Displacement are located at the anchor support of the bridge in the river',
    'Horizontal_Inclinometer':"""The detail location of Horizontal Inclinometer are represented below:
                                 1. H_Inclinometer1 = H4 - G3
                                 2. H_Inclinometer2 = H4 - G3
                                 3. H_Inclinometer3 = H4 - G3
                                 4. H_Inclinometer4 = H4 - G3
                                 5. H_Inclinometer5 = H4 - G3
                                 6. H_Inclinometer6 = H4 - G3
                                 7. H_Inclinometer7 = H4 - G3
                                 8. H_Inclinometer8 = H4 - G3""",
    'Vertical_Inclinometer':"""The detail location of Horizontal Inclinometer are represented below:
                                 1. H_Inclinometer1 = H4 - G3
                                 2. H_Inclinometer2 = H4 - G3
                                 3. H_Inclinometer3 = H4 - G3
                                 4. H_Inclinometer4 = H4 - G3
                                 5. H_Inclinometer5 = H4 - G3
                                 6. H_Inclinometer6 = H4 - G3
                                 7. H_Inclinometer7 = H4 - G3
                                 8. H_Inclinometer8 = H4 - G3""",
    'Frame_Strain_Gauge':"""The detail location of Horizontal Inclinometer are represented below:
                                 1. H_Inclinometer1 = H4 - G3
                                 2. H_Inclinometer2 = H4 - G3
                                 3. H_Inclinometer3 = H4 - G3
                                 4. H_Inclinometer4 = H4 - G3
                                 5. H_Inclinometer5 = H4 - G3
                                 6. H_Inclinometer6 = H4 - G3
                                 7. H_Inclinometer7 = H4 - G3
                                 8. H_Inclinometer8 = H4 - G3""",
    'Hanger_Strain_Gauge':"""The detail location of Horizontal Inclinometer are represented below:
                                 1. H_Inclinometer1 = H4 - G3
                                 2. H_Inclinometer2 = H4 - G3
                                 3. H_Inclinometer3 = H4 - G3
                                 4. H_Inclinometer4 = H4 - G3
                                 5. H_Inclinometer5 = H4 - G3
                                 6. H_Inclinometer6 = H4 - G3
                                 7. H_Inclinometer7 = H4 - G3
                                 8. H_Inclinometer8 = H4 - G3""",
    'Seismometer':'Seismometer are located in the ground near abudment',
    'Thermistor':'Temperature material sensor are located at the central of the bridge',
    'Frame_Vibrometer':"""The detail location of Horizontal Inclinometer are represented below:
                                 1. H_Inclinometer1 = H4 - G3
                                 2. H_Inclinometer2 = H4 - G3
                                 3. H_Inclinometer3 = H4 - G3
                                 4. H_Inclinometer4 = H4 - G3
                                 5. H_Inclinometer5 = H4 - G3
                                 6. H_Inclinometer6 = H4 - G3
                                 7. H_Inclinometer7 = H4 - G3
                                 8. H_Inclinometer8 = H4 - G3""",
    'Hanger_Vibrometer':"""The detail location of Horizontal Inclinometer are represented below:
                                 1. H_Inclinometer1 = H4 - G3
                                 2. H_Inclinometer2 = H4 - G3
                                 3. H_Inclinometer3 = H4 - G3
                                 4. H_Inclinometer4 = H4 - G3
                                 5. H_Inclinometer5 = H4 - G3
                                 6. H_Inclinometer6 = H4 - G3
                                 7. H_Inclinometer7 = H4 - G3
                                 8. H_Inclinometer8 = H4 - G3""",
    
    'Tittle_Analysis':'Description',
    'Desc_Analysis' :"""The analysis ..........
                        .......................""",
    'Tittle_Assumption':'Assumption',
    'Desc_Assumption':"""The assumption .......
                        ......................."""
    
}



#=================================Request Template=================================================================================================

#PARAM Form Requests
PARAM_Live_Fast = {
    "data[0]": 'battery',
    "data[1]": 'data0',
    "data[2]": 'data1',
    "data[3]": 'data2',
    "options[filterTime]": c_str_datetime
}

PARAM_Live_BATTERY = {
    "data[0]": 'battery',
    "options[filterTime]": c_str_datetime
}

PARAM_Live_Common = {
    "data[0]": 'data0',
    "data[1]": 'data1',
    "data[2]": 'data2',
    "data[3]": 'battery',
    "options[filterTime]": c_str_datetime,
    "options[filterNumberBefore]": 0,
    "options[filterStep]": 0
}

PARAM_History_Common = {
    "data[0]": 'data0',
    "data[1]": 'data1',
    "data[2]": 'data2',
    "data[3]": 'battery',
    "options[filterBegin]": '',
    "options[filterEnd]": '',
    "options[filterStep]": 0
}

PARAM_Live_Common_Single = {
    "data[0]": 'data0',
    "data[1]": 'battery',
    "options[filterTime]": c_str_datetime,
    "options[filterNumberBefore]": 0,
    "options[filterStep]": 0
}

PARAM_History_Common_Single = {
    "data[0]": 'data0',
    "data[1]": 'battery',
    "options[filterBegin]": '',
    "options[filterEnd]": '',
    "options[filterStep]": 0
}

#BODY Form Requests
BODY_Live_Fast = {
    "data": ["battery", "data0", "data1", "data2"],
    "options":{
        "filterTime": c_str_datetime
    }
}

BODY_Live_Battery = {
    "data": ["battery"],
    "options":{
        "filterTime": c_str_datetime
    }
}

BODY_Live_Common = {
    "data": ["data0", "data1", "data2", "battery"],
    "options":{
        "filterTime": c_str_datetime,
        "filterNumberBefore": 0,
        "filterStep": 0
    } 
}

BODY_Live_Common_Single = {
    "data": ["data0", "battery"],
    "options":{
        "filterTime": c_str_datetime,
        "filterNumberBefore": 0,
        "filterStep": 0
    } 
}

BODY_History_Common = {
    "data": ["data0", "data1", "data2", "battery"],
    "options":{
        "filterBegin": 0,
        "filterEnd": 0,
        "filterStep": 0
    } 
}
  
BODY_History_Common_Single = {
    "data": ["data0", "battery"],
    "options":{
        "filterBegin": 0,
        "filterEnd": 0,
        "filterStep": 0
    } 
}

#========================Device Annotation=====================
PARAM_DEVICE_COMMON = {
    
}

PARAM_DEVICE_FAST = {
    
}

BODY_DEVICE_COMMON = {
    "device":["name", "scale", "symbol"],
    "options":{
        "showId": True
    }
}

BODY_DEVICE_FAST = {
    "device":["name","scale", "symbol"],
    "options":{
        "showId": True
    }
}




