"""
NLP: Text Summary Process
Creator: Ethan Liu

"""
from scribe import Scribe
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
        
            
    def summarise(self,data: pd.DataFrame, limit: int) -> dict[int:list]:
        """ performs the summarisation """
        res = {'Summarised_Captions':[]}
        summariser = self.prep_model()
        if limit == 0:
            n = len(data)
        else:
            n = limit
        for i in range(n):
            s = summariser(data[i])
            res['Summarised_Captions'].append(s)
            
        # save to json
        with open('summarised_captions.json','w') as j:
            json.dump(res,j)
        print(os.isfile('summarised_captions.json'))
        
        return res 
    
          
    
e = Summariser()
data = e.prepdata('df.csv')
summarised = e.summarise(data,1)

