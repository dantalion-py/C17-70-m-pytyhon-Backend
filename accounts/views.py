from django.shortcuts import render
from rest_framework import viewsets
from .serializer import *

from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.
class AdministratorView(viewsets.ModelViewSet):
    serializer_class = AdminSerializer
    queryset = Administrator.objects.all()


class DoctorView(viewsets.ModelViewSet):
    serializer_class = DoctorSerializer
    queryset = Doctor.objects.all() 


class PatientView(viewsets.ModelViewSet):
    serializer_class = PatientSerializer
    queryset = Patient.objects.all()

class UserView(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = CustomUser.objects.all()

def home(request):
    return HttpResponse("<h1> hello world </h1>")

