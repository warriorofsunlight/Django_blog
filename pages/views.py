from django.shortcuts import render
from django.views.generic import TemplateView
from posts.models import Post


# Create your views here.

def home(request):
    return render(request, 'home/home.html')


class HomeView(TemplateView):
    model = Post
    template_name = 'home/home.html'
    context_object_name = 'posts'
    ordering = ['-created_at']
