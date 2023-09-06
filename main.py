from youtube_api.ytchannel import Ytchannel
from youtube_api.ytvideo import Ytvideo
from nlp.nlp_ner import NER
from etl.etlner import EtlNER
from youtube_api.transcribe import Transcribe

#initialising
channel_manage = Ytchannel()
video_manage = Ytvideo()
nlp_manage = NER()
etlner_manage = EtlNER()
scribe_manage = Transcribe()
id = 'UCVjlpEjEY9GpksqbEesJnNA'


#testing
video_location = channel_manage.get_videos(id)
videos_info = video_manage.export_info(video_location)
videos_captions = scribe_manage.get_captions(videos_info,1)
ner_raw = nlp_manage.ner(videos_captions,1)
ner_data = etlner_manage.direct_etl(ner_raw)
print(ner_data['PER'])
print(ner_data['ORG'])
print(ner_data['LOC'])
print(ner_data['MSC'])
