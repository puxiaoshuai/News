from rest_framework import serializers

from .models import News, Comment, UserProfile, NewsTag, DuanziModel


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('id', 'username', 'email', 'nick_name', 'gender',)


class NewsTag(serializers.ModelSerializer):
    class Meta:
        model = NewsTag
        fields = '__all__'


class User_CommentSerizer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('id', 'username')


class CommentSerializer(serializers.ModelSerializer):
    #通过关键字查询细节，字段名要对应,
    user = UserSerializer()

    class Meta:
        model = Comment
        fields = ('id', 'text', 'create_time', 'user')
        # fields = '__all__'


class NewsSerializer(serializers.ModelSerializer):
    newstag=NewsTag()
    comment_num=serializers.CharField(default=0)
    class Meta:
        model = News
        # fields = ('title', 'body')

        fields = ('id','title','body','img_url','img_tv_url','tv_name','create_time','time_tv','newstag','comment_num')


class DuanziSerializer(serializers.ModelSerializer):
    user = User_CommentSerizer()

    class Meta:
        model = DuanziModel
        fields = ('id', 'title', 'body', 'create_time', 'user')
