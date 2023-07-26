""" YOUTUBE API Data Retrieval 
Creator: Ethan Liu
Last Updated: 26/07/23
"""
from googleapiclient.discovery import build
from youtube_transcript_api import YouTubeTranscriptApi as ytt

class Yt:
    """ A class for retrieving raw data from youtube API """ 
    def __init__(self):
        self.name = 'youtube'
        self.service = 'v3'
        self.api_key = 'AIzaSyDMg2PyJVlG9sj79VXnlffmlD86wEHzXxI'
    
    def _start(self) -> object:
        """ Returns youtube service object """ 
        return build(self.name,self.service,developerKey=self.api_key)
    
    def channel_info(self,id: str) -> dict:
        """ Retrieves  basic channel statistics """ 
        yt = self._start()
        request = yt.channels().list(
        part='statistics,contentDetails',
        id = id
        )
        return request.execute()
    
    def get_videos(self,channel_name: str) -> list:
        """ Retrieves all video ids from a channel """ 
        playlist_id = self.channel_info(channel_name)['items'][0]['contentDetails']['relatedPlaylists']['uploads'] # get playlist id
        yt = self._start() # build service
        res = yt.playlistItems().list(
            playlistId = playlist_id,
            part=['snippet'],
            maxResults=50
        )
        # videos = []
        # next_page_token = None
        # while True:
        #     res = yt.playlistItems().list(
        #         playlistId=playlist_id,
        #         part=["id"],
        #         maxResults=50,
        #         pageToken = next_page_token
        #     ).execute()
            
        #     videos += res['items']
        #     next_page_token = res.get('nextPageToken')
            
        #     if next_page_token is None:
        #         break
            
        return res.execute()
        

cid = 'UCVjlpEjEY9GpksqbEesJnNA' 
e = Yt()
res=e.get_videos(cid)
print(res['items'][0]) 