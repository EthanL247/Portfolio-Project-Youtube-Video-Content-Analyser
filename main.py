from youtube_api.ytchannel import Ytchannel
from youtube_api.ytvideo import Ytvideo
from nlp.nlp_ner import NER
from etl.etlner import EtlNER
from youtube_api.transcribe import Transcribe
from nlp.nlp_sa import SA
from etl.etlsa import EtlSA

#initialising
channel_manage = Ytchannel()
video_manage = Ytvideo()
nlp_ner = NER()
nlp_sa = SA()
etlner_manage = EtlNER()
scribe_manage = Transcribe()
etlsa_mange = EtlSA()
id = 'UCVjlpEjEY9GpksqbEesJnNA'


#testing
video_location = channel_manage.get_videos(id)
videos_info = video_manage.export_info(video_location)
videos_captions = scribe_manage.get_captions(videos_info,1)
saraw = nlp_sa.sa(videos_captions,1)
sares = etlsa_mange.direct_etl(saraw)
