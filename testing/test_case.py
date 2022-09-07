from django.contrib.auth.models import User
from tweet.models import Tweet
from django.test.testcases import TestCase


class TweetTest(TestCase):
    def create_user(self,username):
        return User.objects.create_user(username=username,email = 'email@email.com',password='12345')

    def create_tweet(self,user):
        return Tweet.objects.create(user=user,content="default tweet content.")
