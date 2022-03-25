from django import forms
from .models import Customer


class InformationForm(forms.Form):
    firstname = forms.CharField(max_length=20)
    lastname = forms.CharField(max_length=20)
    age = forms.IntegerField()
    comment = forms.CharField(max_length=255)


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ["firstname", "lastname", "age", "profession"]
