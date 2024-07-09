from django.shortcuts import render, redirect
from .models import Blog
from .forms import BlogForm
from django.contrib.auth.decorators import login_required


# Create your views here.
#crear view de un template index.html
def index(request):
    blogs = Blog.objects.all()
    context={"title":'Super Blog',"blogs":blogs}
    return render(request, 'index.html',context)

def blog(request):
    context = {"title": 'Blogs'}
    return render(request, 'blog.html', context)
    
    # return render(request, 'blog.html')
    
def contact(request):
    context = {"title": 'Contact Us'}
    return render(request, 'contact.html', context)

def blog_detail(request, blog_id):
    context = {"title": 'Blog Detail'}
    return render(request, 'blog_detail.html', context)

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

def edit_blog(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.save()
            return redirect('blog_detail', blog_id=blog.id)
    else:
        form = BlogForm(instance=blog)
    return render(request, 'edit_blog.html', {'form': form})

def delete_blog(request, blog_id):
    context = {"title": 'Delete Blog'}
    return render(request, 'delete_blog.html', context)
