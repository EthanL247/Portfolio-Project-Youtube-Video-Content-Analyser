from django.shortcuts import render
from youtube_app.models import youtube_app_channel_data_1

# Create your views here.

def get_data(request):
    mydata = youtube_app_channel_data_1.objects.all()
    context = {
        'mydata': mydata
    }
    return render(request, 'get_data.html',context)