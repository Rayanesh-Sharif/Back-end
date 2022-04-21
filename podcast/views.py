from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Podcast
from .serializers import PodcastSerializer


class PodcastList(APIView):

    def get(self, request):
        podcasts = Podcast.objects.all()
        serializer = PodcastSerializer(podcasts, many=True)
        return Response(serializer.data)


class PodcastDetail(APIView):

    def get(self, request, pk):
        podcast = Podcast.objects.get(pk=pk)
        serializer = PodcastSerializer(podcast)
        return Response(serializer.data)
