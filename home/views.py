from django.shortcuts import render, HttpResponse
from home import models
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    return render(request, 'index.html')

def profiles(request):
    mentor_profiles = models.Mentor_Profile.objects.all()
    return render(request, 'team.html', {'mentor_profiles':mentor_profiles,})

def contact(request):
    return render(request, 'contact.html')

@login_required
def mentor(request):

    if request.method == 'POST':
        user = request.user
        username = user.username
        role = request.POST.get('role')
        department = request.POST.get('department')
        contact = request.POST.get('contact')
        year = request.POST.get('year')
        alt_email = request.POST.get('alt_email')
        photo = request.FILES.get('photo')
        short_description = request.POST.get('short_description')
        long_description = request.POST.get('long_description')
        hall = request.POST.get('hall')
        facebook_link = request.POST.get('facebook_link')
        linkedin_link = request.POST.get('linkedin_link')

        user_profile = models.Mentor_Profile()
        user_profile.username = user
        user_profile.role = role
        user_profile.department = department
        user_profile.contact = contact
        user_profile.year = year
        user_profile.alt_email = alt_email
        user_profile.short_description = short_description
        user_profile.long_description = long_description
        user_profile.hall = hall
        user_profile.facebook_link = facebook_link
        user_profile.linkedin_link = linkedin_link
        if photo:
            fs = FileSystemStorage()
            filename = fs.save(photo.name, photo)
            uploaded_file_url = fs.url(filename)
            user_profile.photo = filename

            # print(fs)
            print("filename", filename)
            print("Uploaded file url", uploaded_file_url)
            print(user_profile)
        user_profile.save()

        return HttpResponse("Your account has been created")

    return render(request, 'mentor.html')
