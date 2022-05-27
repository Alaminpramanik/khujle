from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from categories.models import Biography


#gmap result filter
class BiographySerializer(ModelSerializer):
    class Meta:
        model = Biography
        fields =[ 'id','parent_id', 'name', 'slug','discription','status']

   

