from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .forms import PostForm, EditForm


# Create your views here.
class HomePageView(ListView):
    model = Post
    template_name = "home_page.html"

class ArticleDetailView(DetailView):
    model = Post
    template_name = "article.html"

class AddPostView(CreateView):
    # view to add new post.
    model = Post
    form_class = PostForm
    template_name = "add_post.html"
    
class EditPostView(UpdateView):
   # View to edit post.
    model = Post
    form_class = EditForm
    template_name = "edit_post.html"