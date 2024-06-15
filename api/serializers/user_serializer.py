from .dynamic_fields_model_serializer import DynamicFieldsModelSerializer
from api.models import User, role
from rest_framework import serializers


class UserSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = User
        exclude = ('password', 'last_login', )

    def to_representation(self, instance):
        role = instance.partof.role
        instance = super().to_representation(instance)
        instance['role'] = role.id
        instance['role_name'] = role.name
        instance['code_name'] = role.code_name
        return instance

class UserUpdateSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = User
        exclude = ('password', 'last_login', )
