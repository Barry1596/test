from PyQt5 import QtCore, QtGui, QtWidgets

class Window(QtWidgets.QFrame):
    def __init__(self):
        super(Window,self).__init__()
        self.setStyle(QtWidgets.QStyleFactory.create('Cleanlooks'))
        self.setGeometry(300, 300, 600, 600)
        self.setWindowTitle("Reddit")
        self.mainWindow()
        self.show()

    def mainWindow(self):
        submissionLayout = QtWidgets.QVBoxLayout(self)
        scrollArea = QtWidgets.QScrollArea(widgetResizable=True)
        submissionLayout.addWidget(scrollArea)
        content_widget = QtWidgets.QWidget()
        scrollArea.setWidget(content_widget)
        self.scroll_layout = QtWidgets.QVBoxLayout(content_widget)
        #to handle all the api calls using praw
        
        self.printSubmissions()

    def printSubmissions(self):
        #Gets the list of all submission titles to be displayed
        #TO DO: Get and add other things like points and comments
        self.submissions = self.x.showSubmissions()

        for submission in self.submissions:
            card = QtWidgets.QWidget()
            subtitle = QtWidgets.QLabel(submission)
            subcard = QtWidgets.QVBoxLayout(card)
            subcard.addStretch()
            subcard.addWidget(subtitle)
            self.scroll_layout.addWidget(card)

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication([])
    w = Window()
    sys.exit(app.exec_())
