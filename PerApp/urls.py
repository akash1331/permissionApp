"""PerApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('permission/',permissionAPIView.as_view()),
    path('masterfilters/',masterfilters.as_view()),
    path('permission/<str:id>',permissionDetail.as_view()),
    path('permissionDetail/<str:id>',Permission_filter.as_view()),
    path('granted_roll/',grantedfilter.as_view()),
    path('admingrant/',admingrantview.as_view()),
    path('admingrant/<int:id>',admingrant.as_view()),
]


'''for master filter use url
http://127.0.0.1:8000/masterfilters/?branch=CSM,



'''