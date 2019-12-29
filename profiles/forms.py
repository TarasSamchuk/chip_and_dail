from allauth.account.forms import SignupForm
from django import forms

class SignUp(SignupForm):
    first_name = forms.CharField(max_length=30, label='First Name', required=False)
    last_name = forms.CharField(max_length=30, label='Last Name', required=False)
    birthday = forms.CharField(max_length=10, label='birthday', required=False)
    phone = forms.IntegerField(label='phone', min_value=0, max_value=9999999999)

    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.birthday = self.cleaned_data['birthday']
        user.phone = self.cleaned_data['phone']
        user.save()
        return user
