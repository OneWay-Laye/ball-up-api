from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied

from ..models.meet_up import MeetUp
from ..serializers import MeetUpSerializer, MeetUpReadSerializer

class MeetUpIndex(APIView):
    """This will be for all Index"""
    permission_classes=()
    def get(self, request):
        """Index request"""
        meetups = MeetUp.objects.all()

        data = MeetUpReadSerializer(meetups, many = True).data
        return Response(data)

class MeetUpCreate(APIView):
    """This will be for Create views"""
    permission_classes=(IsAuthenticated,)
    def post(self, request):
        """Create Request"""
        print(request.data)
        request.data["meetup"]['owner'] = request.user.id
        mu = MeetUpSerializer(data=request.data['meetup'])
        if mu.is_valid():
            mu.save()
            return Response(mu.data, status=status.HTTP_200_OK)
        else:
            return Response(mu.errors, status=status.HTTP_400_BAD_REQUEST)

class MeetUpDetailsShow(APIView):
    """This will be for Show"""
    permission_classes=()
    def get(self, request, pk):
        """Show request"""
        meetup = get_object_or_404(MeetUp, pk=pk)
        data = MeetUpReadSerializer(meetup).data
        return Response(data)
class MeetUpDetailsDeleteUpdate(APIView):
    permission_classes=(IsAuthenticated,)
    def patch(self, request, pk):
        """Update Request"""
        meetup = get_object_or_404(MeetUp, pk=pk)
        if request.user != meetup.owner:
            raise PermissionDenied('You do not have accese to change meetup')

        request.data['meetup']['owner'] = request.user.id
        data = MeetUpSerializer(MeetUp, data=request.data['meetup'], partial=True)
        if data.is_valid():
            data.save()
            return Response(status=status.HTTP_202_ACCEPTED)
        return Response(data.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

    def delete(self,request, pk):
        """Delete Request"""
        meetup = get_object_or_404(MeetUp, pk=pk)
        if request.user !=meetup.owner:
            raise PermissionDenied('You dont have access to delete meetup.')
        meetup.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
