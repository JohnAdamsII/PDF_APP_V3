# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Updated_GUI.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

import os
from PyQt5 import QtCore, QtGui, QtWidgets
from APP_OOP import File, PDF
import qdarkstyle

Files_List = []
Merged_List = []
To_Be_Deleted = []


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.CovertButton = QtWidgets.QPushButton(self.centralwidget)
        self.CovertButton.setGeometry(QtCore.QRect(30, 65, 75, 23))
        self.CovertButton.setObjectName("CovertButton")


        self.imageLbl = QtWidgets.QLabel(self.centralwidget)
        self.imageLbl.setGeometry(QtCore.QRect(0, 0, 141, 131))
        self.imageLbl.setFrameShape(QtWidgets.QFrame.Box)
        self.imageLbl.setText("")
        #self.imageLb1.raise_()



        self.imageLb2 = QtWidgets.QLabel(self.centralwidget)
        self.imageLb2.setGeometry(QtCore.QRect(0, 130, 141, 131))
        self.imageLb2.setFrameShape(QtWidgets.QFrame.Box)
        self.imageLb2.setText("")


        self.imageLb3 = QtWidgets.QLabel(self.centralwidget)
        self.imageLb3.setGeometry(QtCore.QRect(0, 260, 141, 131))
        self.imageLb3.setFrameShape(QtWidgets.QFrame.Box)
        self.imageLb3.setText("")


        self.imageLb4 = QtWidgets.QLabel(self.centralwidget)
        self.imageLb4.setGeometry(QtCore.QRect(0, 390, 141, 131))
        self.imageLb4.setFrameShape(QtWidgets.QFrame.Box)
        self.imageLb4.setText("")
        




        """   self.listWidget_UL_1 = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_UL_1.setGeometry(QtCore.QRect(0, 0, 141, 131))
        self.listWidget_UL_1.setObjectName("listWidget_UL_1") """
        
        """ 
        self.listWidget_UL_2 = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_UL_2.setGeometry(QtCore.QRect(0, 130, 141, 131))
        self.listWidget_UL_2.setObjectName("listWidget_UL_2") """

        self.Merge_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Merge_Button.setGeometry(QtCore.QRect(30, 190, 75, 23))
        self.Merge_Button.setObjectName("Merge_Button")

        """         self.listWidget_UL_3 = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_UL_3.setGeometry(QtCore.QRect(0, 260, 141, 131))
        self.listWidget_UL_3.setObjectName("listWidget_UL_3") """

        self.Split_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Split_Button.setGeometry(QtCore.QRect(30, 330, 75, 23))
        self.Split_Button.setObjectName("Split_Button")
        self.Browse_Files_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Browse_Files_Button.setGeometry(QtCore.QRect(200, 140, 111, 41))
        self.Browse_Files_Button.setObjectName("Browse_Files_Button")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(200, 200, 241, 192))
        self.listWidget.setObjectName("listWidget")                                    #THIS IS FILE LIST WIDGET
        self.Browse_Folders_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Browse_Folders_Button.setGeometry(QtCore.QRect(330, 140, 111, 41))
        self.Browse_Folders_Button.setObjectName("Browse_Folders_Button")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(280, 410, 81, 21))
        self.label.setObjectName("label")

        """         self.listWidget_UL_4 = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_UL_4.setGeometry(QtCore.QRect(0, 390, 141, 131))
        self.listWidget_UL_4.setObjectName("listWidget_UL_4") """

        self.Delete_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Delete_Button.setGeometry(QtCore.QRect(30, 445, 75, 23))
        self.Delete_Button.setObjectName("Delete_Button")
        #self.listWidget_UL_1.raise_()
        self.CovertButton.raise_()
        #self.listWidget_UL_2.raise_()
        self.Merge_Button.raise_()
        #self.listWidget_UL_3.raise_()
        self.Split_Button.raise_()
        self.Browse_Files_Button.raise_()
        self.listWidget.raise_()
        self.Browse_Folders_Button.raise_()
        self.label.raise_()
        #self.listWidget_UL_4.raise_()
        self.Delete_Button.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)


        
        mainMenu = self.menubar




        
        fileMenu = mainMenu.addMenu("&Options")
        action = fileMenu.addAction("Quit")
        #action.triggered.connect()

        



        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        pixmap = QtGui.QPixmap("PDF_logo.png") # Setup pixmap with the provided image
        pixmap = pixmap.scaled(self.imageLbl.width(), self.imageLbl.height(), QtCore.Qt.KeepAspectRatio) # Scale pixmap
        self.imageLbl.setPixmap(pixmap) # Set the pixmap onto the label
        self.imageLbl.setAlignment(QtCore.Qt.AlignCenter) # Align the label to center

        pixmap = QtGui.QPixmap("merge-calls-arrow.png") # Setup pixmap with the provided image
        pixmap = pixmap.scaled(self.imageLb2.width(), self.imageLb2.height(), QtCore.Qt.KeepAspectRatio) # Scale pixmap
        self.imageLb2.setPixmap(pixmap) # Set the pixmap onto the label
        self.imageLb2.setAlignment(QtCore.Qt.AlignCenter) # Align the label to center


        pixmap = QtGui.QPixmap("arrow_diverge_split_divide_path-512.png") # Setup pixmap with the provided image
        pixmap = pixmap.scaled(self.imageLb3.width(), self.imageLb3.height(), QtCore.Qt.KeepAspectRatio) # Scale pixmap
        self.imageLb3.setPixmap(pixmap) # Set the pixmap onto the label
        self.imageLb3.setAlignment(QtCore.Qt.AlignCenter) # Align the label to center

        pixmap = QtGui.QPixmap("Delete-File-icon.png") # Setup pixmap with the provided image
        pixmap = pixmap.scaled(self.imageLb4.width(), self.imageLb4.height(), QtCore.Qt.KeepAspectRatio) # Scale pixmap
        self.imageLb4.setPixmap(pixmap) # Set the pixmap onto the label
        self.imageLb4.setAlignment(QtCore.Qt.AlignCenter) # Align the label to center





        self.Browse_Files_Button.clicked.connect(self.getFiles)                  # BUTTON FUNCTIONALITY 
        self.Browse_Folders_Button.clicked.connect(self.getFolders)
        self.CovertButton.clicked.connect(self.Convert)
        self.Merge_Button.clicked.connect(self.Merge)
        self.Split_Button.clicked.connect(self.Split) 
        self.Delete_Button.clicked.connect(self.Delete)     

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MyPDF"))
        self.CovertButton.setText(_translate("MainWindow", "Convert"))
        self.Merge_Button.setText(_translate("MainWindow", "Merge"))
        self.Split_Button.setText(_translate("MainWindow", "Split"))
        self.Browse_Files_Button.setText(_translate("MainWindow", "Browse Files"))
        self.Browse_Folders_Button.setText(_translate("MainWindow", "Browse Folders"))
        self.label.setText(_translate("MainWindow", "    Added Files"))
        self.Delete_Button.setText(_translate("MainWindow", "Delete"))






    def getFiles(self):
            fileName, _ = QtWidgets.QFileDialog.getOpenFileNames(None,"Select Files","","Files (*.pdf *.jpeg *.png *.jpg )")
            if fileName:
                for i in range(len(fileName)):
                    self.listWidget.addItem(str(fileName[i]))
                    Files_List.append(fileName[i])

    def getFolders(self):
        file = str(QtWidgets.QFileDialog.getExistingDirectory(None, "Select Folder"))
        if file:
            myfiles = File().getdir(path=file)
        for x in range(len(myfiles)):
            self.listWidget.addItem(myfiles[x])
            Files_List.append(myfiles[x])

    def Convert(self):
            pdf_obj = PDF().convert(Files_List)
            self.listWidget.clear() 

    def Merge(self):
        fileName, _ = QtWidgets.QFileDialog.getOpenFileNames(None,"Select Files","","Files (*.pdf )")
        if fileName:
            for i in range(len(fileName)):
                Merged_List.append(fileName[i])
        pdf_obj = PDF().merge(Merged_List)

    def Split(self):
        fileName, _ = QtWidgets.QFileDialog.getOpenFileNames(None,"Select File","","File (*.pdf)")
        if fileName:
            pdf_obj = PDF().split(fileName[0])

    def Delete(self):

        fileName, _ = QtWidgets.QFileDialog.getOpenFileNames(None,"Select Files","","Files (*.pdf *.jpeg *.png *.jpg )")
        if fileName:
            for i in range(len(fileName)):
                os.remove(fileName[i])
                
        """  for i in range(self.listWidget.count()):
            if fileName in self.listWidget:
                self.listWidget.takeItem(i) """


        
    def unzip(self):
        pass

        
        

    

        
         
        









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