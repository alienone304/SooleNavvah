from django.urls import include, path
from comment.views import (CreateCommentView, CommentListView, DeleteCommentView)

app_name ='comment'
urlpatterns = [
    path('create-comment/',CreateCommentView, name = 'createcomment'),
    path('comment-list/',CommentListView, name = 'commentlist'),
    path('delete-comment/<int:pk>/',DeleteCommentView, name = 'commentdelete'),



]
