from django.db import models


class Staff(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    position = models.CharField(max_length=64)
    image = models.ImageField(upload_to='staff_images')
    present_in_landing_page = models.BooleanField(default=False)
