"""
NLP: Text Summary Process
Creator: Ethan Liu

"""
from scribe import Scribe
from transformers import pipeline
import pandas as pd


class Summarise:
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
            
    def summarise(self,df: pd.DataFrame) -> pd.DataFrame:
        summariser = pipeline(self.task,model=self.model)
        data = df[0]
        res = summariser(data,max_length=130,min_length=30)
        return res 
        
        
        
        
    
e = Summarise()
data = e.prepdata('df.csv')
print(data)