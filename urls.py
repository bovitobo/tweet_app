from django.contrib import admin
from django.urls import path, re_path,include

from rest_framework import routers

from .views.main import main_page
from .views.user_account import UserAccountViewSet

admin.autodiscover()

router = routers.SimpleRouter('')
router.register(r'user_account', UserAccountViewSet)

urlpatterns = [
    path('', main_page),
]

urlpatterns += router.urls
