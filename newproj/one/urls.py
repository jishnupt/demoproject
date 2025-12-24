from django.urls import path
from .views import *

urlpatterns = [
    path('home',homepage),
    path('about',aboutpage)
]