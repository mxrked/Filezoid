'''
This is the StartWindow
'''

from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5 import uic, QtCore, QtGui
from PyQt5.QtGui import QCursor

import sys


class StartWindow(QMainWindow):


    def __init__(self):
        super(StartWindow, self).__init__()

        uic.loadUi("frontend/ui/StartWindow.ui", self)



        # Define widgets
        # EX: self.testWidget = self.findChild(QLineEdit, "startWindow_TestLE")
        self.createFileBtn = self.findChild(QPushButton, "startWindow_CreateFileBtn")
        self.exitBtn = self.findChild(QPushButton, "startWindow_ExitCloseBtn")

        # Define functions
        # EX: def doSomething():
        #       print("Test")
        def exitApp():
            '''
            This is used to exit the app
            :return:
            '''

            sys.exit()

        def openCreateFileWindow():
            '''
            This is used to open the create file window
            :return:
            '''

            from frontend.windows.CreateFileWindow import CreateFileWindow

            createFileWindow = CreateFileWindow()
            createFileWindow.move(self.pos())
            createFileWindow.show()

            self.hide()

        # Apply functions to widgets
        self.createFileBtn.clicked.connect(openCreateFileWindow)
        self.exitBtn.clicked.connect(exitApp)

        # Show the app
        self.show()


    def closeEvent(self, event):
        '''
        This is used to close the window on the red X
        :param event:
        :return:
        '''

        sys.exit()


# initializing app

def main():
    app = QApplication(sys.argv)
    UIWindow = StartWindow()
    UIWindow.show()
    app.exec_()

