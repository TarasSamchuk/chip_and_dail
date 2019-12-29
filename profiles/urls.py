from django.urls import path
from .views import *

urlpatterns = [
    path('profile/', user_page),
    path('detail/', user_detail, name='user_detail'),
    path('signup/', register, name='register_url'),
]