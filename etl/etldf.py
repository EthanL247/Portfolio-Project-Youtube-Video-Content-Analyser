""" A file for transforming etl data into dataframe"""
import pandas as pd
import psycopg2 as psy

class EtlDF:
    """ A class to carry convert data into dataframe """
    
    def meta_dataframe(self, metadata: dict[dict[list]]) -> pd.DataFrame:
        df = pd.DataFrame(metadata)
        
        #convert types 
        df = df.astype({'Title':'str','ID':'str','Duration':'str'})
        df[['Views','Likes','Comments']] = df[['Views','Likes','Comments']].apply(pd.to_numeric)
        #add useful metrics 
        df['LikesPerView'] = df['Likes']/df['Views']
        df['CommentsPerView'] = df['Comments']/df['Views']
        df['LikesPerComment'] = df['Likes']/df['Comments']
        0
        return df 
        
    
    