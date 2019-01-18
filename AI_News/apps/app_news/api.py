from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, mixins, status

from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.views import APIView
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from app_news.filters import NewsFilter
from .models import News, UserProfile
from .serialaizers import NewsSerializer, UserSerializer
from rest_framework.response import Response
from common.HttpResponseUtil import generate_response, ResponseCode, create_list_msg


# 1.构建序列化,导入进来了
# 2.编写视图,方法视图，类视图

# class StandardResultsSetPagination(PageNumberPagination):
#     page_size = 3
#     page_size_query_param = 'page_size'
#     # page_query_param = 'p'
#     max_page_size = 20
#
#
# # 继承了ListModeMixin，具有了分页过滤等功能
# class NewsListViewset(viewsets.ModelViewSet):
#     # 分页,搜索，过滤，排序的功能
#     queryset = News.objects.all()
#     serializer_class = NewsSerializer
#     pagination_class = StandardResultsSetPagination
#     filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
#     # filter_fields = ('id', 'title')
#     filter_class = NewsFilter
#     search_fields = ('title', 'tag')
#     ordering_fields = ('id', 'title')

class NewsListView(APIView):
    # permission_classes = (IsAuthenticated, IsAuthenticatedOrReadOnly)
    # authentication_classes = (JSONWebTokenAuthentication,)

    def post(self, request, format=None):
        try:
            page = int(request.POST.get('page', 1))
            page_size = int(request.POST.get('page_size', 2))
        except Exception as err:
            return Response(data=generate_response(code=ResponseCode.CODE_MESSAGE_ERROR))
        total = News.objects.count()
        start = (page - 1) * page_size
        end = page * page_size
        news = News.objects.all()[start:end]
        serializer = NewsSerializer(news, many=True)
        message = create_list_msg(serializer.data, total, page, page_size)
        data = generate_response(message)
        return Response(data=data, status=status.HTTP_200_OK)


class RegisterView(APIView):
    def post(self, request):
        user_name = request.POST.get("username", "")
        password = request.POST.get("password", "")
        if user_name and password:
            # 不为空的时候，查询是否有这个账号了
            user = UserProfile.objects.filter(username=user_name)
            if user:
                return Response(data=generate_response(data="账号已经存在"))
            else:
                # 保存用户
                # user=UserProfile(username=user_name,password=password)
                # 这种方式会加密密码
                user = UserProfile.objects.create_user(username=user_name, password=password)
                user.save()
                return Response(data=generate_response(data="用户注册成功！"))
        else:
            return Response(data=generate_response(data="账号或者密码未填写"))


def jwt_response_payload_handler(token, user=None, request=None):
    user = UserSerializer(user, context={'request': request}).data
    user['token'] = token
    data = generate_response(data=user)
    return data


def jwt_response_payload_error_handler(serializer, request=None):
    return {
        'status': 200,
        'message': "用户名或者密码错误",
        'data': None
    }
