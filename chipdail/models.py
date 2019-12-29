from django.db import models
from django.shortcuts import reverse
from django.contrib.auth.models import User
from django.utils.text import slugify
from time import time
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

def gen_slug(s):
    new_slug = slugify(s, allow_unicode=True)
    return new_slug + '-' + str(int(time()))

class Post(models.Model):
    work = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=50, blank=True, unique=True)
    place = models.TextField(blank=True, db_index=True)
    body = models.TextField(blank=True, db_index=True)
    start_work = models.DateTimeField(null=True, blank=True)
    date_pub = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def get_absolute_url(self):
        return reverse('post_detail_url', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = gen_slug(self.work)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.slug

class Chat(models.Model):
    DIALOG = 'D'
    CHAT = 'C'
    CHAT_TYPE_CHOICES = (
        (DIALOG, _('Dialog')),
        (CHAT, _('Chat'))
    )

    type = models.CharField(
        _('Тип'),
        max_length=1,
        choices=CHAT_TYPE_CHOICES,
        default=DIALOG
    )
    members = models.ManyToManyField(User, verbose_name=_("Учасник"))

    def get_absolute_url(self):
        return 'users:messages', (), {'chat_id': self.pk}

class Message(models.Model):
    chat = models.ForeignKey(Chat, verbose_name=_("Чат"), on_delete=models.CASCADE, null=True)
    author = models.ForeignKey(User, verbose_name=_("Пользователь"), on_delete=models.CASCADE, null=True)
    message = models.TextField(_("Сообщение"))
    pub_date = models.DateTimeField(_('Дата сообщения'), default=timezone.now)
    is_readed = models.BooleanField(_('Прочитано'), default=False)

    class Meta:
        ordering = ['pub_date']

    def __str__(self):
        return self.message