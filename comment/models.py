from django.db import models
from projects.models import ProjectsModel
from django.utils import timezone


class CommentModel(models.Model):
    project = models.ForeignKey(ProjectsModel, null = True, blank = True,
                        on_delete = models.SET_NULL, related_name = 'comments')
    project_name = models.CharField(max_length = 264, null = True, blank = True)
    person_name = models.CharField(max_length = 264, null = False, blank = False)
    comment = models.TextField(null = False, blank = False)
    picture = models.ImageField(blank = False, null = False,
                                upload_to=r'comment', default = r'comment/default/default.jpg')
    created_at = models.DateTimeField(default=timezone.now)                            
