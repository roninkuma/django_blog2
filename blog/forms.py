from django import forms
from .models import *


class Articleform(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content', 'photo', 'category']
