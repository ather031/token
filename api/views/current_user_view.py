from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from api.models.partof import PartOf
from api.serializers import UserSerializer, RoleSerializer
from api.util import combine_role_permissions


class CurrentUserView(APIView):

    permission_classes = (IsAuthenticated, )

    def get(self, request, format=None):
        part_of = PartOf.objects.get(user=request.user)
        permissions = combine_role_permissions(part_of.role)
        roles_data = RoleSerializer(part_of.role).data

        data = UserSerializer(request.user, context={'request': request}).data
        data['roles'] = roles_data

        data['permissions'] = permissions

        return Response({"user": data}, status=status.HTTP_200_OK)
