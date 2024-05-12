from django.shortcuts import render, get_object_or_404
from .models import *
from users.models import *

# Create your views here.
def faculty_list(request):
    faculty_result_set = Faculty.objects.all()
    context = {
        "faculty_result_set": faculty_result_set,
    }

    return render(request, "faculty/faculty_list.html", context)

def faculty_details(request, faculty_id:int):
    faculty = get_object_or_404(Faculty, id=faculty_id)
    faculty_details = [
        ('Name', faculty.user.first_name + " " + faculty.user.last_name),
        ('Designation', faculty.designation),
        ('Department', faculty.department),
        ('Shift', faculty.shift),
        ('E-Mail ID', faculty.user.email),
    ]

    faculty_education = Education.objects.filter(faculty=faculty)
    faculty_experience = Experience.objects.filter(faculty=faculty)
    faculty_pub = Publication.objects.filter(faculty=faculty)

    # TODO: Implement experience, education, publication
    context = {
        "faculty_details": faculty_details,
        "faculty_name": faculty.user.first_name + " " + faculty.user.last_name,
        "faculty_experience": faculty_education, # TBD
        "faculty_education": faculty_experience,  # TBD
        "faculty_publications": faculty_pub, #TBD
    }
    return render(request, "faculty/faculty_details.html", {"faculty_details": faculty_details})def faculty_list(request):
    return render(request, 'home/faculty_list.html',)


def faculty_profile(request):
    return render(request, 'faculty/profile.html')
