from rest_framework import serializers

from .models import News, Comment, UserProfile


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('username', 'email', 'nick_name', 'gender',)


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        # fields = ('title', 'body')
        fields = '__all__'


class NewsSerializer(serializers.ModelSerializer):
    # title = serializers.CharField(required=True, max_length=100)
    # body=serializers.CharField()
    # #新闻model没有的，可以直接添加阅读次数
    # readtime=serializers.IntegerField(default=0)
    # img_url=serializers.ImageField()
    # def create(self, validated_data):
    #     return News.objects.create(**validated_data)

    class Meta:
        model = News
        # fields = ('title', 'body')
        fields = '__all__'
