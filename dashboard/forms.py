# forms.py
from django import forms
from .models import PineNews, PineNewsCategories, PineNewsTags

class PineNewsForm(forms.ModelForm):
    categories = forms.ModelMultipleChoiceField(
        queryset=PineNewsCategories.objects.all(),
        widget=forms.SelectMultiple,  
        required=False
    )
    tags = forms.ModelMultipleChoiceField(
        queryset=PineNewsTags.objects.all(),
        widget=forms.SelectMultiple, 
        required=False
    )

    class Meta:
        model = PineNews
        exclude = ['created_by']
