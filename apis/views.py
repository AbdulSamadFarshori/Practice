from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import EmployeeSerializer
from website.models import Employee
from rest_framework import status
# Create your views here.

class OperationsApiView(APIView):
    
    serializer_class = EmployeeSerializer
    
    def get(self, request):
        all_data = Employee.objects.all()
        serializer = self.serializer_class(all_data, many=True)
        data = serializer.data
        return Response({"data": data})
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response({'message':'data has been added!'})

    def put(self, request, pk):
        employee = get_object_or_404(Employee, pk=pk)
        if employee:
            serializer = self.serializer_class(employee, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({'message':'data has been updated!'})
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'message':'data not found'})

    def delete(self, request, pk):
        employee = get_object_or_404(Employee, pk=pk)
        if employee:
            employee.delete()
            return Response({'message':'data has been deleted!'})
