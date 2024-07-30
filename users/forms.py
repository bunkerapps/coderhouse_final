from django import forms
from django.contrib.auth.forms import UserCreationForm
from users.models import User

class UserRegisterForm(UserCreationForm):
    username = forms.CharField()
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput)
    last_name = forms.CharField()
    first_name = forms.CharField()
    photo = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'last_name', 'first_name', 'photo']
        help_texts = {k: "" for k in fields}
        widgets = {
        'title': forms.TextInput(attrs={'class': 'form-control'}),
        'content': forms.Textarea(attrs={'class': 'form-control'}),
        'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

class UserEditForm(forms.ModelForm):
    email = forms.EmailField(label="Modificar E-mail", widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput(attrs={'class': 'form-control'}), required=False)
    password2 = forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput(attrs={'class': 'form-control'}), required=False)
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    photo = forms.ImageField(required=False, widget=forms.ClearableFileInput(attrs={'class': 'form-control'}))
    about = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'last_name', 'first_name', 'photo', 'about']
        help_texts = {k: "" for k in fields}
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'photo': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'about': forms.Textarea(attrs={'class': 'form-control'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 and password1 != password2:
            self.add_error('password2', "Las contraseñas no coinciden")
        return cleaned_data