from django.db import models

# Create your models here.

class youtube_app_channel_data_1(models.Model):
    ID = models.TextField()
    Title = models.TextField()
    Duration = models.TextField()
    Views = models.BigIntegerField()
    Likes = models.BigIntegerField()
    Comments = models.BigIntegerField()
    LikesPerView = models.FloatField()
    CommentsPerView = models.FloatField()
    LikesPerComment = models.FloatField()
    