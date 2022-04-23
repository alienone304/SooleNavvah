from django.db import models
from django.utils import timezone


class OrderingModel(models.Model):
    #neccessary
    phone_number = models.CharField(max_length = 264, null = False, blank = False)
    length = models.CharField(max_length = 264, null = False, blank = False)
    width = models.CharField(max_length = 264, null = False, blank = False)
    address = models.TextField(null = False, blank = False)
    is_salon = models.BooleanField(default = True)

    #optional
    name = models.CharField(max_length = 264, null = True, blank = True)
    height = models.CharField(max_length = 264, null = True, blank = True)
    type_of_use = models.CharField(max_length = 264, null = True, blank = True)
    number_of_floor = models.CharField(max_length = 264, null = True, blank = True)
    has_half_floor = models.BooleanField(null = True, blank = True)
    has_child_salon = models.BooleanField(null = True, blank = True)
    has_crane = models.BooleanField(null = True, blank = True)
    crane_weight = models.CharField(max_length = 264, null = True, blank = True)

    #roof type
    is_curved = models.BooleanField(null = True, blank = True)
    is_double_side_inclined = models.BooleanField(null = True, blank = True)
    is_single_side_inclined = models.BooleanField(null = True, blank = True)

    created_at = models.DateTimeField(default=timezone.now)
