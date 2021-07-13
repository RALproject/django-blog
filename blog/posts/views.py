from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Post

# Create your views here.

def index(request):
    posts_obj = Post.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(posts_obj, 3)

    posts = paginator.page(page)
    return render(request, 'index.html', {'posts': posts})

def post(request, pk):
    post = Post.objects.get(id=pk)
    return render(request, 'post.html', {'post': post})
