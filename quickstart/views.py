from django.shortcuts import render
from rest_framework import viewsets
from quickstart.models import *
from quickstart.serializers import TestSerializer
from rest_framework.views import APIView
from rest_framework.response import Response



# Create your views here.
class TestViewSet(APIView):
    def get(self, request):
        return Response({"message": "Hello, world!"})

