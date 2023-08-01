""" 
Transcribing Youtube Videos
Creator: Ethan Liu
"""
from youtube_transcript_api import YouTubeTranscriptApi as ytta
from ytvideo import Ytvideo
import json
import os


cid = 'UCVjlpEjEY9GpksqbEesJnNA' 

class Scribe(Ytvideo):
    """ A class to acquire captions for videos """
    
    def get_captions(self,channel_name: str,limit: int)->dict:
        """ Retrieve captions for videos """
        ids = super().get_id(channel_name)
        res = {'ID':[],
                    'Captions':[],
                    'WordCount':[]
                    }
        for i in ids[:limit]:
            try: 
                transcript = ytta.get_transcript(i)
                t_str = ''
                for line in transcript:
                    t_str += line['text']+' '
            except:
                t_str = None
            res['ID'].append(i)
            res['Captions'].append(t_str)
            if t_str == None:
                res['WordCount'].append(0)
            else:
                res['WordCount'].append(len(t_str))
              
        return res
    
    def save_captions(self,channel_name: str,limit: int) ->None:
        """ Saves captions as json, returns bool check of file exist """ 
        captions = self.get_captions(channel_name,limit)
        with open('captions.json','w') as outfile:
            json.dump(captions,outfile)
        return print(f"Checking File Existence: {os.path.isfile('captions.json')}")

