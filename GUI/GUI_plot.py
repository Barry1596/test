import matplotlib
matplotlib.use('Qt5Agg')
from PyQt5 import QtCore, QtWidgets
from matplotlib.backends.backend_qt5agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
from GUI import GUI_Accesing_Common_API
from GUI import GUI_Accesing_Fast_API
from GUI import GUI_Config
from GUI import GUI_Annotation

import random

#Define Canvas
class Canvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        self.compute_initial_figure()
        FigureCanvas.__init__(self, fig)
        self.setParent(parent)
        FigureCanvas.setSizePolicy(
            self, QtWidgets.QSizePolicy.Expanding,QtWidgets.QSizePolicy.Expanding
        )
        FigureCanvas.updateGeometry(self)

    def compute_initial_figure(self):
        pass

#Define Live plot Canvas
class Live_Plot_Fast(Canvas):
    def __init__(self, ID):
        Canvas.__init__(self, ID)
        self.ID = ID
    
    def change_param(self, ID, N_data, step, title):
        print('change param fast')
    
    def update_param(self, ID, N_data, step, title):
        print('update param')

#Define Live plot Common Canvas
class Live_Plot_Common(Canvas):
    def __init__(self, ID):
        Canvas.__init__(self, ID)
        self.ID = ID
    
    def change_param_0(self, ID, N_data, step, title):
        self.ID = ID
        self.N_data = N_data
        self.step = step
        self.title = title
        
        timer = QtCore.QTimer(self)
        timer.timeout.connect(lambda:self.update_param0(self.ID, self.N_data, self.step, self.title))
        timer.start(GUI_Config.TIMING['Period_Time'])
        
    def change_param_1(self, ID, N_data, step, title):
        self.ID = ID
        self.N_data = N_data
        self.step = step
        self.title = title
        
        timer = QtCore.QTimer(self)
        timer.timeout.connect(lambda:self.update_param1(self.ID, self.N_data, self.step, self.title))
        timer.start(GUI_Config.TIMING['Period_Time'])
    
    def change_param_2(self, ID, N_data, step, title):
        self.ID = ID
        self.N_data = N_data
        self.step = step
        self.title = title
        
        timer = QtCore.QTimer(self)
        timer.timeout.connect(lambda:self.update_param2(self.ID, self.N_data, self.step, self.title))
        timer.start(GUI_Config.TIMING['Period_Time'])
          
    def update_param_0(self, ID, N_data, step, title):
        data = GUI_Accesing_Common_API.Acces_Live_Common(ID, N_data, step)
        x_plot = data[0]
        y_plot = data[1]
        x_plot.reverse()
        
        x_label = 'Time'
        y_label = GUI_Annotation.Annotation_Common(ID)
        y_label = y_label[1]
        
        self.axes.cla()
        self.axes.set_xlabel(x_label)
        self.axes.set_ylabel(y_label)
        self.axes.set_title(title)
        self.axes.plot(x_plot,y_plot,'r')
        self.axes.set_xticklabels(x_plot, rotation=45)
        self.draw()
    
    def update_param_1(self, ID, N_data, step, title):
        data = GUI_Accesing_Common_API.Acces_Live_Common(ID, N_data, step)
        x_plot = data[0]
        y_plot = data[2]
        x_plot.reverse()
        
        x_label = 'Time'
        y_label = GUI_Annotation.Annotation_Common(ID)
        y_label = y_label[2]
        
        self.axes.cla()
        self.axes.set_xlabel(x_label)
        self.axes.set_ylabel(y_label)
        self.axes.set_title(title)
        self.axes.plot(x_plot,y_plot,'r')
        self.axes.set_xticklabels(x_plot, rotation=45)
        self.draw()
    
    def update_param_2(self, ID, N_data, step, title):
        data = GUI_Accesing_Common_API.Acces_Live_Common(ID, N_data, step)
        x_plot = data[0]
        y_plot = data[3]
        x_plot.reverse()
        
        x_label = 'Time'
        y_label = GUI_Annotation.Annotation_Common(ID)
        y_label = y_label[3]
        
        self.axes.cla()
        self.axes.set_xlabel(x_label)
        self.axes.set_ylabel(y_label)
        self.axes.set_title(title)
        self.axes.plot(x_plot,y_plot,'r')
        self.axes.set_xticklabels(x_plot, rotation=45)
        self.draw()

#Define Live plot Common Single Canvas    
class Live_Plot_Common_Single(Canvas):
    def __init__(self, ID):
        Canvas.__init__(self, ID)
        self.ID = ID
    
    def change_param(self, ID, N_data, step, title):
        self.ID = ID
        self.N_data = N_data
        self.step = step
        self.title = title
        
        timer = QtCore.QTimer(self)
        timer.timeout.connect(lambda:self.update_param(self.ID, self.N_data, self.step, self.title))
        timer.start(GUI_Config.TIMING['Period_Time'])
        
    def update_param(self, ID, N_data, step, title):
        # data = GUI_Accesing_Common_API.Acces_Live_Common(ID, N_data, step)
        # x_plot = data[0]
        # y_plot = data[1]
        x_plot = [0, 1, 2, 3, 4]
        y_plot = [random.randint(0, 10) for i in range(N_data)]
        
        x_plot.reverse()
        
        x_label = 'Time'
        y_label = GUI_Annotation.Annotation_Common(ID)
        y_label = y_label[1]
        
        self.axes.cla()
        self.axes.set_xlabel(x_label)
        self.axes.set_ylabel(y_label)
        self.axes.set_title(title)
        self.axes.plot(x_plot,y_plot,'r')
        self.axes.set_xticklabels(x_plot, rotation=45)
        self.draw()

#Define History plot Common Single Canvas
class History_Plot_Common(Canvas):
    def __init__(self, ID):
        Canvas.__init__(self, ID)
        self.ID = ID
    
    def change_param_0(self, ID, N_data, step, title):
        self.ID = ID
        self.N_data = N_data
        self.step = step
        self.title = title
        
        timer = QtCore.QTimer(self)
        timer.timeout.connect(lambda:self.update_param0(self.ID, self.N_data, self.step, self.title))
        timer.start(GUI_Config.TIMING['Period_Time_History'])
        
    def change_param_1(self, ID, N_data, step, title):
        self.ID = ID
        self.N_data = N_data
        self.step = step
        self.title = title
        
        timer = QtCore.QTimer(self)
        timer.timeout.connect(lambda:self.update_param1(self.ID, self.N_data, self.step, self.title))
        timer.start(GUI_Config.TIMING['Period_Time_History'])
    
    def change_param_2(self, ID, N_data, step, title):
        self.ID = ID
        self.N_data = N_data
        self.step = step
        self.title = title
        
        timer = QtCore.QTimer(self)
        timer.timeout.connect(lambda:self.update_param2(self.ID, self.N_data, self.step, self.title))
        timer.start(GUI_Config.TIMING['Period_Time'])
          
    def update_param_0(self, ID, N_data, step, title):
        data = GUI_Accesing_Common_API.Acces_History_Common(ID, N_data, step)
        x_plot = data[0]
        y_plot = data[1]
        x_plot.reverse()
        
        x_label = 'Time'
        y_label = GUI_Annotation.Annotation_Common(ID)
        y_label = y_label[1]
        
        self.axes.cla()
        self.axes.set_xlabel(x_label)
        self.axes.set_ylabel(y_label)
        self.axes.set_title(title)
        self.axes.plot(x_plot,y_plot,'r')
        self.axes.set_xticklabels(x_plot, rotation=45)
        self.draw()
    
    def update_param_1(self, ID, N_data, step, title):
        data = GUI_Accesing_Common_API.Acces_History_Common(ID, N_data, step)
        x_plot = data[0]
        y_plot = data[2]
        x_plot.reverse()
        
        x_label = 'Time'
        y_label = GUI_Annotation.Annotation_Common(ID)
        y_label = y_label[2]
        
        self.axes.cla()
        self.axes.set_xlabel(x_label)
        self.axes.set_ylabel(y_label)
        self.axes.set_title(title)
        self.axes.plot(x_plot,y_plot,'r')
        self.axes.set_xticklabels(x_plot, rotation=45)
        self.draw()
    
    def update_param_2(self, ID, N_data, step, title):
        data = GUI_Accesing_Common_API.Acces_History_Common(ID, N_data, step)
        x_plot = data[0]
        y_plot = data[3]
        x_plot.reverse()
        
        x_label = 'Time'
        y_label = GUI_Annotation.Annotation_Common(ID)
        y_label = y_label[3]
        
        self.axes.cla()
        self.axes.set_xlabel(x_label)
        self.axes.set_ylabel(y_label)
        self.axes.set_title(title)
        self.axes.plot(x_plot,y_plot,'r')
        self.axes.set_xticklabels(x_plot, rotation=45)
        self.draw()

#Define History plot Common Single Canvas
class History_Plot_Common_Single(Canvas):
    def __init__(self, ID):
        Canvas.__init__(self, ID)
        self.ID = ID
    
    def change_param(self, ID, N_data, step, title):
        self.ID = ID
        self.N_data = N_data
        self.step = step
        self.title = title
        
        timer = QtCore.QTimer(self)
        timer.timeout.connect(lambda:self.update_param(self.ID, self.N_data, self.step, self.title))
        timer.start(GUI_Config.TIMING['Period_Time_History'])
        
    def update_param(self, ID, N_data, step, title):
        data = GUI_Accesing_Common_API.Acces_History_Common(ID, N_data, step)
        x_plot = data[0]
        y_plot = data[1]
        x_plot.reverse()
        
        x_label = 'Time'
        y_label = GUI_Annotation.Annotation_Common(ID)
        y_label = y_label[1]
        
        self.axes.cla()
        self.axes.set_xlabel(x_label)
        self.axes.set_ylabel(y_label)
        self.axes.set_title(title)
        self.axes.plot(x_plot,y_plot,'r')
        self.axes.set_xticklabels(x_plot, rotation=45)
        self.draw()

