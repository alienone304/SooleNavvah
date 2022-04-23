from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import get_object_or_404, get_list_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone

#handmade
from comment.models import CommentModel
from comment.forms import CommentForm
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
    return HttpResponseRedirect(reverse('comment:list'))
