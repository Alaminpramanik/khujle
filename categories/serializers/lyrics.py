from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from categories.models import Lyrics


#gmap result filter
class LyricsSerializer(ModelSerializer):
    class Meta:
        model = Lyrics
        fields =[ 'id','parent_id', 'song_name', 'slug','writer_name','musician_name','discription','status']
