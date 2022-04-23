from django.db import models
from django.utils import timezone
from django.db import models

class GalleryModel(models.Model):
    picture = models.ImageField(default = r'gallery/default/default.jpg',
                                 upload_to=r'gallery/')
    description = models.TextField(null = True, blank = True)
    created_at = models.DateTimeField(default=timezone.now)
