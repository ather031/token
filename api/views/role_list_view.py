from api.decorator import permission_required
from api.serializers import RoleSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from api.models import Role, Permission
from django.db import transaction
from rest_framework.generics import ListAPIView
from api.filters import RoleFilter

class RoleListView(ListAPIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = RoleSerializer
    filterset_class = RoleFilter

    @permission_required(['role_read'])
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
        

    def get_queryset(self):
        return Role.objects.all().order_by('-id')

    @permission_required(['role_create'])
    def post(self, request, *args, **kwargs):
        try:
            data = request.data

            name = data.get('name', None)
            code_name = data.get('code_name', None)
            permission_data = data.get('permissions', None)

            if not name or not code_name or permission_data is None:
                return Response({'msg': 'Invalid data'}, status=status.HTTP_400_BAD_REQUEST)

            permissions_data = data.pop('permissions')

            with transaction.atomic():
                role = Role(**data)
                role.created_by = request.user
                role.updated_by = request.user
                role.save()

                for perm in permissions_data:
                    permission = Permission.objects.get(pk=perm['id'])
                    role.permissions.add(permission)

                role.save()

            return Response({'msg': 'Role created successfully'}, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({'msg': 'Server error'}, status=status.HTTP_400_BAD_REQUEST)
