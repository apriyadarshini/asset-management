from rest_framework import serializers
from .models import (
    Analyst,
    Assets,
    User
)
from django import forms

class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "username",
            "address",
            "contact_no",
            "email",
            "password1",
            "password2",
            "job_title",
            "title"
        )
        widgets = {
        'password1': forms.PasswordInput(),
        'password2': forms.PasswordInput()
        }
        
class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()
        
        
class AnalystInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Analyst
        fields = (
            "name",
            "company",
        )
        
class AssetsInfoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Assets
        fields = (
            "url",
            "name",
            "description",
            "inception_date",
            "isActive",
            "analyst",
        )