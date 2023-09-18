import json
import pandas as pd
import test
"""
this file is to generate true validation label file
"""
# oib to json v1
# read bio
# {"text":"content od txt","entities":[{"label":"lbName","start_offset":num,"end_offset":num},{}]}
def BioToJson(infile):
    js = {}
    txt = ""
    f = open(infile,'r',encoding='utf-8')
    lines = f.readlines()
    start = 0
    end = 0
    flag = True
    ents = []
    ent = {}
    tempStr = ""
    tempLabel = ""
    dictlabels = {"rs":[],"rsRx":[],"singDbl":[],"mouseCell":[],"nummouse":[],"inoutbody":[],"useMethod":[],"period":[],"numrs":[],"disease":[],"incre":[],"decre":[],"title":[],"result":[],"time":[]}

    for line in lines:
        if line != '\n':
            word,tag = line.split(' ')
            # "text":"whole txt"
            word = word.replace('\t'," ")
            word = word.replace('\u3000'," ")
            txt = txt + word
            # "entities":[{*},{*}]
            #* {"label":"labelName","start_offset":num,"end_offset":num}
            tag = tag.replace("\n","")
            if tag == 'O':
                BIO = tag
            else:
                BIO,label = tag.split("-")
                # label = FindLabel(label)
            if BIO == 'B':
                # not the first b in file
                if flag == False:
                    dictlabels[ent["label"]].append(tempStr)
                    ent["end_offset"] = end+1
                    ents.append(ent)
                    ent = {}
                    
                else:
                    flag = False

                ent["label"] = label
                ent["start_offset"] = start
                tempStr = word

            elif BIO == 'I':
                end = start
                tempStr = tempStr + word

            start = start + 1            
    if BIO != 'B':
        dictlabels[ent["label"]].append(tempStr)
        ent["end_offset"] = end+1
        ents.append(ent)
        # js = {"text":txt,"entities":ents}
    # out = open(outfile,'w',encoding='utf-8')
    # json.dump(js,out)
    return dictlabels


df = pd.DataFrame([])
for i in range(101,126): 
    infile = './trainann/'+str(i)+'.txt.bio'
    tempDic = BioToJson(infile)
    tempDf = test.getResult(tempDic)
    df = pd.concat([df,tempDf],axis=0)
df.to_excel('./valiTrue.xlsx')



# dfD.to_excel("./disease.xlsx")
# dfR.to_excel("./rsrx.xlsx")