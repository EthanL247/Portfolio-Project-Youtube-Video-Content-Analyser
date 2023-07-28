""" 
For retrieving video data
Creator: Ethan Liu
"""
from ytchannel import Ytchannel

class Ytvideo(Ytchannel):
    """ Class for retrieving video data """
    
    def get_id(self,channel_name: str) -> list[str]:
        """ gets all video ids """ 
        vdata = super().get_videos(channel_name)
        vid = [i['snippet']['resourceId']['videoId'] for i in vdata[:50]] #YoutubeAPILimit of 50 items
        return vid

    def get_v(self,channel_name: str) -> list:
        """ gets full video details from youtube""" 
        ids = self.get_id(channel_name)
        yt = super()._start()
        request = yt.videos().list(
                part="contentDetails,statistics,snippet,status",
                id =ids )
        
        return request.execute()
    
    def get_vinfo(self,channel_name: str) -> dict:
        """ retrieves and formats relevant video info"""
        data = self.get_v(channel_name)['items']
        d = {
            'ID':[],
            'Title':[],
            'Duration':[],
            'Views':[],
            'Likes':[],
            'Comments':[]
        }
    
        for i in data:
            d['ID'].append(i['id']),
            d['Title'].append((i['snippet']['title'])),
            d['Duration'].append(i['contentDetails']['duration']),
            d['Views'].append(i['statistics']['viewCount']),
            d['Likes'].append(i['statistics']['likeCount']),
            d['Comments'].append(i['statistics']['commentCount']),

        return d


# cid = 'UCVjlpEjEY9GpksqbEesJnNA'  
# e = Ytvideo()
# v = e.get_vinfo(cid)
# print(v['Views'])