from rest_framework.permissions import IsAuthenticated
from api.decorator import permission_required
from api.models import Employee
from api.serializers import EmployeeSerializer
from rest_framework.generics import ListAPIView

class EmployeeListView(ListAPIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = EmployeeSerializer

    #@permission_required([''])
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        return Employee.objects.all().order_by('-id')


   