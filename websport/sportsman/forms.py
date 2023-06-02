from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from captcha.fields import CaptchaField

from .models import *

class AddPostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cat'].empty_label = "Категорія не вибрана"


    class Meta:
        model = Sportsman
        fields = ['title', 'slug', 'content', 'photo', 'cat']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Введіть заголовок'}),
            'content': forms.Textarea(attrs={'cols': 60, 'rows': 10, 'class': 'form-input', 'placeholder': 'Введіть текст статті'}),
            'slug': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Введіть посилання на статтю'}),
'photo': forms.ClearableFileInput(attrs={'class': 'form-image', 'onchange': 'document.querySelector(".form-image").style.setProperty("--content", this.value); document.querySelector(".form-image").classList.add("form-image-styles");'}),
            'cat': forms.Select(attrs={'class': 'form-select'}),
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) > 200:
            raise ValidationError('Розмір тексту більший за 200 символів')

        return title


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логін', widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Введіть логін'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-input', 'placeholder': 'Введіть email'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input', 'placeholder': 'Введіть пароль'}))
    password2 = forms.CharField(label='Повторення пароля', widget=forms.PasswordInput(attrs={'class': 'form-input', 'placeholder': 'Введіть пароль повторно'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логін', widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Введіть логін'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input', 'placeholder': 'Введіть пароль'}))


class ContactForm(forms.Form):
    name = forms.CharField(label="Ім'я", max_length=255, widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Введіть ім\'я'}))
    email = forms.EmailField(label='Email', widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Введіть email'}))
    content = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows': 10, 'class': 'form-input', 'placeholder': 'Введіть текст повідомлення'}))
    captcha = CaptchaField()
