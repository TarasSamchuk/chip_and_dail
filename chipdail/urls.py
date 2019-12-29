from django.urls import path
from chipdail import views
from .views import *
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', home_page, name='home_page'),
    path('accounts/login/', login, name='login_url'),
    path('accounts/logout/', logout, name='logout_url'),
    path('posts_list/', posts_list, name='posts_list_url'),
    path('post/create/', PostCreate.as_view(), name='post_create_url'),
    path('posts_list/delete/<str:slug>/', delete, name='del_post_url'),
    path('post/<str:slug>/', post_detail, name='post_detail_url'),
    path('dialogs/', login_required(views.DialogsView.as_view()), name='dialogs'),
    path('dialogs/create/<user_id>/', login_required(views.CreateDialogView.as_view()), name='create_dialog'),
    path('dialogs/<chat_id>/', login_required(views.MessagesView.as_view()), name='messages'),
]