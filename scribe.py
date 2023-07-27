""" 
Transcribing Youtube Videos
Creator: Ethan Liu
Last Updated: 27/07/23
"""
from youtube_transcript_api import YouTubeTranscriptApi as ytta
from ytvideo import Ytvideo
import json


cid = 'UCVjlpEjEY9GpksqbEesJnNA' 

class Scribe(Ytvideo):
    """ A class to acquire captions for videos """
    
    def get_captions(self,channel_name):
        ids = super().get_id(channel_name)
        captions = {}
        for i in ids:
            try: 
                transcript = ytta.get_transcript(i)
                t_str = ''
                for line in transcript:
                    t_str += line['text']+' '
            except:
                t_str = None
            
            captions[i]=t_str
            
        return captions

e = Scribe()
i = e.get_captions(cid)
with open('transcript.json','w') as outfile:
    json.dump(i,outfile)

    