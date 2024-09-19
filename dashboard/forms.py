# forms.py
from django import forms
from .models import PineNews, PineNewsCategories, PineNewsTags

class PineNewsForm(forms.ModelForm):
    class Meta:
        model = PineNews
        exclude = ['created_by']
        
