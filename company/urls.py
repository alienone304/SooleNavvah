from django.urls import include, path
from company.views import (ContactUsView, AboutUsView, ContactUsListView,
                            ContactUsDeleteView,FAQsView, ContactUsSuccessView,
                            SteelBuildingView, SalonView)

app_name ='company'
urlpatterns = [
    path('about-us/',AboutUsView, name = 'aboutus'),
    path('FAQs/',FAQsView, name = 'faqs'),
    path('steelbuilding/',SteelBuildingView, name = 'steelbuilding'),
    path('salon/',SalonView, name = 'salon'),
    path('contact-us/',ContactUsView, name = 'contactus'),
    path('contact-us-list/',ContactUsListView, name = 'contact-us-list'),
    path('contact-us-delete/<int:pk>/',ContactUsDeleteView, name = 'contact-us-delete'),
    path('contact-us-success/',ContactUsSuccessView, name = 'contact-us-success'),


]
