"""
File for NER functionality 

"""
from transformers import pipeline
import pandas as pd
import torch
import json
import os
from transformers import AutoTokenizer, AutoModelForTokenClassification
import ast

class NER:
    """ A class for performing Bert-Base Named Entity Recognition """
    def prepdata(self,source: any) ->dict[str:str]:
        """ Prepares data to be summarised"""
        if type(source) == str:
            return pd.read_csv(source)['Captions']
        elif type(source) == pd.DataFrame:
            return source['Captions']
        else:
            print('Data source not supported')
    
    def prepmodel(self) -> object:
        """ creates model object """ 
        tokenizer = AutoTokenizer.from_pretrained("dslim/bert-base-NER")
        model = AutoModelForTokenClassification.from_pretrained("dslim/bert-base-NER")
        nlp = pipeline('ner',model=model, tokenizer=tokenizer)
        return nlp
    
    def savej(self,data: any) -> None:
        """ saves NER output as json """
        with open('ner_results.json','w') as f:
            json.dump(data,f)
        return os.path.isfile('ner_results.json')
    
    def ner(self,source: any, limit = int) -> dict[str:list]:
        """ performs NER """
        data = self.prepdata(source)
        model = self.prepmodel()
        res = {'NER':[]}
        if limit == -1:
            n = len(data)
        else:
            n = limit
        
        for i in range(n):
            nres = model(data[i])
            res['NER'].append(str(nres))
            
        # save nlp output as json
        self.savej(res)
        return res

# e = NER()
# e.ner('df.csv',1)

with open('ner_results.json','r') as f:
    data = json.load(f)

print(type(data))
print(data.keys())
print(type(data['NER']))
print(len(data['NER']))
entry = data['NER']
print(entry)
d = entry[0]
print(type(d))
dlist = ast.literal_eval(d)
print(type(dlist))
print(type(dlist[0]))
