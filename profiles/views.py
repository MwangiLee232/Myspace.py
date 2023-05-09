from django.shortcuts import render
from .models import Profile

def profile_view(request, username):
    profile = Profile.objects.get(username=username)
    return render(request, 'profiles/profile.html', {'profile': profile})
