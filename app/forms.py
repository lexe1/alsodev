from django import forms
from .models import Item


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'id': 'name'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'id': 'price'}),
            'images': forms.FileInput(attrs={'class': 'form-control', "multiple": True, 'id': 'images'}),
            'author': forms.Select(attrs={'class': 'form-control', 'id': 'author'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'mm/dd/yy', 'id': 'date'}),
        }
