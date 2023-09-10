from django import forms
from visitor.models import User


class LoginForm(forms.ModelForm):
    class Meta:
        model = User
