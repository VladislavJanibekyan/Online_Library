from .models import Book
from django import forms

class DropdownForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ["age_group"]
