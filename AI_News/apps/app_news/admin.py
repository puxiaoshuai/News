from django.contrib import admin

# Register your models here.
from app_news.models import News, Comment,UserProfile,NewsTag
admin.site.register(UserProfile)
admin.site.register(NewsTag)
admin.site.register(News)
admin.site.register(Comment)

