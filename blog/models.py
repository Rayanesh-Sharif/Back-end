from django.db import models
from model_utils.models import TimeStampedModel


class BlogPost(TimeStampedModel):
    post_text = models.TextField()
    post_image = models.ImageField(upload_to='media/blog_post_images')
    name = models.CharField(max_length=64)
    contributors = models.TextField(help_text='All contributors comma or new line seperated here')
    subject = models.CharField(max_length=32)
    reading_time = models.IntegerField()
    posting_date = models.DateField()
