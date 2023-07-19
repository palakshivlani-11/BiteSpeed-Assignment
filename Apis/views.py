from django.shortcuts import render
from .models import *
from rest_framework import generics, permissions, status
from .serializers import *
from django.http import HttpResponse
from django.db.models import Q

# Create your views here.

class identity(generics.GenericAPIView):
    
    def post(self,request):
        serializer = getDataSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data['email']
        phonenumber = serializer.validated_data['phonenumber']
        queryset = Contact.objects.filter(Q(email=email) | Q(phonenumber=phonenumber))
        print(queryset)
        if queryset.exists() == True:
            leng = len(queryset)
            print(leng)
            if leng > 1:
                print(queryset.last())
                obj = queryset.last()
                objf = queryset.first()
                obj.linkprecedence = "secondary"
                obj.linkedId = objf.id
                obj.save()
                print(obj.createdAt)
                print(obj.updatedAt)
            else:
                Contact.objects.create(email=email,phonenumber=phonenumber,linkedId=queryset.first().id,linkprecedence="secondary")
        else:
            Contact.objects.create(email=email,phonenumber=phonenumber)
            print("done")
        return HttpResponse("<h1>HI<h1>")
        