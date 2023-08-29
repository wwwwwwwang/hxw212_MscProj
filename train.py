#0
import json
import spacy
from spacy.tokens import Doc
from spacy.tokens import Span
from spacy.training import Example
from spacy import displacy

#1
#nlp = spacy.load("zh_core_web_sm")#spacy.blank('zh')
nlp = spacy.load("zh_core_web_sm")
cfg = {"segmenter": "pkuseg"}
nlp.tokenizer.initialize(pkuseg_model="spacy_ontonotes")
if 'ner' not in nlp.pipe_names:
    ner = nlp.create_pipe('ner')
    nlp.add_pipe('ner', last=True)
else:
    ner = nlp.get_pipe( "ner" ) 
# add label name from labels.txt
labelFile = open('labels.txt','r',encoding='utf-8')
labels = labelFile.readlines()
for label in labels:
    ner.add_label(label)

# from labeled jsonl file build train data
f = open('labeled.jsonl', 'r', encoding="utf-8")
lines = f.readlines()
trainData = []
for data in lines:
    jdata = json.loads(data)
    text = jdata['text']
    ents = jdata['entities'] # list
    entity_list = []
    for ent in ents:
        entity_list.append([ent['start_offset'],ent['end_offset'],ent['label']])
    # data = (text,{'entities':ents})
    doc = nlp.make_doc(text)
    # print(entity_list)
    example = Example.from_dict(doc,{"entities":entity_list})
    trainData.append(example)

# print(trainData)

# get names of other pipes to disable them during training
other_pipes = [pipe for pipe in nlp.pipe_names if pipe != 'ner']
with nlp.disable_pipes(*other_pipes):  # only train NER
    optimizer = nlp.initialize()
    for itn in range(20):
        print("Statring iteration " + str(itn))
        random.shuffle(trainData)
        losses = {}
        nlp.update(
            trainData,
            drop=0.35,  # dropout - make it harder to memorise data
            sgd=optimizer,  # callable to update weights
            losses=losses)
        print(losses)