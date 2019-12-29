from django import forms
from django.forms import ModelForm
from .models import Post, Message
from django.core.exceptions import ValidationError

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['work', 'body', 'place', 'start_work']
        widgets = {
            'work': forms.TextInput(attrs={'class': 'form-control', 'label': 'робота'}),
            'place': forms.Textarea(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'start_work': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def clean_slug(self):
        new_slug = self.cleaned_data['slug'].lower()

        if new_slug == 'create':
            raise ValidationError('Не можливо створити слаг "create".')
        return new_slug

class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ['message']
        labels = {'message': ""}