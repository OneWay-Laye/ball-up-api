from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from rest_framework import generics, status
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView

from ..models.park import Park
from ..serializers import ParkSerializer

# Create your view here.
class Parks(APIView):
    """Request dealing with all Parks"""
    permission_classes = ()
    def get(self, request):
        """Index Parks"""

        parks = Park.objects.all()

        data = ParkSerializer(parks, many=True).data

        return Response({ 'parks': data })

class ParkDetail(APIView):
    """Request dealing with a single Park"""
    permission_classes = ()
    def get(self, request, pk):
        """Show Park"""
        park = get_object_or_404(Parks, pk=pk)

        data = ParkSerializer(park).data

        return Response({ 'park': data })
