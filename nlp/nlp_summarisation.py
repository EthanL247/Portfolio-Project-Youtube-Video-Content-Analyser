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
        
            
    def summarise(self,source: any, limit: int) -> dict[int:list]:
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
            
        # save to json
        with open('summarised_captions.json','w') as j:
            json.dump(res,j)
        
        return res 
    
    def merge(self,main: str, summarised: str) -> pd.DataFrame:
        """ Merges captions with main dataframe """ 
        #local merge
        if type(main) == str and type(summarised) == str:
            main_df = pd.read_csv(main)
            summarised_df = pd.read_json(summarised)
            main = pd.concat([main_df,summarised_df],axis=1)
            # drop not needed features 
            main.drop([main.columns[0],'ID.1'],inplace=True,axis=1)
            return main 
        
        #adhoc merge 
        if type(main) == pd.Dataframe and type(summarised) == pd.Dataframe:
            main = pd.concat([main,summarised],axis=1)
            # drop not needed features 
            main.drop([main.columns[0],'ID.1'],inplace=True,axis=1)
            return main 
        else:
            print('Merge source not supported')
    
    


