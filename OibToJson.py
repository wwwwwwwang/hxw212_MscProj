import json
import pandas as pd
import test

# oib to json v1
# read bio
# {"text":"content od txt","entities":[{"label":"lbName","start_offset":num,"end_offset":num},{}]}
def BioToJson(infile,outfile):
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
    # dictlabels = = {"rs":[],"rsRx":[],"singDbl":[],"mouseCell":[],"nummouse":[],"inoutbody":[],"useMethod":[],"period":[],"numrs":[],"disease":[],"incre":[],"decre":[],"title":[],"result":[],"time":[]}
    # disease = set([])
    # rsrx = set([])
    # dis = ""
    # rs = ""
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
                    
                    # if label == "物质名称":
                    #     rsrx.add(rs)
                    #     rs = word
                    # elif label == "ICD-11名称":
                    #     disease.add(dis)
                    #     dis = word
                else:
                    flag = False

                ent["label"] = label
                ent["start_offset"] = start
                tempStr = word

                # if label == "物质名称":
                #     rs = word
                # elif label == "ICD-11名称":
                #     dis = word
            elif BIO == 'I':
                end = start
                tempStr.append(word)
                # if label == "物质名称":
                #     rs = rs + word
                # elif label == "ICD-11名称":
                #     dis = dis +word
            start = start + 1            
    if BIO != 'B':
        ent["end_offset"] = end+1
        ents.append(ent)
        dictlabels.
        js = {"text":txt,"entities":ents}
    out = open(outfile,'w',encoding='utf-8')
    json.dump(js,out)
    return list(disease),list(rsrx)

dfD = pd.DataFrame()
dfR = pd.DataFrame()
for i in range(1,71):
    
    infile = './trainann/'+str(i)+'.txt.bio'
    outfile = './trainjson/'+str(i)+'.json'
    d,r = BioToJson(infile,outfile)
    ddf = pd.DataFrame({int(i)-1:d})
    ddr = pd.DataFrame({int(i)-1:r})
    dfD = pd.concat([dfD,ddf],axis = 1)
    dfR = pd.concat([dfR,ddr],axis = 1)

    getResult(dictlabels)

# dfD.to_excel("./disease.xlsx")
# dfR.to_excel("./rsrx.xlsx")