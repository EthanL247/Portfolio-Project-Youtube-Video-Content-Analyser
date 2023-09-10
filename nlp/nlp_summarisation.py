"""
NLP: Text Summary Process
Creator: Ethan Liu

"""
from transformers import pipeline
import pandas as pd
import torch
import json
import os



class Summariser:
    """ class for summarising video captions """
    
    def __init__(self)-> None:
        """ parameters to import hugging face obj """
        self.task = 'summarization'
        self.model = 'facebook/bart-large-cnn'
        
    
    def prepdata(self,source: any) ->dict[str:str]:
        """ Prepares data to be summarised"""
        if type(source) == str:
            return pd.read_csv(source)['Captions']
        elif type(source) == pd.DataFrame:
            return source['Captions']
        else:
            print('Data source not supported')
            
            
    def prep_model(self) -> object:
        """ creates longt5 model object """
        summariser = pipeline(
            'summarization',
            'pszemraj/long-t5-tglobal-base-16384-book-summary',
            device=0 if torch.cuda.is_available() else -1,
        )
        return summariser 
    
    def save(self, data:dict[list]) -> None:
        """ saves NER output as json """
        with open('sum_results.json','w') as f:
            json.dump(data,f)
        return os.path.isfile('ner_results.json')
        
            
    def summarise(self,source: any, limit: int,save=False) -> dict[int:list]:
        """ performs the summarisation """
        res = {'Summarised_Captions':[]}
        data = self.prepdata(source)
        summariser = self.prep_model()
        if limit == -1:
            n = len(data)
        else:
            n = limit
        for i in range(n):
            s = summariser(data[i])
            res['Summarised_Captions'].append(s)
            print(f"job {i} done.")
        
        if save == True:
            self.save(res)
        
        return res 
    
    
    


