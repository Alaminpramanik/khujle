from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from categories.models import Categories


#gmap result filter
class CategoriesSerializer(ModelSerializer):

    class Meta:
        model = Categories
        fields =[ 'parent_id', 'name', 'slug','discription','status']

    def create(self, validated_data):
        parent_id=validated_data.get('parent_id')
        name=validated_data.get('name')
        slug=validated_data.get('slug')
        discription=validated_data.get('discription')
        status=validated_data.get('status')
        return  validated_data  

    def update(self, instance, validated_data):
        try:
            instance.parent_id = validated_data.get('parent_id', instance.parent_id)
            instance.name = validated_data.get('name', instance.name)
            instance.slug = validated_data.get('slug', instance.slug)
            instance.discription = validated_data.get('discription', instance.discription)
            instance.status = validated_data.get('status', instance.status)
            
        except Exception as e:
            print('error', e)

        return instance

