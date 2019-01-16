from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from ..models import News
from ..serialaizers import NewsSerializer

###这是方法视图
# @api_view(['GET', 'POST'])
# def news_list1(request,format=None):
#     if request.method == 'GET':
#         news_lsit = News.objects.all()
#         serializer = NewsSerializer(news_lsit, many=True)
#         return Response(serializer.data)
#基于类视图

class NewS(APIView):
    def get(self, request, format=None):
        snippets = News.objects.all()
        serializer = NewsSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = NewsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


