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
#运行脚本提供
import os, django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "AI_News.settings")

django.setup()

from django.contrib import admin
from django.urls import path, include

from app_news.api import NewsListView,RegisterView
from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token
router = DefaultRouter()
# router.register('news',NewsListViewset)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('news/', NewsListView.as_view()),
    path('register/', RegisterView.as_view()),
    path('api-auth/', include('rest_framework.urls')),
    path('login/', obtain_jwt_token),
]
