from django.shortcuts import render, HttpResponse
from home import models

# Create your views here.
def index(request):
    return render(request, 'index.html')

def profiles(request):
    mentor_profiles = models.Mentor_Profile.objects.all()
    return render(request, 'team.html', {'mentor_profiles':mentor_profiles,})

def contact(request):
    return render(request, 'contact.html')
