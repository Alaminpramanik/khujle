from rest_framework.generics import ListAPIView, CreateAPIView,RetrieveDestroyAPIView,RetrieveUpdateAPIView
from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework.response import Response
from categories.models import Categories

from categories.serializers.categories import CategoriesSerializer


class CategoriesCreateApiView(CreateAPIView):
   serializer_class = CategoriesSerializer
   permission_classes = (AllowAny,)
    
   def create(self, request, *args, **kwargs):
      serializer = self.get_serializer(data=request.data)
      serializer.is_valid(raise_exception=True)
      self.perform_create(serializer)
      headers = self.get_success_headers(serializer.data)
      return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class CategoriesListApiView(ListAPIView):
   serializer_class = CategoriesSerializer
   queryset = Categories.objects.all()

class CategoriesUpdateApiView(RetrieveUpdateAPIView):
   serializer_class = CategoriesSerializer
   queryset = Categories.objects.all()
   lookup_url_kwarg = 'parent_id'
    
   
class CategoriesDeleteApiView(RetrieveDestroyAPIView):
   serializer_class = CategoriesSerializer
   queryset = Categories.objects.all()
   lookup_url_kwarg = 'parent_id'


   
  
