from django.urls import include, path
from comment.views import (CreateCommentView, CommentListView, DeleteCommentView,
                    FamousCustomerListView, CreateFamousCustomerView, FamousCustomerDeleteView)

app_name ='comment'
urlpatterns = [
    path('create-comment/',CreateCommentView, name = 'createcomment'),
    path('comment-list/',CommentListView, name = 'commentlist'),
    path('delete-comment/<int:pk>/',DeleteCommentView, name = 'commentdelete'),
    path('create-famous-customer/',CreateFamousCustomerView, name = 'createfamouscustomer'),
    path('famous-customer-list/',FamousCustomerListView, name = 'famouscustomerlist'),
    path('delete-famous-customer/<int:pk>/',FamousCustomerDeleteView, name = 'famouscustomerdelete'),

]
