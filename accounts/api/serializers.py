from django.contrib.auth.models import User, Group
from rest_framework import serializers, exceptions


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [ 'email', 'username']


class SignUpSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=10)
    password = serializers.CharField(min_length=4)
    email = serializers.EmailField()

    class Meta:
        model = User
        fields = ['email', 'username', 'password']

    def validate(self, data):
        print("validating data")
        if User.objects.filter(username=data['username']).exists():
            raise exceptions.ValidationError({"message": "username exists"})
        if User.objects.filter(email=data['email']).exists():
            raise exceptions.ValidationError({"message": "email exists"})
        return data

    def create(self, validated_data):
        print("Saving user")
        user = User.objects.create_user(email=validated_data['email'], username=validated_data['username'],
                                        password=validated_data['password'])
        return user


class SignInSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=10)
    password = serializers.CharField(min_length=4)

