from django.shortcuts import render

# Create your views here.
from retros.models import Users, Session
from retros.serializers import UsersSerializer, SessionSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import json


class UsersDetail(APIView):

    def get_object(self, pk):
        try:
            return Users.objects.get(pk = pk)
        except:
            raise Http404


    def get(self, request, pk, pas, format=None):
        chel = self.get_object(pk)
        serializer = UsersSerializer(chel)
        if serializer.data["password"] == str(pas):
            return Response(serializer.data["name"])    
        else:
            return Response(False)

class SessionKey(APIView):

    def get_object(self, pk):
        try:
            return Session.objects.get(pk = pk)
        except:
            raise Http404    

    def get(self, request, pk, format=None):
        game = self.get_object(pk)
        serializer = SessionSerializer(game)
        if serializer.data["id"] == str(pk):
            return Response(True)    
        else:
            return Response(False)

class SessionALl(APIView):    

    def get(self, request, pk, format=None):
        sess = Session.objects.all()
        serializer = SessionSerializer(sess, many = True)
        return Response(serializer.data[-1])


 
        

    # def post(self, request, format=None):
    #     serializer = SnippetSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #
    #
