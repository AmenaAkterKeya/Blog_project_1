from django import forms
from .models import posts

class PostForm(forms.ModelForm):
    class Meta:
        model = posts
        fields='__all__'