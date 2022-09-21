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
