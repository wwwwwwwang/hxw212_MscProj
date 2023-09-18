# hxw212_MscProj
code for uob Msc Project "information extraction from Chinese medical paper"

To run the main window of the project, use 'python finalMain.py'command

*please make sure all the python library needed is installed. (sys,os,fitz,re,successWindow, pandas, PyQt5, numpy, pandas, spacy. json, matplotlib) 
*the spaCy chinese pipeline 'zh_core_web_lg' is installed.(python -m spacy download zh_core_web_lg)
*The model is too large for the repostry, so run 'trainSpacy.py first' to train the model, which will take about twenty minutes.
*it may take a while after use 'python finalMain.py'command, before the UI shows.
*it also take a while to extract data.
