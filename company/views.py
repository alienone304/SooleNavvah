from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.forms import modelformset_factory
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.core.paginator import Paginator
from django.shortcuts import get_list_or_404

from .models import ContactUsModel
from .forms import ContactUsForm
from accounts.decorators import superuser_required


def AboutUsView(request):
    return render(request,'company/about-us.html')


def SalonView(request):
    return render(request,'company/salon.html')


def SteelBuildingView(request):
    return render(request,'company/steelbuilding.html')


def FAQsView(request):
    return render(request,'company/faqs.html')


def ContactUsView(request):
    if request.method == 'POST':
        contactus_form = ContactUsForm(data = request.POST)
        if contactus_form.is_valid():
             contactus = contactus_form.save(commit=False)
             contactus.save()
             return HttpResponseRedirect(reverse('company:contact-us-success'))
        else:
            print(contactus_form.errors)
    else:
        contactus_form = ContactUsForm()
    return render(request,'company/contact-us.html',
                  {'contactus_form':contactus_form})



@login_required
@superuser_required
def ContactUsListView(request):
    try:
        contactus_list = get_list_or_404(ContactUsModel.objects.order_by('created_at'))
        return render(request,'company/contact-us-list.html',
                      {'contactus_list':contactus_list})
    except:
        return render(request,'company/contact-us-list.html')


@login_required
@superuser_required
def ContactUsDeleteView(request, pk):
    contactus = get_object_or_404(ContactUsModel, pk = pk)
    contactus.delete()
    return HttpResponseRedirect(reverse('company:contact-us-list'))


def ContactUsSuccessView(request):
    return render(request,'company/contact-us-success.html')
