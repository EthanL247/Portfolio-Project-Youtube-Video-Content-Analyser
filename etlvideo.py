"""
Youtube Data ETL
Creator: Ethan Liu
Last Updated:26/07/23

"""
from ytvideo import Ytvideo
from ytchannel import Ytchannel
import pandas as pd

cid = 'UCVjlpEjEY9GpksqbEesJnNA' 

class Etl(Ytvideo):
    """ A class to etl video data """
    
    def get_df(self,channel_name):
        data = super().get_vinfo(channel_name)
        df = pd.DataFrame(data)
        return df


