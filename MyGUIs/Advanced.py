# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Advanced.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 1000)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.AddFilesButton = QtWidgets.QPushButton(self.centralwidget)
        self.AddFilesButton.setGeometry(QtCore.QRect(20, 120, 181, 71))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        self.AddFilesButton.setFont(font)
        self.AddFilesButton.setObjectName("AddFilesButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(400, 10, 241, 31))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.MylistWidget = QtWidgets.QListWidget(self.centralwidget)
        self.MylistWidget.setGeometry(QtCore.QRect(250, 60, 471, 231))
        self.MylistWidget.setObjectName("MylistWidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


        self.AddFilesButton.clicked.connect(self.getFiles)



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.AddFilesButton.setText(_translate("MainWindow", "Add Files"))
        self.label.setText(_translate("MainWindow", "Added Files"))

    def getFiles(self):

        #fileName = QtWidgets.QFileDialog.getSaveFileName(None, "Save file", "", "Image Files (*.png *.jpg *.jpeg *.pdf *.zip)")
        
        fileName, _ = QtWidgets.QFileDialog.getOpenFileNames(None,"Select Files", "", "Image Files (*.png *.jpg *.jpeg *.pdf *.zip) ")
        if fileName:
            self.MylistWidget.addItem(str(fileName))
        
        
        
        


    def getFolders(self):
        pass
        """ file = str(QtWidgets.QFileDialog.getExistingDirectory(None, "Select Directory"))
        if file:
            self.MylistWidget.addItem(str(file))  """


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())