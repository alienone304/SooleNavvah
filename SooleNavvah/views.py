from django.shortcuts import render
from projects.models import ProjectsModel
from comment.models import CommentModel


def HomeView(request):
    projects = ProjectsModel.objects.all()
    comments = CommentModel.objects.all()
    return render(request,'home.html',{'projects':projects,'comments':comments})
