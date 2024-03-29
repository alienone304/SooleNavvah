"""SooleNavvah URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import HomeView, ChangeLanguage

urlpatterns = [
    path('custom-admin/', admin.site.urls),
    path('',include('django.contrib.auth.urls')),
    path('',HomeView,name = 'home'),
    path('lang/',ChangeLanguage,name = 'change_language'),
    path('superuser/', include('accounts.urls',namespace = 'accounts')),
    path('commonuser/', include('commonuser.urls',namespace = 'commonuser')),
    path('gallery/', include('gallery.urls',namespace = 'gallery')),
    path('company/', include('company.urls',namespace = 'company')),
    path('projects/', include('projects.urls',namespace = 'projects')),
    path('comment/', include('comment.urls',namespace = 'comment')),
    path('ordering/', include('ordering.urls',namespace = 'ordering')),
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
