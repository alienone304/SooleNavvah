from django.db import models
from django.utils import timezone

 
class ProjectsModel(models.Model):

    project_name = models.CharField(max_length = 264, blank = False, null = False)
    customer_name = models.CharField(max_length = 264, blank = True, null =True)
    address = models.TextField(null = False, blank = False)
    length = models.CharField(max_length = 264, blank = False, null = False)
    width = models.CharField(max_length = 264, blank = False, null = False)
    height = models.CharField(max_length = 264, blank = False, null = False)
    use_type = models.CharField(max_length = 264, blank = False, null =False)
    roof_type = models.CharField(max_length = 264, blank = False, null =False)
    is_local = models.BooleanField(default = True, null = False)
    date_of_project = models.CharField(max_length = 264, null = False, blank = False)

    contact_info = models.TextField(null = True, blank = True)
    description = models.TextField(null = True, blank = True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        string = self.project_name + " (" + self.customer_name + ")"
        return string


class ProjectPictureModel(models.Model):
    project = models.ForeignKey(ProjectsModel, on_delete = models.CASCADE,
                               related_name = 'pictures')
    picture = models.ImageField(blank = True, null = True,
                                upload_to=r'projects')
    description = models.TextField(null = True, blank = True)
    created_at = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        try:
            name = self.picture.name.lower()
            if name.endswith('.jpg') or name.endswith('.png') or name.endswith('.jpeg'):
                pass
            else:
                self.picture = None
        except:
            pass
        super(ProjectPictureModel, self).save(*args, **kwargs)
