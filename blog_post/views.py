from django.shortcuts import render
from .models import Post
# Create your views here.

def home(request):
    all_post = Post.objects.all()
    context = {
        'all_post_list': all_post
    }
    return render(request, 'index.html', context)

def contact_list(request):
    return render(request, 'contact.html')

def all_posts(request):
    post_list = Post.objects.all()
    context = {
        'post_list': post_list
    }
    return render(request, 'all_post.html', context)

def single_post(request, id):
    post = Post.objects.get(pk=id)
    print(post)
    return render(request, 'single_post.html', {'post':post})
