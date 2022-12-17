from cProfile import label
from dataclasses import fields
from tkinter import Widget
from django.contrib.auth.forms import UserCreationForm, UserChangeForm,AuthenticationForm
from .models import *
from django import forms
from django.utils.translation import gettext_lazy as _

class CustomUserCreationForm(UserCreationForm):
    #password1 =forms.CharField(max_length=200, widget=forms.PasswordInput(),label='Confirm Password')
    #password =forms.CharField(max_length=200, widget=forms.PasswordInput(), label='Password')

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs['placeholder'] = self.fields['email'].label
        self.fields['first_name'].widget.attrs['placeholder'] = self.fields['first_name'].label
        self.fields['last_name'].widget.attrs['placeholder'] = self.fields['last_name'].label
        self.fields['password1'].widget.attrs['placeholder'] = self.fields['password1'].label
        self.fields['password2'].widget.attrs['placeholder'] = self.fields['password2'].label


    class Meta:
        model = myuser
        fields = ('email','first_name','last_name','password1','password2')

class MyLoginForm(AuthenticationForm):
    username = forms.EmailField(label='Email',widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    password = forms.CharField(max_length=32, widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))


class CommentForm(forms.ModelForm):
    class Meta:
        model = BlogComment
        fields = ('body','parent')
       