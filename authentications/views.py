from django.shortcuts import render
import json
from django.shortcuts import render
from rest_framework import serializers
from .models import  *
from rest_framework.permissions import IsAuthenticated,AllowAny
from django.shortcuts import  render
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse,JsonResponse
import io
from django.views.decorators.csrf import csrf_exempt

from rest_framework.decorators import  api_view, permission_classes
from rest_framework.decorators import api_view,action
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status,viewsets
from rest_framework import generics
from rest_framework import mixins
from authentications.models import *
from authentications.serializers import *
from rest_framework.generics import ListAPIView
from django_filters.rest_framework  import DjangoFilterBackend



class Userbasedfilter(generics.ListAPIView):
    queryset = UserAccount.objects.all()
    serializer_class = UserCreateSerializer
    def get_queryset(self):
        user = self.request.user
        return UserCreateSerializer.objects.filter(grantedby=user)

class masterfilter(ListAPIView):
    queryset =  UserAccount.objects.all()
    serializer_class = UserAccountSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['branch'] 




@csrf_exempt
@api_view(['POST','GET','PUT','DELETE'])
@permission_classes([AllowAny])
def hello_world(request):
    if request.method == "GET":
        msh = {'msg':'working'}
        ss = json.dumps(msh)
        
        return Response(ss)
    if request.method =="POST":
        # data =  request.data
        msh = {'msg':'post working'}
        ss = json.dumps(msh)
        
        return Response(ss)

class accountApi(APIView):
    def get(self,request):
        object = UserAccount.objects.all()
        serializer = UserCreateSerializer(object,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = UserCreateSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status = status.HTTP_201_CREATED)
        return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)

