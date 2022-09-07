import django.db.models
from rest_framework import serializers
from tweet.models import Tweet
from accounts.api.serializers import UserSerializer


class TweetSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Tweet
        fields = ['id', 'user', 'content', 'created_at']


class TweetPostSerializer(serializers.ModelSerializer):
    content = django.db.models.CharField(max_length=255)

    class Meta:
        model = Tweet
        fields = ['content']

    def create(self, validated_data):
        tweet = Tweet.objects.create(user=self.context['request'].user, content=validated_data['content'])
        return tweet
