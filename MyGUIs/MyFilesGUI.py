# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MyFilesGUI.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
import time
from PyQt5 import QtCore, QtGui, QtWidgets
from APP_OOP import File, PDF
import qdarkstyle


Files_List = []

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1059, 721)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.AddFilesButton = QtWidgets.QPushButton(self.centralwidget)
        self.AddFilesButton.setGeometry(QtCore.QRect(10, 130, 181, 71))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        self.AddFilesButton.setFont(font)
        self.AddFilesButton.setObjectName("AddFilesButton")
        self.Files_label = QtWidgets.QLabel(self.centralwidget)
        self.Files_label.setGeometry(QtCore.QRect(340, 10, 241, 31))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(12)
        self.Files_label.setFont(font)
        self.Files_label.setObjectName("Files_label")
        self.MyFilesListWidget = QtWidgets.QListWidget(self.centralwidget)
        self.MyFilesListWidget.setGeometry(QtCore.QRect(210, 50, 421, 251))
        self.MyFilesListWidget.setObjectName("MyFilesListWidget")
        self.AddFolders_Button = QtWidgets.QPushButton(self.centralwidget)
        self.AddFolders_Button.setGeometry(QtCore.QRect(10, 470, 181, 71))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        self.AddFolders_Button.setFont(font)
        self.AddFolders_Button.setObjectName("AddFolders_Button")
        self.MyFolderListWidget = QtWidgets.QListWidget(self.centralwidget)
        self.MyFolderListWidget.setGeometry(QtCore.QRect(210, 380, 421, 251))
        self.MyFolderListWidget.setObjectName("MyFolderListWidget")
        self.Folder_label = QtWidgets.QLabel(self.centralwidget)
        self.Folder_label.setGeometry(QtCore.QRect(340, 330, 241, 31))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(12)
        self.Folder_label.setFont(font)
        self.Folder_label.setObjectName("Folder_label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1059, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.AddFilesButton.clicked.connect(self.getFiles)
        self.AddFolders_Button.clicked.connect(self.getFolders)  
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
       
        MainWindow.setWindowTitle(_translate("MainWindow", "MyPDF"))
        self.AddFilesButton.setText(_translate("MainWindow", "Add Files"))
        self.Files_label.setText(_translate("MainWindow", "Added Files"))
        self.AddFolders_Button.setText(_translate("MainWindow", "Convert"))  #comments 
        self.Folder_label.setText(_translate("MainWindow", "Added Folders"))


    def getFiles(self):
        fileName, _ = QtWidgets.QFileDialog.getOpenFileNames(None,"Select Files","","All Files (*.pdf *.jpeg *.png *.jpg )")
        if fileName:
            for i in range(len(fileName)):
                self.MyFilesListWidget.addItem(str(fileName[i]))
                Files_List.append(fileName[i])
            
        
    def getFolders(self):
        PDFobj = PDF().convert(Files_List)
        
        #make ability to select multiple folders
        #file = str(QtWidgets.QFileDialog.getExistingDirectory(None, "Select Folder"))
        #if file:
            #self.MyFolderListWidget.addItem(str(file))
       

    def Convert(self):
        pass
        #pdf_obj = PDF().convert(FilesList)

    def Delete(self):
        pass

    def Merge(self):
        pass

    def Split(self):
        pass

    def DocxToPDF(self):
        pass

    def MoveFilesToCWD(self):
        pass

    def Iterate_list(self):
        FilesList = []
        for x in range(self.MyFilesListWidget.count()):
            FilesList.append(self.MyFilesListWidget.item(x).text())
        #[print(x) for x in items]

    def Mutithreading(self):
        pass

    def WebApp(self):
        pass
    
    def Testing(self):
        pass

    def Convert_2_exe(self):
        pass

    def make_beauiful(self):
        pass

    def dynamic_resizing(self):
        pass

    """ allow user to open files in listwidget """

    """ change the look of top bar """

    """ Add File Menu """
     
    











if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()

    MainWindow.setWindowIcon(QtGui.QIcon('py_icon.png'))
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())

    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())