from datetime import timedelta, date

from django import forms

from administrator.models import UnitGroceries
from visitor.models import User


class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'


class UnitGroceriesForm(forms.ModelForm):
    price_yesterday = forms.IntegerField(label='Harga Kemarin', min_value=0, initial=0,
                                         widget=forms.TextInput(attrs={'disabled': 'true'}))

    class Meta:
        model = UnitGroceries
        fields = ['unit_groceries_variant', 'price_yesterday', 'unit_groceries_price', 'unit_groceries_created']
