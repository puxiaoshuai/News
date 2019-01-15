from django.contrib import admin

# Register your models here.
from app_news.models import News, Comment

admin.site.register(News)
admin.site.register(Comment)

