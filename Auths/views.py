from django.shortcuts import render
from allauth.socialaccount.providers.facebook.views import GoogleOAuth2Adapter
from dj_rest_auth.registration.views import SocialLoginView
from dj_rest_auth.social_serializers import GoogleLoginSerializer

class GoogleLogin(SocialLoginView):
    serializer_class = GoogleLoginSerializer
    adapter_class = GoogleOAuth2Adapter
