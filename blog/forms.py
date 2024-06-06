from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.contrib.auth.models import User
from django.utils.translation import gettext, gettext_lazy as _
from .models import Post


class SignUpForm(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control my-1'}))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'class':'form-control my-1'}))
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        labels = {'email': 'Email'}
        widgets = {
            'username':forms.TextInput(attrs={'class':'form-control my-1'}),
            'first_name':forms.TextInput(attrs={'class':'form-control my-1'}),
            'last_name':forms.TextInput(attrs={'class':'form-control my-1'}),
            'email':forms.EmailInput(attrs={'class':'form-control my-1'}),
        }

class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus': True, 'class':'form-control my-1'}))
    password = forms.CharField(label=_('Password'), strip=False, widget=forms.PasswordInput(attrs={'autocomplete': 'current-password', 'class':'form-control my-1'}))

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'desc']
        labels = {'desc': 'Description'}
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'desc': forms.Textarea(attrs={'class':'form-control'}),
        }