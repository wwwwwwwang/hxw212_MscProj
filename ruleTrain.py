import random
import validation
import evaluate
import json
import spacy
from spacy.tokens import Doc
from spacy.tokens import Span
from spacy.training import Example
from spacy.pipeline import EntityRuler
import pandas as pd
def eva(trueArr):
	preArr = pd.read_excel('./vali_ru.xlsx').values
	tp = 0
	fn = 0 
	fp = 0
	for r in range(0,25):
		for c in range(1,16):
			tr = trueArr[r][c]
			pr = preArr[r][c]
			if tr == pr:
				tp  =tp + 1
			elif pd.isna(tr) and pd.isna(pr) == False:
				fp = fp + 1
			elif pd.isna(tr)==False and pd.isna(pr):
				fn = fn + 1
	pre = evaluate.precision(tp,fp)
	rec = evaluate.recall(tp,fn)
	fs = evaluate.f_score(pre,rec)
	# print("numloop: "+loo+ " drop:" + drp)
	print("precision:"+str(pre))
	print("recall:"+str(rec))
	print("f-score:"+str(fs))
	return pre,rec,fs

nlp = spacy.load("zh_core_web_lg")

patterns = [{"label": "rsRx","pattern": "人参总皂苷"},
{"label": "rsRx","pattern": "人参皂苷Rg3"},
{"label": "rsRx","pattern": "人参皂苷Re"},
{"label": "rsRx", "pattern": "人参皂苷Rg1"},
{"label": "rsRx", "pattern": "人参皂苷Rg2"},
{"label": "rsRx", "pattern": "人参皂苷Rg"},
{"label": "rsRx", "pattern": "人参水煎液"},
{"label": "rsRx", "pattern": "人参三醇类皂苷"},
{"label": "rsRx", "pattern": "人参皂苷Ck"},
{"label": "rsRx", "pattern": "人参提取物"},
{"label": "rsRx", "pattern": "人参二醇类皂苷"},
{"label": "rs", "pattern": "人参"},
{"label": "mouseCell", "pattern": "细胞"},
{"label": "mouseCell", "pattern": "小鼠"},
{"label": "mouseCell", "pattern": "大鼠"},
{"label": "mouseCell", "pattern": "幼鼠"},
{"label": "mouseCell", "pattern": "白兔"},
{"label": "mouseCell", "pattern": "体外"},
{"label": "singDbl", "pattern": "单用"},
{"label": "useMethod", "pattern": "注射"},
{"label": "useMethod", "pattern": "切片"},
{"label": "useMethod", "pattern": "饮用"},
{"label": "useMethod", "pattern": [{"TEXT": {"REGEX":'(\d+)\s*(mg/kg|g/kg|μmol/L|mg/ml)'}}]}]
ruler = nlp.add_pipe("entity_ruler")
ruler.add_patterns(patterns)
df = pd.DataFrame()
for i in range(101,126):
	rpath = "./cleantrain/"+str(i) + ".txt"
	file = open(rpath,'r',encoding = 'utf-8')
	txt = file.read()
	doc = nlp(txt)
	# print(doc.ents)
	i = 0
	j =0

	# tempDict = {"rs":[],"rsRx":[],"singDbl":[],"mouseCell":[],"nummouse":[],"inoutbody":[],"useMethod":[],"period":[],"numrs":[],"disease":[],"incre":[],"decre":[],"title":[],"result":[],"time":[]}
	dictlabels = {"rs":[],"rsRx":[],"singDbl":[],"mouseCell":[],"nummouse":[],"inoutbody":[],"useMethod":[],"period":[],"numrs":[],"disease":[],"incre":[],"decre":[],"title":[],"result":[],"time":[]}
	for ent in doc.ents:
		if ent.label_ in dictlabels.keys():
			dictlabels[ent.label_].append(ent.text)
	    # tempDict[ent.label_].append(ent)
	dfTemp = validation.getResult(dictlabels)
	df = pd.concat([df,dfTemp],axis = 0)
df.to_excel('./vali_ru.xlsx')
trueArr = pd.read_excel('./valiTrue.xlsx').values
eva(trueArr)