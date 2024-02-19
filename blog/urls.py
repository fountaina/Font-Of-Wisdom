from django.urls import path
from .views import HomePageView, ArticleDetailView, AddPostView


urlpatterns = [
    path('', HomePageView.as_view(), name="home_page"),
    path('article/<int:pk>/', ArticleDetailView.as_view(), name="article_detail"),
    path('add_post/', AddPostView.as_view(), name="add_post"),
]