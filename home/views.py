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


def profiles_search(request):
    query = request.GET.get('query')

    mentors_list = models.Mentor_Profile.objects.filter(short_description__contains=query)
    mentors_list = mentors_list.union(models.Mentor_Profile.objects.filter(long_description__contains=query))
    mentors_list = mentors_list.union(models.Mentor_Profile.objects.filter(department__contains=query))
    mentors_list = mentors_list.union(models.Mentor_Profile.objects.filter(role__contains=query))
    mentors_list = mentors_list.union(models.Mentor_Profile.objects.filter(username__first_name__contains=query))
    mentors_list = mentors_list.union(models.Mentor_Profile.objects.filter(username__last_name__contains=query))
    mentors_list = mentors_list.union(models.Mentor_Profile.objects.filter(hall__contains=query))

    return render(request,'team.html',{'query_profiles':mentors_list,})
