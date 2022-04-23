from django.urls import include, path
from django.contrib.auth import views as auth_views
from accounts.forms import UserLoginForm
from accounts.views import SuperUserDashboardView

app_name ='accounts'
urlpatterns = [
    path('dashboard/',SuperUserDashboardView, name='dashboard'),
    path('auth/',auth_views.LoginView.as_view(template_name='registration/login.html',authentication_form=UserLoginForm), name='login'),

]
