from django.urls import path
from blogs import views
from .views import ContactView, edit_profile, profile


urlpatterns = [
    path('contact', ContactView.as_view(), name='contact'),
    path('blog/<int:blog_id>', views.blog_detail, name='blog_detail'),
    path('new_blog', views.new_blog, name='new_blog'),
    path('edit_blog/<int:blog_id>', views.edit_blog, name='edit_blog'),
    path('delete_blog/<int:blog_id>', views.delete_blog, name='delete_blog'),
    path('edit_profile/', edit_profile, name='edit_profile'),
    path('profile/', profile, name='profile'),
]