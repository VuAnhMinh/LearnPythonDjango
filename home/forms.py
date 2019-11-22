from django import forms
import re
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

class RegistrationForm(forms.Form) :
    username = forms.CharField(label = "Account Name", max_length=30)
    email = forms.EmailField(label="Email Address")
    password = forms.CharField(label = "Login Password ", widget = forms.PasswordInput())
    passwordcheck = forms.CharField(label = "Confirm Password", widget = forms.PasswordInput())

    def clean_passwordcheck(self):
        if 'password' in self.cleaned_data:
            password = self.cleaned_data['password']
            passwordcheck = self.cleaned_data['passwordcheck']
            if password == passwordcheck and password :
                return password
        raise forms.ValidationError("Invalid Password !")

    def clean_username(self):
        username = self.cleaned_data['username']
        if not re.search(r'^\w+$', username):
            raise forms.ValidationError("Dont use special symbols in Account Name")
        try:
            User.objects.get(username = username)
        except ObjectDoesNotExist:
            return username
        raise forms.ValidationError("Account already exists")

    def save(self):
        User.objects.create_user(username=self.cleaned_data['username'], email=self.cleaned_data['email'] , password=self.cleaned_data['password'])
