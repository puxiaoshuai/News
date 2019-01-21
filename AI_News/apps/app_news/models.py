from django.db import models
from django.contrib.auth.models import AbstractUser
import json


# Create your models here.

class UserProfile(AbstractUser):
    nick_name = models.CharField(max_length=50, verbose_name="昵称", default="")
    gender = models.CharField(max_length=6, choices=(('male', '男'), ('female', '女')), default='female',
                              verbose_name='性别')

    class Meta:
        verbose_name = "用户"
        verbose_name_plural = '用户'
        db_table = 'userprofile'


class NewsTag(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = "新闻分类"
        verbose_name_plural = '新闻分类'
        db_table = 'news_tag'

    def __str__(self):
        return self.name


class News(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    body = models.TextField()
    img_url = models.CharField(max_length=200)
    newstag = models.ForeignKey('NewsTag', related_name='news', on_delete=models.DO_NOTHING)
    img_tv_url = models.CharField(max_length=120)
    tv_name = models.CharField(max_length=120)
    create_time = models.DateTimeField(auto_now_add=True)
    time_tv = models.CharField(max_length=20, default="")

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-create_time']
        verbose_name = "新闻"
        verbose_name_plural = '新闻'
        db_table = 'news'


# 这是新闻的评论
class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    # name = models.CharField(max_length=100,null=False)
    text = models.TextField()
    create_time = models.DateTimeField(auto_now_add=True)
    news = models.ForeignKey(News, related_name='news_comment', on_delete=models.DO_NOTHING)
    user = models.ForeignKey(UserProfile,related_name='user_comment', on_delete=models.CASCADE, default='', unique=False)

    def __str__(self):
        return self.text

    class Meta:
        ordering = ['-create_time']
        verbose_name = "评论"
        verbose_name_plural = '评论'
        db_table = 'comment'


# class DuanziModel(models.Model):
#     id = models.CharField(primary_key=True)
#     body = models.TextField()

