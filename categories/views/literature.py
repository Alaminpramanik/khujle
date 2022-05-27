from rest_framework.generics import ListAPIView, CreateAPIView,RetrieveDestroyAPIView,RetrieveUpdateAPIView
from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework.response import Response
from categories.models import Literature

from categories.serializers.literature import LiteratureSerializer


class LiteratureCreateApiView(CreateAPIView):
   serializer_class = LiteratureSerializer
   permission_classes = (AllowAny,)
    
   def create(self, request, *args, **kwargs):
      serializer = self.get_serializer(data=request.data)
      serializer.is_valid(raise_exception=True)
      self.perform_create(serializer)
      headers = self.get_success_headers(serializer.data)
      return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class LiteratureListApiView(ListAPIView):
   serializer_class = LiteratureSerializer
   queryset = Literature.objects.all()

class LiteratureUpdateApiView(RetrieveUpdateAPIView):
   serializer_class = LiteratureSerializer
   queryset = Literature.objects.all()
   lookup_url_kwarg = 'parent_id'
    
   
class LiteratureDeleteApiView(RetrieveDestroyAPIView):
   serializer_class = LiteratureSerializer
   queryset = Literature.objects.all()
   lookup_url_kwarg = 'parent_id'
