from rest_framework.views import APIView
from rest_framework.response import Response

from .models import GalleryPhoto
from .serializers import GalleryPhotoSerializer


class GalleryList(APIView):

    def get(self, request):
        gallery_photos = GalleryPhoto.objects.all()
        serializer = GalleryPhotoSerializer(gallery_photos, many=True)
        return Response(serializer.data)


class GalleryDetail(APIView):

    def get(self, request, pk):
        gallery_photo = GalleryPhoto.objects.get(pk=pk)
        serializer = GalleryPhotoSerializer(gallery_photo)
        return Response(serializer.data)
