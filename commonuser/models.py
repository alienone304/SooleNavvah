from django.db import models
from django.utils import timezone
from django.db import models
from django.conf import settings

class CommonUserModel(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete = models.CASCADE,
                               related_name='commonusers', primary_key = True)
    created_at = models.DateTimeField(default=timezone.now)                           

    def __str__(self):
        return self.user.username
