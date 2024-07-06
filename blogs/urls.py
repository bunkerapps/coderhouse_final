from django.urls import path
from blogs import views


urlpatterns = [
    path('', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('blog', views.blog, name='blog'),
]