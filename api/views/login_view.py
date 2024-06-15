from django.middleware import csrf
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework import status
from api.models.partof import PartOf
from api.util import (set_access_cookies, set_refresh_cookies, get_tokens_for_user, combine_role_permissions)
from api.serializers import UserSerializer, RoleSerializer
from django.utils import timezone
from rest_framework.permissions import AllowAny


class LoginView(APIView):
    authentication_classes = ()
    permission_classes = (AllowAny,)

    def post(self, request):
        data = request.data
        response = Response()
        username = data.get('username', None)
        password = data.get('password', None)
        user = authenticate(username=username, password=password)
        if user is not None:
            part_of = PartOf.objects.get(user=user)
            permissions = combine_role_permissions(part_of.role)
            data = get_tokens_for_user(user, is_patient=False)
            set_access_cookies(response, data['access'])
            set_refresh_cookies(response, data['refresh'])
            csrf.get_token(request)
            data = UserSerializer(user, context={'request': request}).data
            data['roles'] = RoleSerializer(part_of.role).data
            data['permissions'] = permissions
            response.status_code = status.HTTP_200_OK
            response.data = {"msg": "Login successfully", "user": data}
            user.last_login = timezone.now()
            user.save()
            return response
        else:
            return Response({"msg": "Invalid credentials"}, status=status.HTTP_404_NOT_FOUND)
