from django.shortcuts import render, HttpResponse
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView, status
from rest_framework.response import Response
# Create your views here.
from app_news.models import News
from .serialaizers import NewsSerializer
from rest_framework import mixins, generics
from rest_framework import viewsets
# 从django_filter中过滤
from django_filters.rest_framework import DjangoFilterBackend
from .filters import NewsFilter
# rest_framework自带的过滤器
from rest_framework.filters import SearchFilter, OrderingFilter


def hello(request):
    print(News.objects.all())
    return HttpResponse("Hello")


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    # page_query_param = 'p'
    max_page_size = 20


# https://q1mi.github.io/Django-REST-framework-documentation/api-guide/generic-views_zh/#_1
# ListModelMixin提供一个 .list(request, *args, **kwargs) 方法，实现列出结果集。
# 如果查询集被填充了数据，则返回 200 OK 响应，将查询集的序列化表示作为响应的主体。相应数据可以任意分页

#继承了ListModeMixin，具有了分页过滤等功能
class NewsListViewset(mixins.ListModelMixin, viewsets.GenericViewSet):
    # 分页,搜索，过滤，排序的功能
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    # filter_fields = ('id', 'title')
    filter_class = NewsFilter
    search_fields = ('title', 'tag')
    ordering_fields = ('id', 'title')

#
# class NewsListView(generics.ListAPIView):
#     # 分页
#     queryset = News.objects.all()[:10]
#     serializer_class = NewsSerializer
#     pagination_class = StandardResultsSetPagination

# def get(self, request, *args, **kwargs):
#     return self.list(request, *args, **kwargs)

# class NewsListView(mixins.ListModelMixin, generics.GenericAPIView):
#     queryset = News.objects.all()[:10]
#     serializer_class = NewsSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

# def get(self, request):
#     news = News.objects.all()[:10]
#     serializer = NewsSerializer(news, many=True)
#     return Response(serializer.data)
# def post(self,request):
#     serializer=NewsSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return  Response(serializer.data,status=status.HTTP_200_OK)
#     return  Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
