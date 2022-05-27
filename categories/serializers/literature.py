from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from categories.models import Literature


#gmap result filter
class LiteratureSerializer(ModelSerializer):
    class Meta:
        model = Literature
        fields =[ 'id','parent_id', 'song_name', 'slug','writer_name','publication_name','discription','status']
