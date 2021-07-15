from .models import MusicalWorks
from rest_framework import serializers


class MusicalWorksSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MusicalWorks
        fields = ['title', 'contributors', 'iswc']
