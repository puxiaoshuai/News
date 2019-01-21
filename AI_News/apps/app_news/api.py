import qiniu
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, mixins, status

from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.views import APIView
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from AI_News.settings import access_key, secret_key
from app_news.filters import NewsFilter
from .models import News, UserProfile, NewsTag, Comment
from .serialaizers import NewsSerializer, UserSerializer,CommentSerializer
from rest_framework.response import Response
from common.HttpResponseUtil import generate_response, ResponseCode, create_list_msg


# 1.构建序列化,导入进来了
# 2.编写视图,方法视图，类视图

# class StandardResultsSetPagination(PageNumberPagination):
#     page_size = 3
#     page_size_query_param = 'page_size'
#     # page_query_param = 'p'
#     max_page_size = 20
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
# 这是新闻的列表
class NewsListView(APIView):
    # permission_classes = (IsAuthenticated, IsAuthenticatedOrReadOnly)
    # authentication_classes = (JSONWebTokenAuthentication,)
    def post(self, request, format=None):
        try:
            page = int(request.POST.get('page', 1))
            news_tag = request.POST.get('tag', "热点")
            newsTag = NewsTag.objects.filter(name=news_tag).first()
            page_size = int(request.POST.get('page_size', 10))
        except Exception as err:
            return Response(data=generate_response(code=ResponseCode.CODE_MESSAGE_ERROR))
        total = News.objects.count()
        start = (page - 1) * page_size
        end = page * page_size
        news = News.objects.filter(newstag=newsTag)[start:end]
        serializer = NewsSerializer(news, many=True)
        message = create_list_msg(serializer.data, total, page, page_size)
        data = generate_response(message)
        return Response(data=data, status=status.HTTP_200_OK)


# 新闻详情
class NewsDetailView(APIView):
    def post(self, request):
        try:
            id = int(request.POST.get('id'))
        except:
            id = 0
        news = News.objects.filter(id=id).first()
        serializer = NewsSerializer(news)
        if news:
            data = generate_response(serializer.data)
        else:
            data = generate_response(data="没有此数据", code=ResponseCode.CODE_NOTFOUND)
        return Response(data=data)


# 新闻评论列表
class News_CommentListView(APIView):
    def post(self, request):
        try:
            news_id = int(request.POST.get('news_id'))
        except:
            news_id = 0
        news = News.objects.filter(id=news_id).first()
        if news:
            comments=news.news_comment.all()
            serializer = CommentSerializer(comments,many=True)
            total=len(comments)
            msg=create_list_msg(data=serializer.data,total=total,page=1,page_size=100)
            data=generate_response(data=msg)
        else:
            data = generate_response(data="新闻没查询到", code=ResponseCode.CODE_NOTFOUND)
        return  Response(data=data)



# 七牛token
class get_QiniuView(APIView):

    def post(self, request):
        q = qiniu.Auth(access_key, secret_key)
        bucket = 'todo'
        # expires设置缓存时间15天,可自己设置
        token = q.upload_token(bucket=bucket, expires=3600 * 24 * 15)
        return Response(generate_response(data=token))


# 新闻评论
class News_CommentView(APIView):
    permission_classes = (IsAuthenticated, IsAuthenticatedOrReadOnly)
    authentication_classes = (JSONWebTokenAuthentication,)

    # 进行了登录验证，客户端需要上传 jwt token
    # 对新闻进行评论，首先拿到新闻的id,
    def post(self, request):
        comment_data = request.POST.get('comment', "")
        try:
            news_id = int(request.POST.get('news_id'))

        except:
            news_id = 0
        try:
            user_id = int(request.POST.get('user_id'))
        except:
            user_id = 0
        print("news_id+{}".format(news_id))
        print("user_id+{}".format(user_id))
        news = News.objects.filter(id=news_id).first()
        print(news)
        user = UserProfile.objects.filter(id=user_id).first()
        print(user)
        if user and news:
            commet = Comment(text=comment_data, news=news, user=user)
            commet.save()

            data = generate_response("评论成功")
        else:
            data = generate_response(data="资源不存在,请检查参数值", code=ResponseCode.CODE_NOTFOUND)
        return Response(data=data)


# 注册
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


# 登录 使用的rest-jwt

# 登录成功返回的jwt 自定义的结构
def jwt_response_payload_handler(token, user=None, request=None):
    user = UserSerializer(user, context={'request': request}).data
    user['token'] = token
    data = generate_response(data=user)
    return data


# 登录失败自定义返回
def jwt_response_payload_error_handler(serializer, request=None):
    return {
        'status': 200,
        'message': "用户名或者密码错误",
        'data': None
    }
