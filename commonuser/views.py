from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils.text import slugify
from django.contrib.auth.decorators import login_required
import jdatetime
import datetime
from django.conf import settings
from django.utils import timezone

#handmade
from accounts.forms import UserForm
from accounts.models import UserModel
from commonuser.models import CommonUserModel
from accounts.decorators import superuser_required


@login_required
@superuser_required
def CommonUserSignupView(request):

        if request.method == 'POST':

            user_form = UserForm(data = request.POST)

            if user_form.is_valid():
                name =  user_form.cleaned_data.get('name')
                password1 =  user_form.cleaned_data.get('password1')
                username = user_form.cleaned_data.get('username')
                user = UserModel.objects.create(username=username, password=password1,
                                            name = name)
                user.is_active = True
                user.is_commonuser = True
                # hashing password
                user.set_password(user.password)
                user.save()

                commonuser = CommonUserModel.objects.create(user=user)
                commonuser.save()
                return HttpResponseRedirect(reverse('accounts:login'))


            else:
                print(user_form.errors)


        else:
            user_form = UserForm()

        return render(request,'commonuser/commonusersignup.html',
                              {'user_form':user_form})
