import PdfTxtUi
import sys
import os
import fitz
import re
import successWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication

def cleanb(txt):
	cle = txt.replace(b' ', b'')
	cle = cle.replace(b'\n',b'')
	cle = cle.replace(b'\r\n',b'')
	return cle
def clean(txt):
	cle = txt.replace(' ', '')
	cle = cle.replace('\n','')
	cle = cle.replace('\r\n','')
	return cle
def readFile(dire):
	f = open(dire,'r',encoding = 'utf-8')
	txt = f.read()
	f.close()
	return txt

def OpenFile():
	try:
		filepath,f = QtWidgets.QFileDialog.getOpenFileName(scene,'choose file','','PDF files(*.pdf)')
		ui.filePathTxt.setText(filepath)
		f = open('./temp/dirpdf.txt','w',encoding = 'utf-8')
		f.write(filepath)
		f.close()
	except:
		print("no file choosed")

def delweird(txt,settxt):
	txt = cleanb(txt)
	txt = txt.replace(bytes('８',encoding = 'utf-8'),b'8')
	txt = txt.replace(bytes('㈨',encoding = 'utf-8'),b'9')
	txt = txt.replace(bytes('㈤',encoding = 'utf-8'),b'5')
	txt = txt.replace(bytes('６',encoding = 'utf-8'),b'6')
	txt = txt.replace(bytes('９',encoding = 'utf-8'),b'9')
	txt = txt.replace(bytes('２',encoding = 'utf-8'),b'2')
	txt = txt.replace(bytes('５',encoding = 'utf-8'),b'5')
	txt = txt.replace(bytes('㈥',encoding = 'utf-8'),b'6')
	txt = txt.replace(bytes('３',encoding = 'utf-8'),b'3')
	txt = txt.replace(bytes('㈧',encoding = 'utf-8'),b'8')
	txt = txt.replace(bytes('㈣',encoding = 'utf-8'),b'4')
	txt = txt.replace(bytes('％',encoding = 'utf-8'),b'%')
	txt = txt.replace(bytes('［',encoding = 'utf-8'),b'[')
	txt = txt.replace(bytes('＝',encoding = 'utf-8'),b'=')
	txt = txt.replace(bytes('０',encoding = 'utf-8'),b'0')
	txt = txt.replace(bytes('¾',encoding = 'utf-8'),b'')
	txt = txt.replace(bytes('²',encoding = 'utf-8'),b'^2')
	txt = txt.replace(bytes('³',encoding = 'utf-8'),b'^3')
	txt = txt.replace(bytes('＜',encoding = 'utf-8'),b'<')
	txt = txt.replace(bytes('½',encoding = 'utf-8'),b'1/2')
	txt = txt.replace(bytes('７',encoding = 'utf-8'),b'7')
	txt = txt.replace(bytes('＊',encoding = 'utf-8'),b'*')
	txt = txt.replace(bytes('４',encoding = 'utf-8'),b'4')
	txt = txt.replace(bytes('ｖ',encoding = 'utf-8'),b'v')
	txt = txt.replace(bytes('ａ',encoding = 'utf-8'),b'a')
	return txt

def TranToTxt():
	if os.path.exists('./temp/dirpdf.txt') == False:
		ui.showTxt.setText('no pdf select')
		return 0
	f = open('./temp/dirpdf.txt','r',encoding = 'utf-8')
	path = f.read()
	doc = fitz.open(path)
	text = ""
	for page in doc: 
		txt = page.get_text()
		text = text + txt
	out = open('./temp/unclean.txt', "w",encoding = 'UTF-8')
	out.write(text)
	out.close()
	f =  open('./temp/unclean.txt','rb')
	text = f.read()
	file = open('./nonChEn.txt','rb')
	txt = file.read()
	settxt = set(list(str(txt,encoding = 'utf-8')))
	tranTxt = delweird(text,settxt)
	out = open('./temp/clean.txt','wb')#,encoding = 'utf-8')
	out.write(tranTxt)
	out.close()
	doc = open('./temp/clean.txt','r',encoding = 'utf-8')
	txt = doc.read()
	txt = clean(txt)
	en = re.findall(r'[a-zA-Z0-9\.\,\:\+\*\-]{10,1000}',txt)
	for e in en:
		txt = txt.replace(e,"")
	ui.showTxt.setText(txt)
	out = open('./temp/final.txt','w',encoding = 'utf-8')
	out.write(txt)
	out.close()
	doc.close()
	file.close()
	f.close()
	return 0

def ChoosePath():
	try:
		filepath = QtWidgets.QFileDialog.getExistingDirectory(scene,'choose filr')
		ui.saveFilePathTxt.setText(filepath)
		f = open('./temp/choosePath.txt','w',encoding = 'utf-8')
		f.write(filepath)
		f.close()
	except:
		print("no file choosed")


def SaveToFile():
	try:
		f = open('./temp/choosePath.txt','r',encoding = 'utf-8')
		path  = f.read()
		if path == "":
			errWindow.show()
			return 0
		path = path.strip() + "/TransedTxt.txt"
		f.close()
		f = open('./temp/final.txt','r',encoding = 'utf-8')
		txt = f.read()
		f.close()
		f = open(path,'w',encoding = 'utf-8')
		f.write(txt)
		f.close()
	
		ui1.showPath.setText(path)
		scene1.show()
	except:
		errWindow.show()

app = QApplication(sys.argv)
scene = QtWidgets.QMainWindow()
ui = PdfTxtUi.Ui_MainWindow()
ui.setupUi(scene)
ui.chooseFileButton.clicked.connect(OpenFile)
ui.transToTxtButton.clicked.connect(TranToTxt)
ui.choosePathButton.clicked.connect(ChoosePath)
ui.saveButton.clicked.connect(SaveToFile)
scene1 = QtWidgets.QMainWindow()
ui1 = successWindow.Ui_MainWindow()
ui1.setupUi(scene1)
#
errWindow = QtWidgets.QWidget()
errWindow.resize(400,200)
errWindow.setWindowTitle("Fail to Save")
errWindow.label = QtWidgets.QLabel(errWindow)
errWindow.label.setText("Fail to save, \ncheck if choose the path to save")
scene.show()
sys.exit(app.exec_())