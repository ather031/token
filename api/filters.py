import django_filters as filters
from api.models import User, Role
from datetime import datetime

class UserFilter(filters.FilterSet):
    name                = filters.CharFilter(field_name='full_name', lookup_expr='icontains')

    class Meta:
        model = User
        fields = ['full_name']

class RoleFilter(filters.FilterSet):
    name                = filters.CharFilter(field_name='name', lookup_expr='icontains')

    class Meta:
        model = Role
        fields = ['name']
