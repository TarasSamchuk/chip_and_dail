from django.shortcuts import render
from django.shortcuts import redirect, reverse
from django.contrib.auth.forms import UserCreationForm
from .models import Post, Chat, User
from django.views.generic import View
from .forms import PostForm, MessageForm
from django.utils import timezone
from django.db.models import Q
from django.db.models import Count

def home_page(request):
    return render(request, 'chipdail/home_page.html')

def login(request):
    return render(request, 'chipdail/login.html')

def logout(request):
    return render(request, 'chipdail/logout.html')

def register(request):
    form = UserCreationForm()
    return render(request, 'profiles/registration.html', context={'form': form})

def posts_list(request):
    search_query = request.GET.get('search', '')

    if search_query:
        posts = Post.objects.filter(Q(work__icontains=search_query) | Q(body__icontains=search_query))
    else:
        posts = Post.objects.all()

    posts = Post.objects.all()
    return render(request, 'chipdail/posts_list.html', context={'posts': posts})

def post_detail(request, slug):
    post = Post.objects.get(slug__iexact=slug)
    return render(request, 'chipdail/post_detail.html', context={'post': post})

def delete(request, slug):
    post = Post.objects.get(slug__iexact=slug)
    post.delete()
    return render(request, 'chipdail/home_page.html', context={'post': post})

class PostCreate(View):
    def get(self, request):
        form = PostForm()
        return render(request, 'chipdail/post_create.html', context={'form': form})

    def post(self, request):
        if request.method == "POST":
            form = PostForm(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.user = request.user
                post.published_date = timezone.now()
                post.save()
                return render(request, 'chipdail/home_page.html')
        else:
            form = PostForm()
        return render(request, 'chipdail/post_create.html', {'form': form})

class DialogsView(View):
    def get(self, request):
        chats = Chat.objects.filter(members__in=[request.user.id])
        return render(request, 'chipdail/dialogs.html', {'user_profile': request.user, 'chats': chats})

class MessagesView(View):
    def get(self, request, chat_id):
        try:
            chat = Chat.objects.get(id=chat_id)
            if request.user in chat.members.all():
                chat.message_set.filter(is_readed=False).exclude(author=request.user).update(is_readed=True)
            else:
                chat = None
        except Chat.DoesNotExist:
            chat = None

        return render(
            request,
            'chipdail/messages.html',
            {
                'user_profile': request.user,
                'chat': chat,
                'form': MessageForm()
            }
        )

    def post(self, request, chat_id):
        form = MessageForm(data=request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.chat_id = chat_id
            message.author = request.user
            message.save()
        return redirect(reverse('users:messages', kwargs={'chat_id': chat_id}))

class CreateDialogView(View):
    def get(self, request, user_id):
        chats = Chat.objects.filter(members__in=[request.user.id, user_id], type=Chat.DIALOG).annotate(c=Count('members')).filter(c=2)
        if chats.count() == 0:
            chat = Chat.objects.create()
            chat.members.add(request.user)
            chat.members.add(user_id)
        else:
            chat = chats.first()
        return redirect(reverse('user:messages', kwargs={'chat_id': chat.id}))