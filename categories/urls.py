from django.urls import path
from categories.views import categories,lyrics, biography,literature
 
urlpatterns = [
   path('categories/create/', categories.CategoriesCreateApiView.as_view(), name='categories-create'),
   path('categories/list/', categories.CategoriesListApiView.as_view(), name='categories-list'),
   path('categories/update/<parent_id>/', categories.CategoriesUpdateApiView.as_view(), name='categories-details'),
   path('categories/delete/<parent_id>/', categories.CategoriesDeleteApiView.as_view(), name='categories-create'),
   path('lyrics/create/', lyrics.LyricsCreateApiView.as_view(), name='lyrics-create'),
   path('lyrics/list/', lyrics.LyricsListApiView.as_view(), name='lyrics-list'),
   path('lyrics/update/<parent_id>/', lyrics.LyricsUpdateApiView.as_view(), name='lyrics-details'),
   path('lyrics/delete/<parent_id>/', lyrics.LyricsDeleteApiView.as_view(), name='lyrics-create'),
   path('biography/create/', biography.BiographyCreateApiView.as_view(), name='biography-create'),
   path('biography/list/', biography.BiographyListApiView.as_view(), name='biography-list'),
   path('biography/update/<parent_id>/', biography.BiographyUpdateApiView.as_view(), name='biography-details'),
   path('biography/delete/<parent_id>/', biography.BiographyDeleteApiView.as_view(), name='biography-create'),
   path('literature/create/', literature.LiteratureCreateApiView.as_view(), name='literature-create'),
   path('literature/list/', literature.LiteratureListApiView.as_view(), name='literature-list'),
   path('literature/update/<parent_id>/', literature.LiteratureUpdateApiView.as_view(), name='literature-details'),
   path('literature/delete/<parent_id>/', literature.LiteratureDeleteApiView.as_view(), name='literature-create'),


]