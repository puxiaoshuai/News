"""AI_News URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

# from app_news.views_base import NewsListView
from rest_framework.routers import DefaultRouter
from app_news.views import NewsListViewset
from app_news.mytest.views import  NewS

router = DefaultRouter()
router.register('news', NewsListViewset)
# news_list=NewsListViewset.as_view({
#     'get':'list',
# })

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('news/', NewsListView.as_view(),name="news_list"),
    path('', include(router.urls)),
    #path('test1/', news_list1),
    path('test1/', NewS.as_view()),
    # path('news/', news_list,name="news_list"),
    path('api-auth/', include('rest_framework.urls'))
]
