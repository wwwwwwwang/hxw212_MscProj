import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import spacy
import json
# import seaborn as sns



def SaveNerHtml(name):
	colors = {"rs":"#FF88C2","rsRx":"#FF8888","singDbl":"#FFBB66","mouseCell":"#FFFF77","nummouse":"#DDFF77","inoutbody":"#66FF66"
,"useMethod":"#77FFEE","period":"77DDFF","numrs":"#99BBFF","disease":"#9999FF","incre":"#D1BBFF","decre":"#D28EFF",
"title":"#FF77FF","result":"#EEFFBB","time":"#FF0088"}
	options = {"ents": ["rs","rsRx","singDbl","mouseCell","nummouse","inoutbody","useMethod","period","numrs","disease","incre","decre","title","result","time"], "colors": colors}
	html = spacy.displacy.render(doc, style="ent",jupyter = False,options=options)
	f = open('./tempHtml/'+name+'.txt','w',encoding='utf-8')
	f.write(html)
	f.close()


# def CalSim(lEnts):
# 	l = len(lEnts)
# 	if l <=1:
# 		return 0
# 	arr = np.empty([l,l])
# 	i = 0
# 	j = 0
# 	for e in lEnts:
# 		print(e.text)
# 		j = 0
# 		for e1 in lEnts:
# 			arr[i][j] = e.similarity(e1)
# 	hp = sns.heatmap(arr).invert_yaxis()
# 	plt.savefig('./temp/'+e.label_+'.png')
def getResult(dictlabels):
	finalResult = {}
	for key in dictlabels:
		value = dictlabels[key]
		if key == 'result':
			tempStr = ""
			for v in value:
				tempStr = tempStr + v
			finalResult[key] = tempStr
			continue
		if value == []:
		    finalResult[key] = value
		    continue
		tempFirstValue = value[0]
		tempMaxValue = [0,"",""]
		tempSet = set(value)
		if key == 'incre' or key =='decre':
			tempStr = ""
			for v in tempSet:
				tempStr = tempStr + v + " "
			finalResult[key] = tempStr
			continue
		for s in tempSet:
			num = value.count(s)
			if num>tempMaxValue[0]:
				tempMaxValue[0] = num
				tempMaxValue[2] = tempMaxValue[1]
				tempMaxValue[1] = s
		if key == "rsRx" and tempMaxValue[1] in tempFirstValue:
			finalResult[key] = tempFirstValue
		else:
			finalResult[key] = tempMaxValue[1]
	if finalResult['singDbl'] == []:
		finalResult['singDbl'] = '单用'
	if finalResult['inoutbody'] == []:
		if finalResult['mouseCell'] == '细胞':
			finalResult['inoutbody'] = "体外"
		else:
			if 'useMethod' == '切片':
				finalResult['inoutbody'] = "体外"
			else:
				finalResult['inoutbody'] = "体内"
	if key == "rsRx" and 'Rg' in finalResult[key]:
		finalResult[key] = "人参皂苷"+finalResult[key]
	for key in finalResult:
		if finalResult[key] == []:
			finalResult[key] = ""
	df = pd.DataFrame(finalResult, index=[0])
	return df

def runModel(txt):
	nlp1 = spacy.load("./temp/final")
	# doc = nlp(txt)
	doc = nlp1(txt)
	# print(doc.ents)
	i = 0
	j =0

	tempDict = {"rs":[],"rsRx":[],"singDbl":[],"mouseCell":[],"nummouse":[],"inoutbody":[],"useMethod":[],"period":[],"numrs":[],"disease":[],"incre":[],"decre":[],"title":[],"result":[],"time":[]}
	dictlabels = {"rs":[],"rsRx":[],"singDbl":[],"mouseCell":[],"nummouse":[],"inoutbody":[],"useMethod":[],"period":[],"numrs":[],"disease":[],"incre":[],"decre":[],"title":[],"result":[],"time":[]}
	for ent in doc.ents:
		dictlabels[ent.label_].append(ent.text)
	    # tempDict[ent.label_].append(ent)
	df = getResult(dictlabels)
	# for key in tempDict:
		# if tempDict != []:
			# print(key)
			# CalSim(tempDict[key])
	return df
def runModelHtml(txt):
	nlp1 = spacy.load("./temp/final")
	# doc = nlp(txt)
	doc = nlp1(txt)
	# print(doc.ents)
	i = 0
	j =0

	tempDict = {"rs":[],"rsRx":[],"singDbl":[],"mouseCell":[],"nummouse":[],"inoutbody":[],"useMethod":[],"period":[],"numrs":[],"disease":[],"incre":[],"decre":[],"title":[],"result":[],"time":[]}
	dictlabels = {"rs":[],"rsRx":[],"singDbl":[],"mouseCell":[],"nummouse":[],"inoutbody":[],"useMethod":[],"period":[],"numrs":[],"disease":[],"incre":[],"decre":[],"title":[],"result":[],"time":[]}
	for ent in doc.ents:
		dictlabels[ent.label_].append(ent.text)
	    # tempDict[ent.label_].append(ent)
	df = getResult(dictlabels)
	# for key in tempDict:
		# if tempDict != []:
			# print(key)
			# CalSim(tempDict[key])
	colors = {"rs":"#FF88C2","rsRx":"#FF8888","singDbl":"#FFBB66","mouseCell":"#FFFF77","nummouse":"#DDFF77","inoutbody":"#66FF66","useMethod":"#77FFEE","period":"77DDFF","numrs":"#99BBFF","disease":"#9999FF","incre":"#D1BBFF","decre":"#D28EFF","title":"#FF77FF","result":"#EEFFBB","time":"#FF0088"}
	options = {"ents": ["rs","rsRx","singDbl","mouseCell","nummouse","inoutbody","useMethod","period","numrs","disease","incre","decre","title","result","time"], "colors": colors}
	html = spacy.displacy.render(doc, style="ent",jupyter = False,options=options)
	f = open('./temp/h.html','w',encoding = 'utf-8')
	f.write(html)
	f.close()
	return df

def main():
	df = pd.DataFrame()
	for i in range(1,91):
		rpath = "./cleantest/"+str(i) + ".txt"
		file = open(rpath,'r',encoding = 'utf-8')
		txt = file.read()
		dfTemp = runModel(txt)
		df = pd.concat([df,dfTemp],axis = 0)
	df.to_excel('./testResult.xlsx')

if __name__ == '__main__':
	main()