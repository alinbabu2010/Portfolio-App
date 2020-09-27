from django.shortcuts import render,get_object_or_404
from .models import Projects

def index(request):
    projects = Projects.objects
    return render(request, 'projects/index.html', {'projects': projects})
    
def detail(request, project_id):
    project_detail = get_object_or_404(Projects,pk=project_id)
    return render(request,'projects/details.html',{'project' : project_detail })