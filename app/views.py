from django.shortcuts import render, redirect

from app.form import ContactModelForm
from app.models import Skill, Project, Blog


def index_view(request):
    skills = Skill.objects.all()
    projects = Project.objects.all()
    blogs = Blog.objects.all()
    return render(request=request,
                  template_name='app/index.html',
                  context={"skills":skills,
                           "projects":projects,
                           "blogs":blogs})


def project_view(request, project_id):
    project = Project.objects.filter(id=project_id).first()
    return render(request=request,
                  template_name='app/project.html',
                  context={"project":project})


def blog_view(request, blog_id):
    blog = Blog.objects.filter(id=blog_id).first()
    return render(request=request,
                  template_name='app/blog.html',
                  context={"blog":blog})


def add_contact(request):
    if request.method == "POST":
        form = ContactModelForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    form = ContactModelForm()

    return render(request=request,
                  template_name='app/index.html',
                  context={"form":form}
                  )