from django.shortcuts import render
from django.core import serializers

from .models import Analyst, Assets, User
from rest_framework.authtoken.models import Token
from django.contrib.auth import logout 

from .serializers import (
    AnalystInfoSerializer,
    AssetsInfoSerializer,
    CreateUserSerializer,
    LoginSerializer
)
from rest_framework.authentication import  SessionAuthentication
from .auth_backend import MyBasicAuthentication
from rest_framework.permissions import   IsAuthenticated

from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer

from rest_framework import viewsets, permissions
from rest_framework.response import Response
from django.http import HttpResponse
from django.contrib.auth import authenticate, login

class AnalystsViewSet(viewsets.ModelViewSet):
    queryset = Analyst.objects.all()
    serializer_class = AnalystInfoSerializer
    permission_classes = [IsAuthenticated ]
    authentication_classes = (SessionAuthentication, MyBasicAuthentication)

class AssetsViewSet(viewsets.ModelViewSet):
    queryset = Assets.objects.all()
    serializer_class = AssetsInfoSerializer
    permission_classes = [IsAuthenticated ]
    authentication_classes = (SessionAuthentication, MyBasicAuthentication)
    
class UserAuthenticationViewSet(viewsets.ModelViewSet):
    serializer_class = CreateUserSerializer
    def signup(self, request, *args, **kwargs):
        
        if request.data['password1']!=request.data['password2']:
            return Response('Passwords do not match', status=400)
            
        serializer = CreateUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        validated_data = serializer.data
                
        user = User.objects.create(**validated_data)
        user.set_password(validated_data.pop("password1"))
        validated_data.pop("password2")

        try:
            user.is_staff = validated_data.pop("is_staff")
        except KeyError:
            user.is_staff = False

        for attr, value in validated_data.items():
            setattr(user, attr, value)

        user.is_superuser = False
        user.save()

        return Response('User created successfully', status=200)
    
class LoginViewSet(viewsets.ModelViewSet):
    serializer_class = LoginSerializer
    def login(self, request, *args, **kwargs):
        
        email = request.data['email']
        password = request.data['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            try:
                token = Token.objects.get(user=user)
            except:
                token = Token.objects.create(user=user)
            return Response({'status':'Login Successful'}, status=200)
            
        else:
            return Response('Login Failed', status=403)
        
        
@api_view(('GET',))
@renderer_classes((TemplateHTMLRenderer, JSONRenderer))
def customlogout(request):
    print(request.user.username)
    if request.user.username != '':
        request.user.auth_token.delete()
        logout(request)
        return HttpResponse('Logout Successful',status=200)
    else:
        return HttpResponse('Requires Authentication',status=401)
    
    
signup = UserAuthenticationViewSet.as_view({"post": "signup"})
login = LoginViewSet.as_view({"post": "login"})

 



