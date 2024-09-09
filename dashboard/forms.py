# forms.py
from django import forms

from .models import PineNews

class PineNewsForm(forms.ModelForm):
    class Meta:
        model = PineNews
        fields = '__all__'
