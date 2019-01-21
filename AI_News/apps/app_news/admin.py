from django.contrib import admin

"""
'''设置列表可显示的字段'''
    list_display = ('title', 'author',  'status', 'mod_date',)
    '''设置过滤选项'''
    list_filter = ('status', 'pub_date', )
    '''每页显示条目数'''
    list_per_page = 5
    '''设置可编辑字段'''
    list_editable = ('status',)
    '''按日期月份筛选'''
    date_hierarchy = 'pub_date
    '''按发布日期排序'''
    ordering = ('-mod_date',)
"""
from app_news.models import News, Comment, UserProfile, NewsTag, DuanziModel


class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'newstag')


class DuanziAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'user')


class NewTagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'news', 'user')
    # 这是增加链接,和edit不能同时出现
    list_display_links = ('text', 'news', 'user')
    # list_editable = ['text', 'news', 'user']


admin.site.register(UserProfile)
admin.site.register(NewsTag, NewTagAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(DuanziModel, DuanziAdmin)