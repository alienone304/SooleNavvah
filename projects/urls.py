from django.urls import include, path
from projects.views import (CreateProjectView, ProjectListView, ProjectDetailView,
                            ProjectDeleteView, ProjectUpdateView, ProjectPictureUpdateView,
                            ProjectPictureAddView)

app_name ='projects'
urlpatterns = [
    path('create-project/',CreateProjectView, name = 'createproject'),
    path('project-list/',ProjectListView, name = 'projectlist'),
    path('project-detail/<int:pk>/',ProjectDetailView, name = 'projectdetail'),
    path('project-delete/<int:pk>/',ProjectDeleteView, name = 'projectdelete'),
    path('project-update/<int:pk>/',ProjectUpdateView, name = 'projectupdate'),
    path('picture-update/<int:pk>/',ProjectPictureUpdateView, name = 'projectpictureupdate'),
    path('picture-add/<int:pk>/',ProjectPictureAddView, name = 'projectpictureadd'),


]
