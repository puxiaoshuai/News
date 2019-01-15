from django.views.generic.base import View
# from  django.views.generic import ListView
from app_news.models import News
from django.http import HttpResponse, JsonResponse
# 2.种把类转成字典，datatime还是不能序列化
from django.forms.models import model_to_dict
# 3.使用serilaizers
from django.core import serializers

import json

"""
以下都是使用django功能原生实现，都有一定的弊端，serilaizeer格式固定
"""


class NewsListView(View):
    def get(self, request):
        """
        通过View实现新闻的列表页面, 这是传统的写法
        content_type='application/json'重要
        缺点很多：
        时间datatime等不能序列号
        :param request:
        :return:
        """
        json_list = []
        news = News.objects.all()[:10]
        # 1种
        # for new in news:
        #     json_dict = {'title': new.title, 'img_url': new.img_url}
        #     json_list.append(json_dict)
        # 2种
        # for new in  news:
        #     json_dict=model_to_dict(new)
        #     json_list.append(json_dict)
        # 3种
        json_data = serializers.serialize('json', news)  # 这是字符串
        print(json_data)
        json_msg = json.loads(json_data)
        # return HttpResponse(json.dumps(json_list), content_type='application/json')
        # return HttpResponse(json.dumps(json_msg), content_type='application/json')
        return JsonResponse(json_msg, safe=False)
