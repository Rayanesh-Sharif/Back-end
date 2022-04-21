from rest_framework.views import APIView
from rest_framework.response import Response

from .models import BlogPost
from .serializers import BlogPostSerializer


class BlogPostList(APIView):

    def get(self, request):
        blogposts = BlogPost.objects.all()
        serializer = BlogPostSerializer(blogposts, many=True)
        return Response(serializer.data)


class BlogPostDetail(APIView):

    def get(self, request, pk):
        blogpost = BlogPost.objects.get(pk=pk)
        serializer = BlogPostSerializer(blogpost)
        return Response(serializer.data)
