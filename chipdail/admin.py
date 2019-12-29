from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from django.contrib.admin.filters import ListFilter

from .models import Post
from .models import Chat
from .models import Message


# class PostAdmin(admin.ModelAdmin):
#     prepopulated_fields = {'slug': ('slug')}

admin.site.register(Post)
admin.site.register(Chat)
admin.site.register(Message)
