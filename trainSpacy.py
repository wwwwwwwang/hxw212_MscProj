import random
import json
import spacy
from spacy.tokens import Doc
from spacy.tokens import Span
from spacy.training import Example
from spacy import displacy
from spacy.pipeline import EntityRuler
from spacy.training import iob_to_biluo
from spacy.training import biluo_tags_to_spans

nlp = spacy.load("zh_core_web_lg")

def FindTrain():
    train = []
    temp = 0
    stopWord = set()
    words = set(nlp.vocab.strings)
    for i in range(1,101):
        labels = []
        txt = ""
        f = open("./trainann/"+str(i)+".txt.bio",'r',encoding = 'utf-8')
        lines = f.readlines()
        for line in lines:
            if line != '\n':
                word,tag = line.split(' ')
                word = word.replace('\t',"")
                word = word.replace('\u3000',"")
                tag = tag.replace("\n","")
                # stop_words = (lex for lex in nlp.vocab if lex.is_stop)
                # if nlp.vocab[word].is_stop == True:# in nlp.vocab.is_stop:
                    # s.add(word)
                # if word not in words:
                #     stopWord.add(word)
                if word != "" and tag != "":#and word not in stopWord:
                    txt = txt + word
                    labels.append(tag)
        # print(labels)
        biluo_tags = iob_to_biluo(labels)
        # print(len(biluo_tags))
        # print(len(txt))
        # nlp1 = spacy.blank("zh")
        space = []
        for t in txt:
            space.append(False)
        doc = Doc(nlp.vocab, words=txt, spaces=space)
        # print(txt)
        # print('\n')
        # print(doc)
        # print(len(doc))
        # solve doc and txt have different length
        entities = biluo_tags_to_spans(doc, biluo_tags)
        temp = {}
        temp["words"]=txt
        temp["entities"]=entities
        train.append(temp)
    # print(stopWord)
    return train

from spacy.scorer import Scorer
def evaluate(trainedModel,traindata):
    scorer = Scorer()
    examples = []
    for entities in trainData:
        text = entities['words']
        doc = nlp.make_doc(text)
        example = Example.from_dict(doc, entities)
        txt = entities['words']
        example.predicted = trainedModel(txt)
        examples.append(example)
    scoreEnt = scorer.score_spans(examples,"ents")
    return scoreEnt

#spacy.blank('zh')
if 'ner' not in nlp.pipe_names:
    ner = nlp.create_pipe('ner')
    nlp.add_pipe('ner', last=True)
else:
    ner = nlp.get_pipe("ner") 
# add label name from labels.txt
labelFile = open('labels.txt','r',encoding='utf-8')
labels = labelFile.readlines()
for label in labels:
    ner.add_label(label)

patterns = [#{"label": "rsRx","pattern": "人参总皂苷"},
# {"label": "rsRx","pattern": "人参皂苷Rg3"},
# {"label": "rsRx","pattern": "人参皂苷Re"},
# {"label": "rsRx", "pattern": "人参皂苷Rg1"},
# {"label": "rsRx", "pattern": "人参皂苷Rg2"},
# {"label": "rsRx", "pattern": "人参皂苷Rg"},
# {"label": "rsRx", "pattern": "人参水煎液"},
# {"label": "rsRx", "pattern": "人参三醇类皂苷"},
# {"label": "rsRx", "pattern": "人参皂苷Ck"},
# {"label": "rsRx", "pattern": "人参提取物"},
# {"label": "rsRx", "pattern": "人参二醇类皂苷"},
# {"label": "rs", "pattern": "人参"},
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
# ruler = nlp.add_pipe("entity_ruler")
# ruler.add_patterns(patterns)

trainData = FindTrain()
# wordsForToken = ["人参","人参皂苷","人参皂苷Rg3","人参皂苷Rb","人参皂苷Rg1","人参皂苷Rg2","人参三醇类皂苷","人参二醇类皂苷","人参皂苷Ck","μmol·L"]
# nlp.tokenizer.pkuseg_update_user_dict(wordsForToken)

other_pipes = [pipe for pipe in nlp.pipe_names if pipe != 'ner']# and pipe !='entity_ruler']
with nlp.disable_pipes(*other_pipes):  # only train NER
    # optimizer = nlp.initialize()
    for itn in range(50):
        print("Statring iteration " + str(itn))
        random.shuffle(trainData)
        losses = {}
        for entities in trainData:
            text = entities['words']
            # print(text)
            doc = nlp.make_doc(text)
            example = Example.from_dict(doc, entities)
            nlp.update(
                [example],
                drop=0.1,  # dropout - make it harder to memorise data
                losses=losses)
        print(losses)

score = evaluate(nlp,trainData)
print("Precision: " + str(score["ents_p"]))
print("Recall:" +str(score["ents_r"]))
print("F-measure:"+ str(score["ents_f"]))

nlp.to_disk('./temp/100_50_0.1')

#0.2
#Precision: 0.8217696273134455
#Recall:0.6177890724269377
#F-measure:0.7053276756247052

"""
0.1
Precision: 0.833138953682106
Recall:0.6353875476493012
F-measure:0.7209486735870819
"""



# text = "Wang is a student at the University of Birmingham."
# # create a Doc object through a spaCy pretrained pipeline 
# doc = spaCyPipe(text) 

# for token in doc: # Doc contains a sequence of Token object
#     print(token.text) # output: 'Wang','is'...,'Birmingham','.'

# span = doc[6:9] # Span object is a slice of Doc object
# print(span.text) # output: University of Birmingham
# print(span.label_) # output: Organization



