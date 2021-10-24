from django.urls import path
from django.urls.resolvers import URLPattern

URLPattern += [
  
    path('dj-rest-auth/google/', GoogleLogin.as_view(), name='gl_login')
]