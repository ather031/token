from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.http import Http404
from django.db import transaction
from api.decorator import permission_required
from api.models import User, Role
from api.models.partof import PartOf
from api.serializers import UserSerializer

class UserDetailView(APIView):
    permission_classes = (IsAuthenticated, )

    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    @permission_required(['user_read','appointment_read'])
    def get(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserSerializer(user, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    @permission_required(['user_update','patient_update_hospital'])
    def put(self, request, pk, format=None):
        try:
            data = request.data
            username = data.get('username', None)
            first_name = data.get('first_name', None)
            last_name = data.get('last_name', None)
            role = data.get('role', None)
            if not username or not first_name or not last_name or not role:
                return Response({'msg': 'Invalid data'}, status=status.HTTP_400_BAD_REQUEST)

            with transaction.atomic():
                user = self.get_object(pk)
                user.username = username
                user.first_name = first_name
                user.last_name = last_name
                user.save()
                try:
                    role = Role.objects.get(pk=role)
                except:
                    return Response({'msg':'Invalid Role id'}, status=status.HTTP_400_BAD_REQUEST)
                part_of = PartOf.objects.get(user=user)
                part_of.role = role
                part_of.save()
            return Response({'msg': 'User updated successfully' , 'user' : data }, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({'msg': e.args[0]}, status=status.HTTP_400_BAD_REQUEST)

    @permission_required(['user_delete'])
    def delete(self, request, pk, format=None):
        user = self.get_object(pk)
        user.delete()
        return Response({'msg': 'User deleted successfully'}, status=status.HTTP_200_OK)
