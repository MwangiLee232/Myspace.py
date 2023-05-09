from django.urls import path
from . import views

app_name = 'myspace'

urlpatterns = [
    # Map the post list view to the URL 'posts/'
    path('posts/', views.PostListView.as_view(), name='post_list'),

    # Map the like view to the URL 'posts/<int:pk>/like/'
    path('posts/<int:pk>/like/', views.like_post, name='like_post'),
]
