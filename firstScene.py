# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'firstScene.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Information Extraction From Paper")
        MainWindow.resize(800, 500)
        self.path = ""
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.chooseFileButton = QtWidgets.QPushButton(self.centralwidget)
        self.chooseFileButton.setGeometry(QtCore.QRect(360, 20, 121, 31))
        self.chooseFileButton.setObjectName("chooseFileButton")
        self.exExcelButton = QtWidgets.QPushButton(self.centralwidget)
        self.exExcelButton.setGeometry(QtCore.QRect(490, 20, 141, 31))
        self.exExcelButton.setObjectName("exExcelButton")
        self.filepathTxt = QtWidgets.QTextBrowser(self.centralwidget)
        self.filepathTxt.setGeometry(QtCore.QRect(50, 20, 291, 31))
        self.filepathTxt.setObjectName("filepathTxt")
        self.filepathTxt.setText("Txt file only")
        self.filepathTxt.setAcceptDrops(True)
        self.displaytxt = QtWidgets.QTextBrowser(self.centralwidget)
        self.displaytxt.setGeometry(QtCore.QRect(50, 70, 701, 351))
        self.displaytxt.setAutoFillBackground(False)
        self.displaytxt.setObjectName("displaytxt")
        self.showInfoButton = QtWidgets.QPushButton(self.centralwidget)
        self.showInfoButton.setGeometry(QtCore.QRect(640, 20, 111, 31))
        self.showInfoButton.setObjectName("showInfoButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setEnabled(False)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def dragEnterEvent(self,e):
        evn.accept()

    def dropEvent(self,e):
        path = e.mimeData().text.replace('file:///',"")
        self.filepathTxt.setText(path)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.chooseFileButton.setText(_translate("MainWindow", "Choose File"))
        self.exExcelButton.setText(_translate("MainWindow", "Export Excel"))
        self.displaytxt.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.showInfoButton.setText(_translate("MainWindow", "Show Info"))
