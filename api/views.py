
from rest_framework import viewsets
from api.models import Company,Employee
from api.serializers import CompanySerializer,EmployeeSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
# Create your views here.
class ComapnayViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    @action(detail=True,methods=['get'])
    def empyees(self,request,pk= None):
        try:
            company = Company.objects.get(pk=pk)
            emps   = Employee.objects.filter(company = company)
            emps_serializers = EmployeeSerializer(emps,many = True,context={'request':request})
            return Response(emps_serializers.data)
        except Exception as e:
            print(e)
            return Response({
                'message ':'compnay might nit exisit'
            })


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
