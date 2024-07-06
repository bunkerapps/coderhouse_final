from django.shortcuts import render

# Create your views here.
#crear view de un template index.html
def index(request):
    context={"title":'Super Blog'}
    return render(request, 'index.html',context)

def blog(request):
    context = {"title": 'Blogs'}
    return render(request, 'blog.html', context)
    
    # return render(request, 'blog.html')
    
def about(request):
    context = {"title": 'About Us'}
    return render(request, 'about.html', context)
    
def contact(request):
    context = {"title": 'Contact Us'}
    return render(request, 'contact.html', context)
