from rest_framework import serializers

from .models import BlogPost


class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = ['id', 'post_text', 'post_image', 'name', 'contributors', 'subject',
                  'reading_time', 'posting_date']
