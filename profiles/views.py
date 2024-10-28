from django.shortcuts import render

# Create your views here.
import subprocess
from django.http import HttpResponse
from django.shortcuts import render
from .forms import ProfileForm

def create_profile(request):
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST)

        if profile_form.is_valid():
            profile = profile_form.save()

            # Trigger the resume generation script after saving the form data
            run_resume_script(profile.id)  # Pass the profile ID
            
            return HttpResponse("Resume generated successfully!")  # Redirect or success message

    else:
        profile_form = ProfileForm()

    return render(request, 'profiles/profile_form.html', {
        'profile_form': profile_form,
    })

def run_resume_script(profile_id):
    """Trigger external Python script to generate the resume."""
    script_path = '/path/to/your/resume_script.py'
    subprocess.run(['python3', script_path, str(profile_id)])
