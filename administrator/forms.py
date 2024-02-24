from datetime import timedelta, date

from django import forms

from administrator.models import UnitGroceries
from visitor.models import User


class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'


class UnitGroceriesForm(forms.ModelForm):
    price_yesterday = forms.DecimalField(
        label='Harga Kemarin',
        min_value=0,
        initial=0,
        required=False,
        widget=forms.TextInput(
            attrs={
                'disabled': True,
                'style': 'border: none'
            }
        )
    )

    class Meta:
        model = UnitGroceries
        fields = ['unit_groceries_variant', 'price_yesterday', 'unit_groceries_price', 'unit_groceries_created']

    def save(self, commit=True):
        instance = super().save(commit=False)
        if commit:
            instance.save()
        return instance