"""
Youtube Data ETL
Creator: Ethan Liu
"""
from ytvideo import Ytvideo
from ytchannel import Ytchannel
import pandas as pd
from scribe import Scribe
import json 
import os

cid = 'UCVjlpEjEY9GpksqbEesJnNA' 

class Etl(Ytvideo):
    """ A class to etl video data """
    
    def get_vdf(self,channel_name: str) -> pd.DataFrame:
        """ ETL video data as dataframe """
        data = super().get_vinfo(channel_name)
        df = pd.DataFrame(data)
        return df
    
    def get_tdf(self,transcripts: dict[str:list]) -> pd.DataFrame:
        """ ETL video caption data as dataframe """ 
        return pd.DataFrame.from_dict(transcripts,orient='index').transpose()
    
    def get_jtdf(self,json_file: json) -> pd.DataFrame:
        """ ETL Json video caption data as dataframe """
        try: 
            with open(json_file) as j:
                data = json.load(j)
            return pd.DataFrame.from_dict(data,orient='index').transpose()
        except FileNotFoundError:
            print("Json File Not Found")
            
    def transform_vdf(self,channel_name: str) -> pd.DataFrame:
        """ Transform data type and add features in videos dataframe """ 
        df = self.get_vdf(channel_name)
        #change types 
        df = df.astype({'Title':'str','ID':'str','Duration':'str'})
        df[['Views','Likes','Comments']] = df[['Views','Likes','Comments']].apply(pd.to_numeric)
        #add useful metrics 
        df['LikesPerView'] = df['Likes']/df['Views']
        df['CommentsPerView'] = df['Comments']/df['Views']
        df['LikesPerComment'] = df['Likes']/df['Comments']
        return df
    
    def transform_tdf(self,source: str) -> pd.DataFrame:
        """ transform and add features in video transcript data frame """
        #tdf can be from json or dict 
        if type(source) == dict:
            df = self.get_tdf(source)
        if '.json' in source:
            df = self.get_jtdf(source)
        else:
            return print('DataFrame Source Not Supported')
        #change data type
        df = df.astype({'WordCount':'int'})
        return df
    
    def format_df(self,channel_name: str,source: str,save: bool) -> pd.DataFrame:
        vdf = self.transform_vdf(channel_name)
        tdf = self.transform_tdf(source)
        df = pd.concat([vdf,tdf],axis=1)
        
        # drop all empty indexs due to restricted subtitles 
        df.dropna(inplace=True)
        
        if save == True:
            df.to_csv('df')
            print(os.path.isfile('df.csv'))
        
        return df 

