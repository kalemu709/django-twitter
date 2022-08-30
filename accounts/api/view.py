from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from accounts.api.serializers import UserSerializer
from accounts.api.serializers import SignUpSerializer, SignInSerializer
from rest_framework.permissions import AllowAny
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth import login, authenticate, logout


class ViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class AccountViewSet(viewsets.ViewSet):
    permission_classes = (AllowAny,)
    serializer_class = SignUpSerializer

    @action(methods=['POST'], detail=False)
    def signup(self, request):
        serializer = SignUpSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({'message': 'inputs having issue', 'error': serializer.errors}, status=400)
        user = serializer.save()
        return Response({"created user": serializer.data}, status=200)

    @action(methods=['POST'], detail=False)
    def signin(self, request):
        serializer = SignInSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({"message": "bad login inputs", "error": serializer.errors}, status=400)
        user = authenticate(username=serializer.validated_data["username"],
                            password=serializer.validated_data["password"])
        if not user or user.is_anonymous:
            return Response({"error": "wrong username or password"}, status=400)
        login(request, user)
        return Response({"logged in user": serializer.data}, status=200)

    @action(methods=['GET'], detail=False)
    def login_status(self,request):
        response={"user authenticated" : request.user.is_authenticated}
        if request.user.is_authenticated:
            response["authenticated user"] = UserSerializer(request.user).data
        return Response(response,status=200)

    @action(methods=['POST'], detail=False)
    def logout(self, request):
        logout(request)
        return Response(status=200)


