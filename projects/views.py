from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from django.forms import modelformset_factory
from django.shortcuts import get_object_or_404, get_list_or_404
from django.conf import settings
from django.utils import timezone
import datetime
from django.utils.decorators import method_decorator

#handmade
from accounts.decorators import superuser_required
from projects.models import ProjectsModel, ProjectPictureModel
from projects.forms import ProjectsForm, ProjectPictureForm, ProjectPictureUpdateForm


@login_required
@superuser_required
def CreateProjectView(request):
    imageformset = modelformset_factory(ProjectPictureModel,
                                        form=ProjectPictureForm, extra=9)
    if request.method == 'POST':
        projects_form = ProjectsForm(data = request.POST)
        formsets = imageformset(request.POST or None, request.FILES or None)

        if projects_form.is_valid() and formsets.is_valid():
             project = projects_form.save(commit=False)
             if 'is_local' in request.POST:
                 is_local = request.POST['is_local']
             else:
                 is_local = False
             if is_local == "1":
                 project.is_local = True
             if is_local == "2":
                 project.is_local = False
             formsets = imageformset(request.POST or None, request.FILES or None)
             project.save()
             for formset in formsets.cleaned_data:
                    if formset:
                        picture = formset['picture']
                        description = formset['description']
                        photo = ProjectPictureModel(project = project, picture = picture)
                        photo.save()
             return HttpResponseRedirect(reverse('accounts:dashboard'))
        else:
             print(projects_form.errors)

    else:
        projects_form = ProjectsForm()
        formsets = imageformset(queryset=ProjectPictureModel.objects.none())
    return render(request,'projects/create.html',
                          {'form':projects_form,'formsets':formsets})


def ProjectListView(request):
    projects = ProjectsModel.objects.all()
    return render(request,'projects/list.html',
                          {'projects':projects})


def ProjectDetailView(request, pk):
    project = get_object_or_404(ProjectsModel, pk = pk)
    return render(request,'projects/details.html',
                          {'project':project})


@login_required
@superuser_required
def ProjectDeleteView(request, pk):
    project = get_object_or_404(ProjectsModel, pk = pk)
    project.delete()
    return HttpResponseRedirect(reverse('projects:projectlist'))


@login_required
@superuser_required
def ProjectUpdateView(request,pk):
    project = get_object_or_404(ProjectsModel, pk = pk)

    project_update_form = ProjectsForm(request.POST or None, instance = project)
    if project_update_form.is_valid():
        project_update_form.save()
        project.save()
        return HttpResponseRedirect(reverse('projects:projectdetail',
                                    kwargs={'pk':project.pk,}))
    return render(request,'projects/update.html',
                          {'form':project_update_form,
                          'project':project,})

@login_required
@superuser_required
def ProjectPictureUpdateView(request, pk):
    pic = ProjectPictureModel.objects.get(pk=pk)
    form = ProjectPictureUpdateForm(request.POST or None,instance=pic)
    if form.is_valid():
        form.save()
        if 'picture' in request.FILES:
            pic.picture = request.FILES['picture']

        pic.save()
        return HttpResponseRedirect(reverse('projects:projectupdate',
                                    kwargs={'pk':pic.project.pk}))
    else:
        print(form.errors)
        return render(request, 'projects/pictureupdate.html', {'form':form})


@login_required
@superuser_required
def ProjectPictureAddView(request, pk):
    project = ProjectsModel.objects.get(pk=pk)
    if request.method == 'POST':
        form = ProjectPictureForm(data = request.POST)
        if form.is_valid():
            pic = form.save(commit = False)
            pic.project = project
            if 'picture' in request.FILES:
                pic.picture = request.FILES['picture']
            pic.save()
        return HttpResponseRedirect(reverse('projects:projectupdate',
                                    kwargs={'pk':pic.project.pk}))
    else:
        form = ProjectPictureForm()
    return render(request, 'projects/pictureadd.html', {'form':form})
