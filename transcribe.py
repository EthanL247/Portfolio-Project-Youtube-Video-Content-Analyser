""" 
For Transcriping Youtube videos
Creator: Ethan Liu
Last Updated: 26/07
"""
from yt import Yt
from youtube_transcript_api import YouTubeTranscriptApi as YTT
import pandas as pd
from googleapiclient.discovery import build

class Scribe(Yt):
    """ A subclass for transcribing youtube video captions """
    def getid(self,channel_name: str) -> list:
        """ get all video ids """ 
        vdata = super().get_videos(channel_name)
        vid = [i['id'] for i in vdata]
        return vid

    def get_vinfo(self,channel_name) -> list:
        """ makes a video based data frame """ 
        ids = self.getid(channel_name)
        yt = super()._start()
        request = yt.videos().list(
                part="contentDetails,statistics,snippet,status",
                id =ids[1]
        )
        return request.execute()


cid = 'UCVjlpEjEY9GpksqbEesJnNA'  
        
        
        
        
            