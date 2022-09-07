from testing.test_case import TweetTest
from rest_framework.test import APIClient


class TweetAPITest(TweetTest):
    def setUp(self):
        print('creating user1')
        self.user1 = self.create_user('user1')
        self.create_tweet(self.user1)
        self.client = APIClient()

    def test_create_tweet(self):
        response = self.client.get('/api/tweet/list_content/?user_id=1', {})
        print('test response:' + response.data['All posts'][0]['content'])
        self.assertEqual(len(response.data['All posts']), 1)
        self.assertEqual(response.status_code, 200)
        self.client.force_authenticate(self.user1)
        response = self.client.post('/api/tweet/post_content/', {'content': 'User defined content'})
        self.assertEqual(response.status_code, 200)
        response = self.client.get('/api/tweet/list_content/?user_id=1', {})
        self.assertEqual(len(response.data['All posts']), 2)
        self.assertEqual(response.data['All posts'][0]['content'], 'User defined content')
