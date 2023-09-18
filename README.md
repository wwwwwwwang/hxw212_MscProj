# hxw212_MscProj
code for uob Msc Project "information extraction from Chinese medical paper"

To run the main window of the project, use 'python finalMain.py'command

* Please make sure all the python library needed is installed. (sys,os,fitz,re,successWindow, pandas, PyQt5, numpy, pandas, spacy, json, matplotlib, random, etc.) 
* The spaCy chinese pipeline 'zh_core_web_lg' is installed.(python -m spacy download zh_core_web_lg)
* The model is too large for the repostry, so run 'trainSpacy.py' first to train the model, which will take about twenty minutes.
* The 'trainSpacy.py', 'test.py','evaluate.py' must be run with the data, to run those file please make sure all the data is in the same name of file as in this repostry and in the same relatve path with the code. 
* It may take a while after use 'python finalMain.py'command, before the UI shows.
* It also take a while to extract data.
* Please make sure the '.\temp' path exist or some error might rise.
