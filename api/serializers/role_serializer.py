from rest_framework import serializers
from api.models import Role
from .permission_serializer import PermissionSerializer
from .user_serializer import UserSerializer


class RoleSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(fields=('id', 'username', 'email'))
    updated_by = UserSerializer(fields=('id', 'username', 'email'))
    permissions = PermissionSerializer(many=True, read_only=True)

    class Meta:
        model = Role
        fields = '__all__'
