from django import forms
from .models import Item, Image


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'price', ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'id': 'name'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'id': 'price'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'mm-dd-yy', 'id': 'date', 'hidden': True}),
        }


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['image', ]
        widgets = {
            'image': forms.FileInput(attrs={'class': 'form-control', "multiple": True, 'id': 'images'}),
        }
