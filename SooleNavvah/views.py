from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from projects.models import ProjectsModel
from comment.models import CommentModel, FamousCustomerModel


def HomeView(request):
    projects = ProjectsModel.objects.all()
    comments = CommentModel.objects.all()
    famouscustomers = FamousCustomerModel.objects.all()
    return render(request,'home.html',{'projects':projects,'comments':comments,
                    'famouscustomers':famouscustomers})


def ChangeLanguage(request):
    try:
        if request.session['lang'] == 'en':
            request.session['lang'] = 'fa'
            return HttpResponseRedirect(reverse('home'))
        else:
            request.session['lang'] = 'en'
            return HttpResponseRedirect(reverse('home'))
    except:
        pass
    request.session['lang'] = 'en'
    return HttpResponseRedirect(reverse('home'))
