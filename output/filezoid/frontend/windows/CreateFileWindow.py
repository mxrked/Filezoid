'''
This is the CreateFileWindow
'''

from PyQt5.QtWidgets import *
from PyQt5 import uic, QtCore, QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QCursor

import sys


class CreateFileWindow(QMainWindow):


    def __init__(self):
        super(CreateFileWindow, self).__init__()

        uic.loadUi("frontend/ui/CreateFileWindow.ui", self)



        # Define widgets
        # EX: self.testWidget = self.findChild(QLineEdit, "startWindow_TestLE")
        self.backBtn = self.findChild(QPushButton, "startWindow_CreateFileBtn")
        self.fileNameLineEdit = self.findChild(QLineEdit, "createFileWindow_FileNameLineEdit")
        self.selectedFileLineEdit = self.findChild(QLineEdit, "createFileWindow_SelectedFolderLineEdit")
        self.extensionsComboBox = self.findChild(QComboBox, "createFileWindow_ExtensionsComboBox")
        self.openBtn = self.findChild(QPushButton, "createFileWindow_SelectedFolderBtn")
        self.createFileBtn = self.findChild(QPushButton, "createFileWindow_CreateFileBtn")
        self.createdFileLabel = self.findChild(QLabel, "createdFile_Label")
        self.allInputsMustBeFilledLabel = self.findChild(QLabel, "allInputsMustBeFilled_Label")

        self.fileNameLineEdit.installEventFilter(self) # Making it so that the space bar can be disabled

        # Define functions
        # EX: def doSomething():
        #       print("Test")
        def openStartWindow():
            '''
            This is used to open the start window
            :return:
            '''

            from frontend.windows.StartWindow import StartWindow

            startWindow = StartWindow()
            startWindow.move(self.pos())
            startWindow.show()

            self.hide()

        def openFileExplorer():
            '''
            This is used to open the file explorer
            :return:
            '''

            file_dialog = QFileDialog()
            file_dialog.setFileMode(QFileDialog.Directory)
            if file_dialog.exec_():
                selected_files = file_dialog.selectedFiles()
                if selected_files:
                    folder_path = selected_files[0]
                    self.selectedFileLineEdit.setText(folder_path)

                    print('Selected folder:', folder_path)  # Replace with your own logic

        def createFile():
            '''
            This is used to create a file into a targeted folder
            :return:
            '''

            fileName = self.fileNameLineEdit.text()
            selectedFolder = self.selectedFileLineEdit.text()
            selectedExtension = self.extensionsComboBox.itemText(self.extensionsComboBox.currentIndex())


            if fileName != "" and fileName != None and selectedFolder != "" and selectedFolder != None and self.extensionsComboBox.currentIndex() != 0:

                try:

                    file = selectedFolder + "/" + fileName + "." + selectedExtension

                    with open(file, 'w') as f:

                        f.write("")

                    print("File created!")
                    self.createdFileLabel.setText("Created file: " + file)

                    self.allInputsMustBeFilledLabel.setFixedHeight(0)
                    self.createdFileLabel.setFixedHeight(50)

                    self.fileNameLineEdit.setText("")
                    self.extensionsComboBox.setCurrentIndex(0)
                    self.selectedFileLineEdit.setText("")


                except IOError as e:
                    print("Error creating file.")

            else:

                self.createdFileLabel.setFixedHeight(0)
                self.allInputsMustBeFilledLabel.setFixedHeight(50)


        # Apply functions to widgets
        self.backBtn.clicked.connect(openStartWindow)
        self.openBtn.clicked.connect(openFileExplorer)
        self.createFileBtn.clicked.connect(createFile)

        # Show the app
        self.hide()



    def eventFilter(self, source, event):
        '''
        Disabling space bar
        :param source:
        :param event:
        :return:
        '''
        if event.type() == event.KeyPress and event.key() == Qt.Key_Space:
            return True
        return super().eventFilter(source, event)

    def closeEvent(self, event):
        '''
        This is used to close the window on the red X
        :param event:
        :return:
        '''
        from frontend.windows.StartWindow import StartWindow

        startWindow = StartWindow()
        startWindow.move(self.pos())
        startWindow.show()

        self.hide()


# initializing app
app = QApplication(sys.argv)
UIWindow = CreateFileWindow()
app.exec_()