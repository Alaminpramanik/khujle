from django.contrib import admin
from categories.models import Biography,Categories,Lyrics,Literature,Directory
from categories.mixinadmin import BiographyAdmin,CategorieAdmin,LyricsAdmin,LiteratureAdmin,DirectoryAdmin


admin.site.site_header='Khujle Dhashboard'

admin.site.register(Biography,BiographyAdmin)
admin.site.register(Categories,CategorieAdmin)
admin.site.register(Lyrics,LyricsAdmin)
admin.site.register(Literature,LiteratureAdmin)
admin.site.register(Directory,DirectoryAdmin)




