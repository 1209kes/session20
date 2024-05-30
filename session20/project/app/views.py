from django.shortcuts import render
from .models import Post

# Create your views here.
def detail(request, article_id):
    article = Post.objects.get(pk =article_id)
    return render(request, 'detail.html', {'article': article})