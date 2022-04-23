from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Handmade
from accounts.decorators import superuser_required


@login_required
@superuser_required
def SuperUserDashboardView(request):
    return render(request,'accounts/superuserdashboard.html')
