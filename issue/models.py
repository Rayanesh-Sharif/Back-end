from django.db import models
from model_utils.models import TimeStampedModel


class Issue(TimeStampedModel):
    raw_file = models.FileField(upload_to='files/issues/')
    cover_image = models.ImageField(upload_to='media/issue_cover_images')
    name = models.CharField(max_length=128)
    authors = models.TextField(help_text='Authors list comma or new line seperated here')
    subject = models.CharField(max_length=32)
    pages_number = models.IntegerField()
    Pressing_date = models.DateField()

