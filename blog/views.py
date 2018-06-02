from django.shortcuts import render, get_object_or_404
from .models import Post, Category
from django.views.generic import ListView


class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 10
    template_name = 'blog/post_list.html'


def post_detail(request, category, slug):
    post = Post.published.get(category__name=category, slug=slug)
    return render(request, 'blog/post_detail.html', {'post': post})


def cat_detail(request, name):
    cat_posts = Post.published.filter(category__name=name)
    return render(request, 'blog/cat_detail.html', {'cat_posts': cat_posts})
