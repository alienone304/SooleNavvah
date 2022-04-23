from django.urls import include, path
from ordering.views import (OrderingView, OrderSuccessView, OrderListView,
                        OrderDeleteView)

app_name ='ordering'
urlpatterns = [
    path('order/',OrderingView, name = 'order'),
    path('order-success/',OrderSuccessView, name = 'order-success'),
    path('order-list/',OrderListView, name = 'orderlist'),
    path('order-delete/<int:pk>/',OrderDeleteView, name = 'orderdelete'),

]
