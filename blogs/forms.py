from django import forms
from .models import Blog, Comment

class CreateBlog(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'content', 'author']

class FindBlog(forms.Form):
    title = forms.CharField(max_length=200, required=False)
    author = forms.CharField(max_length=100, required=False)

    


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'content', 'image']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
        
    def save(self, commit=True):
        blog = super().save(commit=False)
        if self.cleaned_data.get('remove_image'):
            blog.image.delete()
            blog.image = None
        if commit:
            blog.save()
        return blog
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
        
class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}), required=True)