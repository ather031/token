from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken, TokenError
from api.util import unset_cookies

class LogoutView(APIView):

    permission_classes = (IsAuthenticated, )

    def post(self, request):
        data = request.COOKIES

        refresh_token = data.get('refresh_token', None)

        try:
            RefreshToken(refresh_token).blacklist()
        except TokenError:
            return Response({'msg': 'Bad token'}), 400

        response = Response()
        unset_cookies(response)
        response.status_code = status.HTTP_204_NO_CONTENT

        return response
