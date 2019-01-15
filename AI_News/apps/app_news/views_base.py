from  django.views.generic.base import  View
#from  django.views.generic import ListView
class NewsListView(View):
    def get(self,request):
        """
        通过View实现新闻的列表页面
        :param request:
        :return:
        """