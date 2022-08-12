from django.contrib import admin
from django.urls import path, re_path, include

#from rest_framework import routers

from .views.main import main_page
from .views.user_account import registration, login

admin.autodiscover()

#router = routers.SimpleRouter('')

urlpatterns = [
    path('', main_page),
    path('user_account/register', registration),
    path('user_account/login', login),
]

#urlpatterns += router.urls
