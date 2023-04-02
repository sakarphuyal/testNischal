from rest_framework import serializers
from quickstart.models import *

class TestSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = test
        fields = ['name']
