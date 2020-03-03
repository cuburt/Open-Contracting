import unicodedata

from django import forms
from django.contrib.auth import password_validation
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext, gettext_lazy as _
from .models import *

class NewUserForm(forms.ModelForm):
    username = forms.CharField(
        label="Username",
        help_text=_("Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.")
    )
    first_name = forms.CharField(label="Given Name")
    last_name = forms.CharField(label="Surname")
    email = forms.EmailField(label="Email address")
    password1 = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput,
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label=_("Password confirmation"),
        widget=forms.PasswordInput,
        strip=False,
        help_text=_("Enter the same password as before, for verification."),
    )

    class Meta:
        model = User
        fields = ("first_name", "last_name", "username", "email","password1","password2")

class DatasetForm(forms.ModelForm):
    class Meta:
        model = Dataset
        fields = ('title','date_updated')

class DatabaseForm(forms.ModelForm):
    class Meta:
        model = Database
        fields = ('title','description','frequency','group_by_column','columns','file')