from rest_framework import serializers
from .models import RestApi


class RestApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = RestApi
        fields  = ['id','name','description']