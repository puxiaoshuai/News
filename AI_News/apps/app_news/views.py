from django.shortcuts import render,HttpResponse

# Create your views here.
from app_news.models import News


def hello(request):
    print(News.objects.all())
    return HttpResponse("你好")

