""" 
File for performing sentiment analysis 
"""
from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline
import pandas as pd
import json
import os 

class SentimentAnalysis:
    """ a class for performing SamLowe/roberta-base-go_emotions sentiment analysis """
    
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
        tokenizer = AutoTokenizer.from_pretrained("SamLowe/roberta-base-go_emotions")
        model = AutoModelForSequenceClassification.from_pretrained("SamLowe/roberta-base-go_emotions")
        sa = pipeline("text-classification", model="SamLowe/roberta-base-go_emotions",truncation=True,return_all_scores=True)
        return sa
    
    def savej(self,data: any) -> None:
        """ saves sa output as json """
        with open('sa_results.json','w') as f:
            json.dump(data,f)
        return os.path.isfile('sa_results.json')
    
    
    def sa(self,source: any, limit: int) -> dict:
        """ performs sentiment analysis """ 
        data = self.prepdata(source)
        model = self.prepmodel()
        res = {'SA':[]}
        if limit == -1:
            n = len(data)
        else:
            n = limit
        
        for i in range(n):
            sares = model(data[i])
            res['SA'].append(str(sares))
            print(f"job: {i+1} /{n} done.")
        
        self.savej(res)
        return res 
        
        
    
        
    