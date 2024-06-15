from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.db import transaction
from api.decorator import permission_required
from api.models import Role, User
from api.models.partof import PartOf
from api.serializers import UserSerializer
from rest_framework.generics import ListAPIView
from api.util import CustomPagination
from django.db import IntegrityError
from api.filters import UserFilter

class UserListView(ListAPIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = UserSerializer
    pagination_class = CustomPagination
    filterset_class = UserFilter

    @permission_required(['user_read'])
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        return User.objects.all().order_by('-id')


    @permission_required(['user_create'])
    def post(self, request, *args, **kwargs):
        try:
            data = request.data
            username = data.get('username', None)
            first_name = data.get('first_name', None)
            last_name = data.get('last_name', None)
            password = data.get('password', None)
            role = data.get('role', None)

            if not username or not first_name or not last_name or not password or not role:
                return Response({'msg': 'Invalid data'}, status=status.HTTP_400_BAD_REQUEST)

            with transaction.atomic():
                user = User.objects.create_user(
                    username=username, first_name=first_name, last_name=last_name,password=password
                )
                user.created_by = request.user
                user.updated_by = request.user
                user.save()
                try:
                    role = Role.objects.get(id=role)
                except:
                    return Response({'msg':'Invalid role ID'}, status=status.HTTP_400_BAD_REQUEST)
                part_of = PartOf.objects.create(user=user, role=role)
                part_of.save()
            return Response({'msg': 'User created successfully'}, status=status.HTTP_200_OK)
        
        except IntegrityError as e:
            print(e.args)
            if 'UNIQUE constraint failed: api_user.mobile' in e.args:
                return Response({'msg':'User with this mobile number already exists'}, status=status.HTTP_400_BAD_REQUEST)
            elif 'UNIQUE constraint failed: api_user.username' in e.args:
                return Response({'msg':'User with this username already exists'}, status=status.HTTP_400_BAD_REQUEST)
            return Response({'msg': 'Integrity Error'}, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            print(e)
            return Response({'msg': 'Server error'}, status=status.HTTP_400_BAD_REQUEST)
