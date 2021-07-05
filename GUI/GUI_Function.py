import time
from GUI import GUI_Config
from GUI import GUI_plot
from GUI import GUI_Annotation
from GUI import GUI_Accesing_Common_API
from GUI import GUI_dummy_plot

Live_Plot_Common = GUI_plot.Live_Plot_Common
Live_Plot_Common_Single = GUI_plot.Live_Plot_Common_Single
Live_Plot_Fast = GUI_plot.Live_Plot_Fast
History_Plot_Common = GUI_plot.History_Plot_Common
History_Plot_Common_Single = GUI_plot.History_Plot_Common_Single
Battery_plot = GUI_Accesing_Common_API.Acces_Battery

Dummy_plot_Common_live = GUI_dummy_plot.MyDynamicMplCanvas
Dummy_plot_Common_history = GUI_dummy_plot.MyStaticMplCanvas
Dummy_plot_Battery = GUI_dummy_plot.Random_Voltage

COMMON = GUI_Config.SENSOR_COMMON
COMMON_SINGLE = GUI_Config.SENSOR_COMMON_SINGLE
FAST = GUI_Config.SENSOR_FAST
PERIOD_COMMON = GUI_Config.TIMING['Period_Time']
CONFIG_ID = GUI_Config.CONFIG_ID
ALERT = GUI_Config.ALERT
TITLE_COMMON = GUI_Annotation.Annotation_Common
TITLE_COMMON_SINGLE = GUI_Annotation.Annotation_Common_Single
TITLE_FAST = GUI_Annotation.Annotation_Fast
DEFAULT = GUI_Config.DEFAULT
BATTERY = GUI_Config.BATTERY
TIME_RANGE = GUI_Config.TIME_RANGE
N_DATA = GUI_Config.N_DATA
STEP = GUI_Config.STEP



#Adding sensor to dictionary
def Add_Sensor(type, name): 
        dict_index = {}
        for i in range(type[str(name)]):
            dict_index[str(name)+str(i+1)] = 0
        return(dict_index)
    
#Adding sensor to Index
def Add_Index(type):    
    Final_Index = {}
    for j in type:
        Index = Add_Sensor(type, j)
        Final_Index.update(Index)
    return(Final_Index)

#Add item to combo menu
def Add_Combo_Item(type, name, combo):
    dict_combo = Add_Sensor(type, name)
    for i in dict_combo:
        combo.addItem(i)

#Add time range item to combo time range menu
def Add_Combo_Time_Range(list_, combo):
    for item in list_:
        combo.addItem(item)

#Add value to the list
def Add_value(list, sensor):
    for key in sensor:
        list.append(sensor[key])

#Add Frame Into Scroll bar Area widget (The Frame must be new name)
def Add_Frame(layout, Frame, scroll_widget, widget):
    Frame = QtWidgets.QFrame(scroll_widget)
    Frame.setMinimumSize(QtCore.QSize(0, 676))
    Frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
    Frame.setFrameShadow(QtWidgets.QFrame.Raised)
    Frame.setObjectName("Frame_plot_live")

    layout = QtWidgets.QVBoxLayout(Frame)
    widget = QtWidgets.QWidget()
    layout.addWidget(widget)



#Erase Widget in layout
def Erase_Widget(layout):

    #Erase the widget
    for i in reversed(range(layout.count())):
        layout.itemAt(i).widget().setParent(None)

#Plot the Widget
def Plot_widget_dummy(function, widget, layout):

    #Plot the widget
    plot = function(widget)
    layout.addWidget(plot)

#Set Hidden set Hidden Frame
def Hidden_Frame(Frame):

    Frame.hidden()

#Make the accesing index value from 0 to 1
def zero_one_Index(dict, text):
    for key in dict:
        dict[key]=0
        if key == text:
            dict[key] = 1
            return(key)

#Check if ID is still in arrangement max_ID and min_ID
def Check_ID(ID, sensor):
    if ID > CONFIG_ID[sensor]['max_ID'] or ID < CONFIG_ID[sensor]['min_ID']:
        ALERT['Config_ID'] = 'Please Enter The Correct ID Sensor, The Correct ID for '+sensor+'is at range '+CONFIG_ID[sensor]['min_ID']+'-'+CONFIG_ID[sensor]['max_ID']
        print(ALERT['Config_ID'])
    else:
        pass

#Check The the corresponden of sum sensor with range of max_ID and min_ID
def Check_GUI_Config():
    
    #Define Empty Array
    sum_sensor = []
    range_ID = []
    
    #Adding value to sum sensor
    Add_value(sum_sensor, COMMON)
    Add_value(sum_sensor, COMMON_SINGLE)
    Add_value(sum_sensor, FAST)
    
    #Appending range ID
    for key in CONFIG_ID :
        Range_ = CONFIG_ID[key]['max_ID']-CONFIG_ID[key]['min_ID']+1
    range_ID.append(Range_)
    
    #Compare between sum sensor to range ID
    for i in range(len(sum_sensor)):
        if sum_sensor[i] != range_ID[i]:
            ALERT['Range_ID'] = 'There is asyncronous between sum and max_id and min_id of the sensor, please check the sum and range id of the sensor'
    else :
        pass

#Clasify the dictionary 
def Clasify(dict_):
    Clasify = {}
    for key in dict_:
        if dict_[key] == 1:
            Clasify.update(key)
    return(Clasify)

#Check whter the key in one of type sensor
def Check_key(dict_, index):
    for keys in dict_:
        if keys == index:
            return True

#Clasify the selected index at the certain of the type      
def Clasify_Index(Index):
    Common = Add_Index(COMMON)
    Common_single = Add_Index(COMMON_SINGLE)
    Fast = Add_Index(FAST)
    
    Clasify_Index = Index
    
    Clasify_common = Check_key(Common, Clasify_Index)
    Clasify_common_single = Check_key(Common_single, Clasify_Index)
    Clasify_fast = Check_key(Fast, Clasify_Index)
    
    if Clasify_common == True :
        RESULT = 'COMMON'
    elif Clasify_common_single == True :
        RESULT = 'COMMON_SINGLE'
    elif Clasify_fast == True :
        RESULT = 'FAST'
    else :
        RESULT = ''
    return(RESULT)

#Separate Index the number with the clasified type of sensor
def Extract_Index(Index):
    name = Index[:len(Index)-1]
    number = Index[-1] 
    return(name, number)

#Configuring ID for http request from number of separated index
def Configure_ID_Plot(Index):
    name , number = Extract_Index(Index)
    ID = (CONFIG_ID[name]['min_ID']-1)+int(number)
    return(ID)

#Calculate state of charge battery
def SOC_Battery(value):
    max_V = BATTERY['max_V']
    min_V = BATTERY['min_V']
    SOC = ((value-min_V)/(max_V-min_V))*100
    return(SOC)

#Configuring date from input GUI interface   
def Conf_date(date):
    Month = ['Jan', 'Feb', 'Mar', 'Apr', 'Mei', 'Jun', 'Jul', 'Agu', 'Sep', 'Okt', 'Nov','Des']
    Numb_12 = ['01','02','03','04','05','06','07','08','09','10','11','12']
    for i in range(len(Month)):
        if date[1] == Month[i]:
            date[1] = Numb_12[i]
    Numb_9 = ['1','2','3','4','5','6','7','8','9']
    Numb_09 = ['01','02','03','04','05','06','07','08','09']
    for j in range(len(Numb_9)):
        if date[2] == Numb_9[j]:
            date[2] = Numb_09[j]  

#==================Configuring plot from http request data with different type of sensor and plot==============================================

#Erase Widget and replace to common single live plot      
def Set_Live_Common_Single(ID, N_data, step, tittle, layout, widget):
    
    #Erase the widget
    for i in reversed(range(layout.count())):
        layout.itemAt(i).widget().setParent(None)
    
    #Replace the widget
    plot = Live_Plot_Common_Single(widget)
    plot.change_param(ID, N_data, step, tittle)
    plot.update_param(ID, N_data, step, tittle)
    layout.addWidget(plot)
    
#Erase Widget and replace to common live plot
def Set_Live_Common(ID, N_data, step, tittle, layout, widget):
    
    #Erase the widget
    for i in reversed(range(layout.count())):
        layout.itemAt(i).widget().setParent(None)
    
    #Replace the widget
    plot_0 = Live_Plot_Common(widget)
    plot_0.change_param_0(ID, N_data, step, tittle)
    plot_0.update_param_0(ID, N_data, step, tittle)
    layout.addWidget(plot_0)
    
    plot_1 = Live_Plot_Common(widget)
    plot_1.change_param_0(ID, N_data, step, tittle)
    plot_1.update_param_0(ID, N_data, step, tittle)
    layout.addWidget(plot_1)
    
    plot_2 = Live_Plot_Common(widget)
    plot_2.change_param_0(ID, N_data, step, tittle)
    plot_2.update_param_0(ID, N_data, step, tittle)
    layout.addWidget(plot_2)

#Erase Widget and replace to fast live plot    
def Set_Live_Fast(ID, N_data, step, tittle, layout, widget):
    
    #Erase the widget
    for i in reversed(range(layout.count())):
        layout.itemAt(i).widget().setParent(None)
    
    #Replace the widget
    plot = Live_Plot_Fast(widget)
    plot.change_param(ID, N_data, step, tittle)
    plot.update_param(ID, N_data, step, tittle)
    layout.addWidget(plot)

#=================================== Dummy Data =================================================================================


#Set Dummy Plot Live
def Set_Dummy_plot_single_live(layout, widget):
    
    Erase_Widget(layout)

    Plot_widget_dummy(Dummy_plot_Common_live, widget, layout)

#Set Dummy Plot Live
def Set_Dummy_plot_multi_live(scroll_widget, layout, Frame):
    
    Add_Frame(layout_2, Frame_1, scroll_widget)

    # Add_Frame(layout_3, Frame_2, scroll_widget)

    # Plot_widget_dummy(Dummy_plot_Common_live, widget_1, layout_1)

    # Plot_widget_dummy(Dummy_plot_Common_live, widget_2, layout_2)

    # Plot_widget_dummy(Dummy_plot_Common_live, widget_3, layout_3)
    
    
    



#Set Dummy Plot History
def Set_Dummy_plot_single_history(layout, widget):
    
    Erase_Widget(layout)

    Plot_widget_dummy(Dummy_plot_Common_history, widget, layout)

#Set Dummy Plot History
def Set_Dummy_plot_multi_history(layout, widget):
    
    Erase_Widget(layout)

    Plot_widget_dummy(Dummy_plot_Common_history, widget, layout)




#Set Battery Plot Battery
def Set_Dummy_plot_battery(label, text, progres_bar, lcd):
    
    label.setText(text)

    Volt = Dummy_plot_Battery(BATTERY['min_V'], BATTERY['max_V'])

    SOC = SOC_Battery(Volt)

    progres_bar.setProperty('value', SOC)

    lcd.setProperty('value', Volt)

#Set Dummy Live
def Set_Dummy_plot_live(text, index, layout, widget):
    
    key = zero_one_Index(index, text)
    clasify_result = Clasify_Index(key)

    if clasify_result == 'COMMON':
        Set_Dummy_plot_multi_live(layout ,widget)
    elif clasify_result == 'COMMON_SINGLE':
        Set_Dummy_plot_single_live(layout, widget)
    elif clasify_result == 'FAST':
        Set_Dummy_plot_single_live(layout, widget)

#Set Dummy History
def Set_Dummy_plot_history(text, index, layout, widget):
    
    key = zero_one_Index(index, text)
    clasify_result = Clasify_Index(key)

    if clasify_result == 'COMMON':
        Set_Dummy_plot_multi_history(layout, widget)
    elif clasify_result == 'COMMON_SINGLE':
        Set_Dummy_plot_single_history(layout, widget)
    elif clasify_result == 'FAST':
        Set_Dummy_plot_single_history(layout, widget)








#=======================================================================================================================================

#Set Date time for history plot          
def Set_Datetime(time_begin, time_end, date_begin, date_end):
    
    #Set Time
    T_begin = time_begin.time().toString()
    T_end = time_end.time().toString()
    
    #Set Day Begin
    D_begin = date_begin.date().toString()
    D_begin = date_begin.split(' ')
    Conf_date(D_begin)
    
    #Set Datetime begin
    datetime_begin = D_begin[3]+'-'+D_begin[1]+'-'+D_begin[2]+' '+T_begin
    datetime_begin = str(datetime_begin)
    
    #Set Day end
    D_end = date_end.date().toString()
    D_end = date_end.split(' ')
    Conf_date(D_end)
    
    #Set Datetime end
    datetime_end = D_end[3]+'-'+D_end[1]+'-'+D_end[2]+' '+T_end
    datetime_end = str(datetime_end)
    
    return[datetime_begin, datetime_end]

#Erase Widget and replace to common history plot
def Set_History_Common(ID, datetime_begin, datetime_end, step, tittle, layout, widget):
    
    #Erase the widget
    for i in reversed(range(layout.count())):
        layout.itemAt(i).widget().setParent(None)
    
    #Replace the widget
    plot_0 = History_Plot_Common(widget)
    plot_0.change_param_0(ID, datetime_begin, datetime_end, step, tittle)
    plot_0.update_param_0(ID, datetime_begin, datetime_end, step, tittle)
    layout.addWidget(plot_0)
    
    plot_1 = History_Plot_Common(widget)
    plot_1.change_param_0(ID, datetime_begin, datetime_end, step, tittle)
    plot_1.update_param_0(ID, datetime_begin, datetime_end, step, tittle)
    layout.addWidget(plot_1)
    
    plot_2 = History_Plot_Common(widget)
    plot_2.change_param_0(ID, datetime_begin, datetime_end, step, tittle)
    plot_2.update_param_0(ID, datetime_begin, datetime_end, step, tittle)
    layout.addWidget(plot_2)
    
#Erase Widget and replace to common single history plot
def Set_History_Common_Single(ID, datetime_begin, datetime_end, step, tittle, layout, widget):
    
    #Erase the widget
    for i in reversed(range(layout.count())):
        layout.itemAt(i).widget().setParent(None)
    
    #Replace the widget
    plot = History_Plot_Common_Single(widget)
    plot.change_param(ID, datetime_begin, datetime_end, step, tittle)
    plot.update_param(ID, datetime_begin, datetime_end, step, tittle)
    layout.addWidget(plot)

#Setting interval of time for live plot   
def Set_Interval(text):
    for i in range(len(TIME_RANGE)):
        if text == TIME_RANGE[i]:
            N_data = N_DATA[i]
            step = STEP[i]
    return[N_data, step]

#Set Default of live plot before interference with time range
def Set_Default_Live_Plot(text, index, layout, widget):
    
    #Proced from read combo item to http requests
    key = zero_one_Index(index, text)
    clasify_result = Clasify_Index(key) 
    ID = Configure_ID_Plot(key)
    N_data = DEFAULT['N_data']
    step = PERIOD_COMMON
    
    #Clasify type of sensor and set plot based on type
    if clasify_result == 'COMMON':
        title = TITLE_COMMON
        Set_Live_Common(ID, N_data, step, title, layout, widget)
    elif clasify_result == 'COMMON_SINGLE':
        title = TITLE_COMMON_SINGLE
        Set_Live_Common_Single(ID, N_data, step, title, layout, widget)
    elif clasify_result == 'FAST':
        title = TITLE_FAST
        Set_Live_Fast(ID, N_data, step, title, layout, widget)

#Set Live plot
def Set_Live_Plot(text, text_time, index, layout, widget):
    
    #Proced from read combo item to http requests
    key = zero_one_Index(index, text)
    clasify_result = Clasify_Index(key)
    N_data, step = Set_Interval(text_time)
    ID = Configure_ID_Plot(key)
    
    #Clasify type of sensor and set plot based on type
    if clasify_result == 'COMMON':
        title = TITLE_COMMON
        Set_Live_Common(ID, N_data, step, title, layout, widget)
    elif clasify_result == 'COMMON_SINGLE':
        title = TITLE_COMMON_SINGLE
        Set_Live_Common_Single(ID, N_data, step, title, layout, widget)
    elif clasify_result == 'FAST':
        title = TITLE_FAST
        Set_Live_Fast(ID, N_data, step, title, layout, widget)

#Set History Plot     
def Set_History_plot(text, index, time_begin, time_end, date_begin, date_end, layout, widget):
    
    #Proced from read combo item to http requests
    key = zero_one_Index(index, text)
    clasify_result = Clasify_Index(key)
    datetime_begin, datetime_end = Set_Datetime(time_begin, time_end, date_begin, date_end)
    ID = Configure_ID_Plot(key)
    step = PERIOD_COMMON
    
    #Clasify type of sensor and set plot based on type
    if clasify_result == 'COMMON':
        title = TITLE_COMMON
        Set_History_Common(ID, datetime_begin, datetime_end, step, title, layout, widget)
    elif clasify_result == 'COMMON_SINGLE':
        title = TITLE_COMMON_SINGLE
        Set_History_Common_Single(ID, datetime_begin, datetime_end, step, title, layout, widget)

#Set Battery Plot        
def Set_Battery_plot(text, index, progres_bar, lcd, label):
    
    #Proced from read combo item to http requests
    key = zero_one_Index(index, text)
    ID = Configure_ID_Plot(key)
    
    #Calculate and plot selected battery 
    while index[key] == 1:
        battery_volt = Battery_plot(ID)
        SOC = SOC_Battery(battery_volt)
        lcd.setProperty('value', battery_volt)
        progres_bar.setProperty('value', SOC)
        label.setText(SOC)
        time.sleep(PERIOD_COMMON)


    

    


        
 
        


    
     
        
        
    
    
    
