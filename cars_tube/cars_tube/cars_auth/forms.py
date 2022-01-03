from django import forms
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError

from cars_tube.cars_auth.models import Profile


class SignInForm(forms.Form):
    user = None

    username = forms.CharField(
        max_length=150
    )

    password = forms.CharField(
        max_length=150,
        widget=forms.PasswordInput(),
    )

    def clean_password(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        self.user = authenticate(
            username=username,
            password=password,
        )

        if not self.user:
            raise ValidationError('Username and/or password incorrect.')

    def save(self):
        return self.user


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']


