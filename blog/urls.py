from django.urls import path
from .views import HomePageView, ArticleDetailView, AddPostView, EditPostView


urlpatterns = [
    path('', HomePageView.as_view(), name="home_page"),
    path('article/<int:pk>/', ArticleDetailView.as_view(), name="article_detail"),
    path('add_post/', AddPostView.as_view(), name="add_post"),
    path('article/edit/<int:pk>/', EditPostView.as_view(), name='edit_post')
]
