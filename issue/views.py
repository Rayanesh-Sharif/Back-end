from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Issue
from .serializers import IssueSerializer


class IssueList(APIView):

    def get(self, request):
        issues = Issue.objects.all()
        serializer = IssueSerializer(issues, many=True)
        return Response(serializer.data)


class IssueDetail(APIView):

    def get(self, request, pk):
        issue = Issue.objects.get(pk=pk)
        serializer = IssueSerializer(issue)
        return Response(serializer.data)
