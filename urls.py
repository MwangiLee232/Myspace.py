from django.urls import path
from profiles.views import profile_view

urlpatterns = [
    path('profiles/<str:username>/', profile_view, name='profile'),
]
