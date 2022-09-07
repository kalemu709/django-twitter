from rest_framework import viewsets
from rest_framework.decorators import action
from tweet.api.serializer import TweetSerializer,TweetPostSerializer
from rest_framework.response import Response
from tweet.models import Tweet
from rest_framework import permissions
from accounts.api.serializers import UserSerializer


class TweetViewSet(viewsets.ViewSet):
    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer

    def get_permissions(self):
        if self.action == 'post_content':
            return [permissions.IsAuthenticated()]
        return [permissions.AllowAny()]

    @action(methods=['POST'], detail=False)
    def post_content(self, request):
        serializer = TweetPostSerializer(data=request.data)
        serializer.context['request'] = request
        if not serializer.is_valid():
            return Response({'invalid': serializer.errors}, status=400)
        tweet = serializer.save()
        return Response({'Saved content': TweetSerializer(tweet).data}, status=200)

    @action(methods=['GET'], detail=False)
    def list_content(self, request):
        if 'user_id' not in request.query_params:
            return Response(status=400)
        tweets = Tweet.objects.all().filter(user = request.query_params['user_id']).order_by('-created_at')
        serial = TweetSerializer(tweets,many=True)
        return Response({'All posts':serial.data},status=200)
