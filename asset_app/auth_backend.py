from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend

'''class EmailBackend(ModelBackend):
    def authenticate(self, request, email=None, password=None, **kwargs):
        UserModel = get_user_model()
        try:
            user = UserModel.objects.get(email=email)
        except UserModel.DoesNotExist:
            return None
        else:
            if user.check_password(password):
                return user
        return None
        
'''
from django.contrib.auth import login

from rest_framework.authentication import BasicAuthentication

class MyBasicAuthentication(BasicAuthentication, ModelBackend):

    def authenticate(self, request, email=None, password=None, **kwargs):
        #user, _ = super(MyBasicAuthentication, self).authenticate(request)
        UserModel = get_user_model()
        try:
            user = UserModel.objects.get(email=email)
        except UserModel.DoesNotExist:
            return None
        else:
            if user.check_password(password):
                login(request, user)
                return user
        return None
        
