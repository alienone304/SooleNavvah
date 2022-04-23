from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import get_object_or_404, get_list_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone

#handmade
from ordering.models import OrderingModel
from ordering.forms import OrderingForm
from accounts.decorators import superuser_required


def OrderingView(request):
    if request.method == 'POST':
        ordering_form = OrderingForm(data = request.POST)
        if ordering_form.is_valid():
             ordering = ordering_form.save(commit=False)
             if 'type' in request.POST:
                 type = request.POST['type']
             else:
                 type = False
             if type == "1":
                 ordering.is_double_side_inclined = True
             if type == "2":
                 ordering.is_curved = True
             if type == "3":
                 ordering.is_single_side_inclined = True
             if 'use' in request.POST:
                 use = request.POST['use']
             else:
                 use = False
             if use == "1":
                 ordering.is_salon = True
             if use == "2":
                 ordering.is_salon = False


             if 'has_child_salon' in request.POST:
                 has_child_salon = request.POST['has_child_salon']
             else:
                 has_child_salon = False
             if has_child_salon == "1":
                 ordering.has_child_salon = False
             if has_child_salon == "2":
                 ordering.has_child_salon = True


             if 'has_half_floor' in request.POST:
                 has_half_floor = request.POST['has_half_floor']
             else:
                 has_half_floor = False
             if has_half_floor == "1":
                 ordering.has_half_floor = False
             if has_half_floor == "2":
                 ordering.has_half_floor = True


             if 'has_crane' in request.POST:
                 has_crane = request.POST['has_crane']
             else:
                 has_crane = False
             if has_crane == "1":
                 ordering.has_crane = False
             if has_crane == "2":
                 ordering.has_crane = True

             ordering.save()
             return HttpResponseRedirect(reverse('ordering:order-success'))
        else:
            print(ordering_form.errors)
    else:
        ordering_form = OrderingForm()
    return render(request,'ordering/order.html',
                  {'form':ordering_form})


def OrderSuccessView(request):
    return render(request,'ordering/order-success.html')


@login_required
@superuser_required
def OrderListView(request):
    orders = OrderingModel.objects.all()
    return render(request,'ordering/list.html', {'orders':orders})


@login_required
@superuser_required
def OrderDeleteView(request, pk):
    order = get_object_or_404(OrderingModel, pk = pk)
    order.delete()
    return HttpResponseRedirect(reverse('ordering:orderlist'))
