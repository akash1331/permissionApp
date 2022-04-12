from rest_framework.generics import ListAPIView
from django_filters.rest_framework  import DjangoFilterBackend
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
import authentications
from authentications.models import *
from .models import *
from rest_framework.parsers import JSONParser
from .serializers import *
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view,action
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status,viewsets
from rest_framework import generics
from rest_framework import mixins
import urllib.request
from authentications.serializers import *

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

class Permission_filter(APIView):
    def get_object(self,roll_number):
        try:
            return permission.objects.get(roll_number = roll_number)
        except permission.DoesNotExist:
            return HttpResponse(status = status.HTTP_404_NOT_FOUND)

    @api_view(['GET','POST'])
    def view(self,request,roll_number):
        obj = self.get_object(instance = roll_number)
        serializer = PermissionSerializer(obj,many = True)
        return Response(serializer.data)

class masterfilters(ListAPIView):
    queryset =  permission.objects.all()
    serializer_class = PermissionSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['student_roll'] 

class grantedfilter(ListAPIView):
    queryset =  permission.objects.all()
    serializer_class = PermissionSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['student_roll','granted'] 

class branchfilter(ListAPIView):
        queryset =  permission.objects.all()
        serializer_class = PermissionSerializer
        filter_backends = [DjangoFilterBackend]
        filter_fields = ['branch'] 

class branchgrant(ListAPIView):
        queryset =  permission.objects.all()
        serializer_class = PermissionSerializer
        filter_backends = [DjangoFilterBackend]
        filter_fields = ['branch','granted']

class admingrantview(APIView):
    def get(self,request):
        object = permission.objects.all()
        serializer = admingrantSerializer(object,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = admingrantSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status = status.HTTP_201_CREATED)
        return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)


class admingrant(APIView):
    # if UserAccount.type_of_account == "superadmin" or UserAccount.type_of_account == "admin":
        def get_object(self,id):
            try:
                return permission.objects.get(id = id)
            except permission.DoesNotExist:
                return HttpResponse(status = status.HTTP_404_NOT_FOUND)

        def get(self,request,id):
            articles = self.get_object(id)
            serializer = admingrantSerializer(articles)
            return Response(serializer.data)


        def put(self,request,id):
            article  = self.get_object(id)
            serializer = admingrantSerializer(article,data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)

        def delete(self,request,id):
            article = self.get_object(id)
            article.delete()
            return Response(status = status.HTTP_204_NO_CONTENT)

class qr(APIView):
    def get_object(self,id):
            try:
                return permission.objects.get(id = id)
            except permission.DoesNotExist:
                return HttpResponse(status = status.HTTP_404_NOT_FOUND)

    def get(self,request,id):
        articles = self.get_object(id)
        serializer = qrSerializer(articles)
        return Response(serializer.data)


    def put(self,request,id):
        article  = self.get_object(id)
        serializer = qrSerializer(article,data = request.data)
        if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
        return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)

    def delete(self,request,id):
        article = self.get_object(id)
        article.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
