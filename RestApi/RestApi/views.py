from urllib import response
from .models import RestApi
from .serializers import RestApiSerializer
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET','POST'])
def get_List(request):
    if request.method=='GET':
        list_objects = RestApi.objects.all()
        list_serializer =  RestApiSerializer(list_objects,many=True)
        return JsonResponse({'get-details':list_serializer.data},safe=False)

    if request.method=='POST':
        serializer = RestApiSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)

@api_view(['PUT','DELETE','GET'])
def api_methods(request,id):
    try:
        object = RestApi.objects.get(pk=id)
    except RestApi.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method=='GET':
        serializer = RestApiSerializer(object)
        return Response(serializer.data)
        
    elif request.method=='PUT':
        serializer = RestApiSerializer(object,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    elif request.method=='DELETE':
        object.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)