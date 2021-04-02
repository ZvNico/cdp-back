from rest_framework import viewsets
from . import models
from . import serializers
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from rest_auth.registration.views import SocialLoginView
# Create your views here.

class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter