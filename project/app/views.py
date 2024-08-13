from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import*
from .serializers import SchoolSerializer,StudentSerializer
from rest_framework import viewsets
from rest_framework.authtoken.models import Token  

# Create your views here.
class SchoolViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = SchoolModel.objects.all()
    serializer_class = SchoolSerializer

class StudentViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = StudentModel.objects.all()
    serializer_class = StudentSerializer

