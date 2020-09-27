from django.shortcuts import render
from .models import Projects

def index(request):
    projects = Projects.objects
    return render(request,'projects/index.html',{'projects' : projects})