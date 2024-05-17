

from django.contrib import admin
from django.urls import path, include
from .views import *

app_name = "fams"

urlpatterns = [
    path('faculty_list/', faculty_list, name="faculty_list"),
    path('profile/<int:faculty_id>/', faculty_profile, name="faculty_profile"),
]