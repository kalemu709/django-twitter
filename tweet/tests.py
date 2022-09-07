from django.test import TestCase
from tweet.models import Tweet
from django.contrib.auth.models import User
from datetime import datetime, timedelta


class TweetTest(TestCase):
    def test_hours_to_now(self):
        user = User.objects.create_user('test user')
        tweet = Tweet.objects.create(user=user, content='jiuzhang good')
        tweet.created_at = datetime.utcnow() - timedelta(hours=10)
        tweet.save()
        self.assertEqual(tweet.hours_age, 10)
