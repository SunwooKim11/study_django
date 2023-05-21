from django.shortcuts import render
from rest_framework.views import APIView
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

from .models import *
from django.core.wsgi import get_wsgi_application


class Main(APIView):
    def get(self, request="GET"):
        feed_list = Feed.objects.all().order_by('-id') # query set select * from feed_list
        recommend_list = Recommend.objects.all().order_by('-id')
        #for feed in feed_list:
        #    print(feed.contents())

        return render(request, 'main.html', context=dict(feeds=feed_list, recommends=recommend_list))
    
class Test(APIView):
    def get(self, request):
        return render(request, 'test.html')

if __name__ =="__main__":   
    obj = Main()
    obj.get()