from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import get_object_or_404, get_list_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone

#handmade
from comment.models import CommentModel, FamousCustomerModel
from comment.forms import CommentForm, FamousCustomeForm
from accounts.decorators import superuser_required


@login_required
@superuser_required
def CreateCommentView(request):
    if request.method == 'POST':
        comment_form = CommentForm(data = request.POST)
        if comment_form.is_valid():
             comment = comment_form.save(commit=False)
             if 'picture' in request.FILES:
                 comment.picture = request.FILES['picture']

             comment.save()
             return HttpResponseRedirect(reverse('accounts:dashboard'))
        else:
            print(comment_form.errors)
    else:
        comment_form = CommentForm()
    return render(request,'comment/createcomment.html',
                  {'form':comment_form})


@login_required
@superuser_required
def CommentListView(request):
    comments = CommentModel.objects.all()
    return render(request,'comment/commentlist.html',{'comments':comments})


@login_required
@superuser_required
def DeleteCommentView(request, pk):
    comment = get_object_or_404(CommentModel, pk = pk)
    comment.delete()
    return HttpResponseRedirect(reverse('comment:commentlist'))


@login_required
@superuser_required
def CreateFamousCustomerView(request):
    if request.method == 'POST':
        famouscustomer_form = FamousCustomeForm(data = request.POST)
        if famouscustomer_form.is_valid():

             logo = famouscustomer_form.save(commit=False)
             if 'picture' in request.FILES:
                logo.picture = request.FILES['picture']
             logo.save()
             return HttpResponseRedirect(reverse('accounts:dashboard'))
        else:
            print(famouscustomer_form.errors)
    else:
        famouscustomer_form = FamousCustomeForm()
    return render(request,'comment/createfamouscustomer.html',
                  {'form':famouscustomer_form})


@login_required
@superuser_required
def FamousCustomerListView(request):
    try:
        famouscustomers = get_list_or_404(FamousCustomerModel)
        return render(request,'comment/famouscustomerlist.html',
                      {'famouscustomers':famouscustomers})
    except:
        return render(request,'comment/famouscustomerlist.html')



@login_required
@superuser_required
def FamousCustomerDeleteView(request, pk):
    famouscustomers = get_object_or_404(FamousCustomerModel, pk = pk)
    famouscustomers.delete()
    return HttpResponseRedirect(reverse('comment:famouscustomerlist'))
