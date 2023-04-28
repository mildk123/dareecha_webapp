from django.db import models
from baham.enum_types import VehicleType
# Create your models here.


class VehicleModel(models.Model):
    model_id = models.AutoField(primary_key=True, db_column='id')
    vendor = models.CharField(max_length=20, null=False, blank=False)
    model = models.CharField(max_length=20, null=False, blank=False)
    type = models.CharField(max_length=50, choices=[(tag.name, tag.value) for tag in VehicleType], help_text="Select Vehicle Type")
    capacity = models.PositiveSmallIntegerField(null=False, default=2)