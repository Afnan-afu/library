from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from web.models import Members


class MemberSerializer(ModelSerializer):
    class Meta:
        model = Members
        fields = ['id','name','membership','date','expiry_date']


