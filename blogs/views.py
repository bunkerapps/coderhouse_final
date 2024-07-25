from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model
from .models import Blog, Comment
from .forms import ContactForm
from django.core.mail import send_mail
from django.contrib import messages
from django.views.generic import TemplateView
from django.conf import settings


User = get_user_model()
from .forms import BlogForm, CommentForm, FindBlog
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail, BadHeaderError


class ContactView(TemplateView):
    template_name = 'contact.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Contáctanos'
        context['form'] = ContactForm()
        return context

    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            try:
                send_mail(
                    f'Mensaje de {name}',
                    message,
                    email,
                    [settings.DEFAULT_FROM_EMAIL],
                )
                context = self.get_context_data(success=True)
            except (BadHeaderError, Exception) as e:
                messages.error(request, 'Por favor configura el settings.py')
                print(f'Error: {e}') 
                context = self.get_context_data(form=form, error=str(e))
        else:
            context = self.get_context_data(form=form)
        return self.render_to_response(context)
    template_name = 'contact.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Contáctanos'
        context['form'] = ContactForm()
        return context
# Create your views here.
#crear view de un template index.html
def index(request):
    form = FindBlog(request.GET or None)
    blogs = Blog.objects.all()
    comments = Comment.objects.all()
    users = User.objects.all()
    if form.is_valid():
        title = form.cleaned_data.get('title')
        if title:
            blogs = blogs.filter(title__icontains=title)
    context={"title":'Super Blog',"blogs":blogs, 'comments': comments, users: 'users', 'form': form}
    return render(request, 'index.html',context)

def blog(request):
    context = {"title": 'Blogs'}
    return render(request, 'blog.html', context)
    
    # return render(request, 'blog.html')
    
# def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            
            try:
                # Intentar enviar el correo electrónico
                send_mail(
                    f'Message from {name}',
                    message,
                    email,
                    ['your_email@example.com'],  # Cambia esto a tu dirección de correo electrónico
                    fail_silently=False,
                )
                messages.success(request, '¡Tu mensaje ha sido enviado exitosamente!')
                return redirect('contact')
            except (BadHeaderError, Exception) as e:
                # Capturar la excepción y mostrar un mensaje de error en español
                messages.error(request, 'Por favor configura el settings.py')
                print(f'Error: {e}')  # Opcional: imprimir el error en la consola para depuración
    else:
        form = ContactForm()
    
    context = {
        'title': 'Contáctanos',
        'form': form,
    }
    return render(request, 'contact.html', context)

    
def blog_detail(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    comments = blog.comments.all()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.blog = blog
            comment.author = request.user
            comment.save()
            return redirect('/', blog_id=blog.id)
    else:
        form = CommentForm()
    return render(request, 'blog_detail.html', {'blog': blog, 'comments': comments, 'form': form})

@login_required
def new_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.author = request.user  
            blog.save()
            return redirect('index')
    else:
        form = BlogForm()
    return render(request, 'new_blog.html', {'form': form})

@login_required
def edit_blog(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.save()
            return redirect('/', blog_id=blog.id)
    else:
        form = BlogForm(instance=blog)
    return render(request, 'edit_blog.html', {'form': form})

@login_required
def delete_blog(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    if request.method == 'POST':
        blog.delete()
        return redirect('index')
    return render(request, 'delete_blog.html', {'blog': blog})
