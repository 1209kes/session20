from django.shortcuts import render
from .models import Post

# Create your views here.
def detail(request, post_id):
    post = Post.objects.get(pk =post_id)
    return render(request, 'detail.html', {'post': post})

def list(request):
    posts = Post.objects.all()

    return render(request, 'list.html', {'posts': posts})