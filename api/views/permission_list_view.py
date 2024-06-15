from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from api.models import Permission
from api.serializers.permission_serializer import PermissionSerializer


class PermissionListView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        permissions = Permission.objects.all()
        data = PermissionSerializer(permissions, many=True).data
        return Response(data=data, status=status.HTTP_200_OK)
