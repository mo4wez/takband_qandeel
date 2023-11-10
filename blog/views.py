from django.shortcuts import render
from django.views import generic

from .models import Post

class PostListView(generic.ListView):
    queryset = Post.objects.filter(active=True, status=Post.POST_PUBLISHED).all()
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    ordering = 'title'


class PostDetailView(generic.DeleteView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

