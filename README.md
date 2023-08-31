# Data Science MSc Project
code for MSc Project "information extraction from Chinese medical paper"

## Requeirment
Python 3.8.3
python packages:"PdfTxtUi","sys","os","fitz","re","PyQt5","webbrowser","openpyxl"
Please confirm your matplotlib support 'Microsoft YaHei' using matplotlib.font_manager

## Explaination of folder and files
### What's in folder
* trainpdf and testpdf folder store pdf format original chinese medical paper for train and test.
* traintxt and testtxt folder store txt format chinese medical paper changed through pdftxt.py
* cleantest folder store cleaned txt format testing data for test model.
* cleantrain folder store cleaned txt format training data and some of its annotation files in .ann .bio and .bmes.
* trainann folder only store .bio format training data. This folder is used for training ner model.
* temp folder store temporery data used in pdftxtexe.py and showinfo.py

### Important files
* pdftxtexe.py file is used for tranform a pdf format data to txt format data. To use it, the successWindow.py, successWindow.ui, PdfTxtUi.py and PdfTxt.ui must be in the same folder.
* infoEx.py file is used for extract information from .txt format paper. To use it, the successWindow.py, successWindow.ui, showInfo.py, showInfo.ui, firstScene.py and firstScene.ui must be in the same folder.
