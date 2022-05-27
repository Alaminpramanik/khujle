from rest_framework.generics import ListAPIView, CreateAPIView,RetrieveDestroyAPIView,RetrieveUpdateAPIView
from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework.response import Response
from categories.models import Lyrics

from categories.serializers.lyrics import LyricsSerializer


class LyricsCreateApiView(CreateAPIView):
   serializer_class = LyricsSerializer
   permission_classes = (AllowAny,)
    
   def create(self, request, *args, **kwargs):
      serializer = self.get_serializer(data=request.data)
      serializer.is_valid(raise_exception=True)
      self.perform_create(serializer)
      headers = self.get_success_headers(serializer.data)
      return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class LyricsListApiView(ListAPIView):
   serializer_class = LyricsSerializer
   queryset = Lyrics.objects.all()

class LyricsUpdateApiView(RetrieveUpdateAPIView):
   serializer_class = LyricsSerializer
   queryset = Lyrics.objects.all()
   lookup_url_kwarg = 'parent_id'
    
   
class LyricsDeleteApiView(RetrieveDestroyAPIView):
   serializer_class = LyricsSerializer
   queryset = Lyrics.objects.all()
   lookup_url_kwarg = 'parent_id'
