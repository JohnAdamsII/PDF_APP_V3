#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
import sys
#from PyQt4.QtGui import *
from PyQt5 import QtCore, QtGui, QtWidgets

# Create an PyQT4 application object.
a = QtWidgets.QApplication(sys.argv) 
 
# The QWidget widget is the base class of all user interface objects in PyQt4.
w = QtWidgets.QMainWindow()
 
# Set window size. 
w.resize(320, 240)
 
# Set window title 
w.setWindowTitle("Hello World!")
 
# Get filename using QFileDialog
filename = QtWidgets.QFileDialog.getOpenFileName(w, 'Open File', '/')
print(filename)
 
# print file contents
with open(filename, 'r') as f:
    print(f.read())
 
# Show window
w.show() 
 
sys.exit(a.exec_())