from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import *
from rest_framework.parsers import JSONParser
from .serializers import *
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import generics
from rest_framework import mixins
import urllib.request

# Create your views here.

class permissionAPIView(APIView):
    def get(self,request):
        object = permission.objects.all()
        serializer = PermissionSerializer(object,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = PermissionSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status = status.HTTP_201_CREATED)
        return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)

class permissionDetail(APIView):
    def get_object(self,id):
        try:
            return permission.objects.get(id = id)
        except permission.DoesNotExist:
            return HttpResponse(status = status.HTTP_404_NOT_FOUND)

    def get(self,request,id):
        articles = self.get_object(id)
        serializer = PermissionSerializer(articles)
        return Response(serializer.data)

    def put(self,request,id):
        article  = self.get_object(id)
        serializer = PermissionSerializer(article,data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)

    def delete(self,request,id):
        article = self.get_object(id)
        article.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)

# class permissionfilter(APIView):
    