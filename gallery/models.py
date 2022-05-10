from django.db import models
from model_utils.models import TimeStampedModel


class GalleryPhoto(TimeStampedModel):
    image = models.ImageField(upload_to='gallery_photos')
    caption = models.CharField(max_length=256)
    attenders = models.TextField(help_text='All attenders comma or new line seperated here')
    shooting_date = models.DateField()
    publishing_year = models.IntegerField()
