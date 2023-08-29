import firstScene
import showInfo
import sys
import os
import webbrowser
import successWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication

def readFile(dire):
	f = open(dire,'r',encoding = 'utf-8')
	txt = f.read()
	f.close()
	return txt

def OpenFile():
	try:
		filepath,f = QtWidgets.QFileDialog.getOpenFileName(scene1,'choose file','','text files(*.txt)')
		s1ui.filepathTxt.setText(filepath)
		txt = readFile(filepath)
		s1ui.displaytxt.setText(txt)
		# the path of choosed file
		f = open('./temp/dir.txt','w')
		f.write(filepath)
		f.close()
	except:
		s1ui.displaytxt.setText("no file choosed")

def ChoosePath():
	try:
		filepath = QtWidgets.QFileDialog.getExistingDirectory(scene2,'choose filr')
		ui.textBrowser.setText(filepath)
		f = open('./temp/choosePathInfo.txt','w',encoding = 'utf-8')
		f.write(filepath)
		f.close()
	except:
		ui.textBrowser.setText("no file choosed")

def ShowNER():
	try:
		f = webbrowser.open_new_tab("file:///"+os.getcwd()+"/temp/temp.html")
	except:
		print('error showNER')

def SaveNER():
	try:
		f = open('./temp/choosePathInfo.txt','r',encoding = 'utf-8')
		path = f.read()+"NER.html"
		f.close()
		f = open("./temp/temp.html",'r',encoding = 'utf-8')
		txt = f.read()
		f.close()
		f1 = open(path,'w',encoding='utf-8')
		f1.write(txt)
		f1.close()
		succUI.showPath.setText(path)
		succScene.show()
	except:
		errWindow.show()


def ShowInfo():
	try:
		pic = QtGui.QPixmap("./temp/test.jpg")
		ui2.showImage.setPixmap(pic)
		ui2.showImage.setScaledContents(True)
		ui2.showNerButton.clicked.connect(ShowNER)
		ui2.saveNerButton.clicked.connect(SaveNER)
		ui2.choosePathButton.clicked.connect(ChoosePath)

		scene2.show()
	except:
		print("error ShowInfo")


if __name__ == '__main__':
	app = QApplication(sys.argv)
	scene1 = QtWidgets.QMainWindow()
	s1ui = firstScene.Ui_MainWindow()
	s1ui.setupUi(scene1)
	s1ui.chooseFileButton.clicked.connect(OpenFile)
	s1ui.showInfoButton.clicked.connect(ShowInfo)
	# show info window
	scene2 = QtWidgets.QMainWindow()
	ui2 = showInfo.Ui_MainWindow()
	ui2.setupUi(scene2)
	scene1.show()
	sys.exit(app.exec_())
	# success window
	succScene = QtWidgets.QMainWindow()
	succUI = successWindow.Ui_MainWindow()
	succUI.setupUi(scene1)
	#
	errWindow = QtWidgets.QWidget()
	errWindow.resize(400,200)
	errWindow.setWindowTitle("Fail to Save")
	errWindow.label = QtWidgets.QLabel(errWindow)
	errWindow.label.setText("Fail to save, \ncheck if choose the path to save")