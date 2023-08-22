from youtube_api.ytchannel import Ytchannel
from youtube_api.ytvideo import Ytvideo
from youtube_api.transcribe import Transcribe
from youtube_api.etlvideo import Etl

c_object = Ytchannel()
v_object = Ytvideo()
transcribe = Transcribe()
etl = Etl()


videos = c_object.get_videos('UChBEbMKI1eCcejTtmI32UEw')
vinfo = v_object.export_info(videos)
captions = transcribe.get_captions(vinfo,2)

vdf = etl.transform_vdf(vinfo).iloc[:2]
jdf = etl.transform_tdf(captions)

df = etl.export_df(vinfo,captions,False)
