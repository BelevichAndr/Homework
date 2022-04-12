from django import forms
from .models import Tasks, Customer


class TasksForm(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = ["title", "content"]


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ["firstname", "lastname", "age"]



