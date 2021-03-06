from django import forms
from django.contrib.auth import authenticate

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100, label="KUllanıcı Adı")
    password = forms.CharField(max_length=100,label="Şifre",widget=forms.PasswordInput)

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username,password=password)
            if not user:
                raise forms.ValidationError("Böyle bir kullanıcı yok")
            return super(LoginForm, self).clean()