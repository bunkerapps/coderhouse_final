from django import forms
from .models import Blog

class CreateBlog(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'content', 'author']

class FindBlog(forms.Form):
    title = forms.CharField(max_length=200, required=False)
    author = forms.CharField(max_length=100, required=False)