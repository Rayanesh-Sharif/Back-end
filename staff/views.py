from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Staff
from .serializers import StaffSerializer


class StaffView(APIView):
    
    def get(self, request):
        staffs = Staff.objects.all()
        serializer = StaffSerializer(staffs, many=True)
        return Response(serializer.data)
