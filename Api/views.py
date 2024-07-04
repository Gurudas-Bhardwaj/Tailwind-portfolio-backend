from django.shortcuts import render
from rest_framework.decorators import api_view
from MyApp.models import ContactModel
from .serializers import ContactSerializers
from rest_framework.response import Response


@api_view(['GET',"POST"])
def Contact_Data(request):

    if request.method=='GET':
        obj=ContactModel.objects.all()
        serializer=ContactSerializers(obj,many=True)
        return Response(serializer.data)
    
    elif request.method=='POST':
        data=request.data
        print(data)
        DataSerializer=ContactSerializers(data=data)
        if DataSerializer.is_valid():
            DataSerializer.save()
            return Response(DataSerializer.data)
        return Response(DataSerializer.errors)