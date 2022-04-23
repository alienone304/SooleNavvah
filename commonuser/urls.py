from django.urls import include, path
from django.contrib.auth import views as auth_views
from commonuser.views import CommonUserSignupView

app_name ='commonuser'
urlpatterns = [
    path('commonuser-signup/',CommonUserSignupView, name='commonusersignup'),

]
