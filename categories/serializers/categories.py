from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from categories.models import Categories


#gmap result filter
class CategoriesSerializer(ModelSerializer):
    class Meta:
        model = Categories
        fields =[ 'id','parent_id', 'name', 'slug','discription','status']

   

