"""
ETL of caption and video info data
"""
import pandas as pd
import json 
import os

cid = 'UCVjlpEjEY9GpksqbEesJnNA' 

class EtlMetaData:
    """ A class to etl all of the metadata of videos as well as their captions """
    
    def get_vdf(self,video_info: dict) -> pd.DataFrame:
        """ ETL video data as dataframe """
        df = pd.DataFrame(video_info)
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
            
    def transform_vdf(self,video_info: str) -> pd.DataFrame:
        """ Transform data type and add features in videos info dataframe """ 
        df = self.get_vdf(video_info)
        #change types 
        df = df.astype({'Title':'str','ID':'str','Duration':'str'})
        df[['Views','Likes','Comments']] = df[['Views','Likes','Comments']].apply(pd.to_numeric)
        #add useful metrics 
        df['LikesPerView'] = df['Likes']/df['Views']
        df['CommentsPerView'] = df['Comments']/df['Views']
        df['LikesPerComment'] = df['Likes']/df['Comments']
        return df
    
    def transform_tdf(self,source: any) -> pd.DataFrame:
        """ transform and add features in video transcript dataframe """
        #tdf can be from json or dict 
        if type(source) != str:
            df = self.get_tdf(source)
        else:
            if '.json' in source and type(source) == str:
                df = self.get_jtdf(source)
            else:
                return print('DataFrame Source Not Supported')
        #change data type
        df = df.astype({'WordCount':'int'})
        return df
    
    def export_df(self,video_info: str,source: str,save: bool) -> pd.DataFrame:
        """ combines video info and captions dataframe into one and saves as csv """
        vdf = self.transform_vdf(video_info)
        tdf = self.transform_tdf(source)
        df = pd.concat([vdf,tdf],axis=1)
        
        if save == True:
            df.to_csv('df')
            print(os.path.isfile('df.csv'))
        
        return df 

