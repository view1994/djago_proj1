"""djago_proj1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from Django_app1.views import *
from django.conf.urls import url
urlpatterns = [
    path('',FR_home),
    path('admin/', admin.site.urls),
    path('hello/' , hello_view),
    path('login',FR_login_page),
    path('register',FR_register_page),
    url(r'^regist_submit$',FR_regist_confirm),
    url(r'^login_submit$',FR_login_confirm),
    url(r'^room107$',hello_view),
    url(r'^index/', index),
    url(r'^chart/', chart),
]
