from api.serializers import ChangePasswordSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import GenericAPIView
from api.models import User
from django.http import Http404
from rest_framework.response import Response
from rest_framework import status

class UserChangePasswordView(GenericAPIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, *args, **kwargs):
        try:
            new = request.data.get('new_password')
            confirm = request.data.get('confirm_new')
            user = request.data.get('user')
            if new != confirm:
                return Response({'msg': 'Password not matched'}, status=status.HTTP_400_BAD_REQUEST)
            else:    
                user_obj = User.objects.get(id=user)
                user_obj.set_password(new)
                user_obj.save()
                return Response({'msg': 'Password Successfully Changed'}, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({'msg': e.args[0]}, status=status.HTTP_400_BAD_REQUEST)