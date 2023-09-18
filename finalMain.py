import final
import test
import sys
import os
import fitz
import re
import successWindow
import pandas as pd
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
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


def TranToTxt():
	if os.path.exists('./temp/dirpdffinal.txt') == False:
		ui.showPathTxt.setText('no pdf select')
		return 0
	ui.showPathTxt.setText("Changing pdf to txt...Please wait...")
	f = open('./temp/dirpdffinal.txt','r',encoding = 'utf-8')
	paths = f.readlines()
	numTxt = 0
	for path in paths:
		numTxt = numTxt + 1
		doc = fitz.open(path.replace('\n',""))
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
		tempPath = './temp/final'+str(numTxt)+".txt"
		out = open(tempPath,'w',encoding = 'utf-8')
		out.write(txt)
		out.close()
		doc.close()
		file.close()
		f.close()
	return numTxt

def OpenFile():
	try:
		s = "\n"
		filepath,f = QtWidgets.QFileDialog.getOpenFileNames(scene,'choose file','','PDF files(*.pdf)')
		p = s.join(filepath)
		ui.showPathTxt.setText(p)
		f = open('./temp/dirpdffinal.txt','w',encoding = 'utf-8')
		f.write(p)
		f.close()
	except:
		ui.showPathTxt.setText("no file choosed")
def TxtToExcel(numTxt):
	ui.showPathTxt.setText("extracting information...Please wait...")
	tempPath = './temp/final'+str(numTxt)+".txt"
	file = open(tempPath,'r',encoding = 'utf-8')
	txt = file.read()
	dfTemp = test.runModel(txt)
	return dfTemp
		

def ExExcel():
	# numFile = TranToTxt()
	try:
		numFile = TranToTxt()
	except:
		ui.showPathTxt.setText("error when changing to txt")
	
	try:
		df = pd.DataFrame()
		for n in range(1,numFile+1):
			dfTemp = TxtToExcel(n)
			df = pd.concat([df,dfTemp],axis = 0)
		df.to_excel('./Result.xlsx')
		ui.showPathTxt.setText("successfully extract")
		# path = path.strip() + '/Result.xlsx'
		ui1.showPath.setText('./Result.xlsx')
		scene1.show()
	except:
		ui.showPathTxt.setText("error when exporting excel")
app = QApplication(sys.argv)
scene = QtWidgets.QMainWindow()
ui = final.Ui_MainWindow()
ui.setupUi(scene)
ui.choosFileButton.clicked.connect(OpenFile)
ui.exportExcel.clicked.connect(ExExcel)
scene1 = QtWidgets.QMainWindow()
ui1 = successWindow.Ui_MainWindow()
ui1.setupUi(scene1)
scene.show()
sys.exit(app.exec_())