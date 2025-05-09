from django.shortcuts import render

# Create your views here.

def landing_home_page(request):
    return render(request, 'core/landing_page.html')

from django.shortcuts import render, get_object_or_404
from .models import Post

def post_list(request):
    posts = Post.objects.filter(published=True).order_by('-created_at')
    return render(request, 'core/post_list.html', {'posts': posts})

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug, published=True)
    return render(request, 'core/post_detail.html', {'post': post})