from django.db import models


# Create your models here.

class News(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    body = models.TextField()
    img_url = models.CharField(max_length=200)
    tag = models.CharField(max_length=24)
    img_tv_url = models.CharField(max_length=120)
    tv_name = models.CharField(max_length=120)
    create_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-create_time']
        verbose_name = "新闻"
        verbose_name_plural = '新闻'
        db_table='news'


class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    text = models.TextField()
    create_time = models.DateTimeField(auto_now_add=True)
    news = models.ForeignKey('News',related_name='comment', on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = "评论"
        verbose_name_plural = '评论'
        db_table = 'comment'
