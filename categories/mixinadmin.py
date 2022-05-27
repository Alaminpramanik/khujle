from django.contrib import admin


class BiographyAdmin(admin.ModelAdmin):
    list_display=('parent_id','name','slug','discription','status')
    fieldsets = (
            
            ('parent_id info', {
                'fields': ('parent_id',)
                }),
            ('name info', {
                'fields': ('name',)
                }),
            ('slug info', {
                'fields': ('slug',)
                }),
            ('discription info', {
                'fields': ('discription',)
                }),
            ('status info', {
                'fields': ('status',)
                }),
        )

class CategorieAdmin(admin.ModelAdmin):
    list_display=('parent_id','name','slug','discription','status')
    # fieldsets = (
                
    #             ('parent_id info', {
    #                 'fields': ('parent_id',)
    #                 }),
    #             ('name info', {
    #                 'fields': ('name',)
    #                 }),
    #             ('slug info', {
    #                 'fields': ('slug',)
    #                 }),
    #             ('discription info', {
    #                 'fields': ('discription',)
    #                 }),
    #             ('status info', {
    #                 'fields': ('status',)
    #                 }),
    #         )


class LyricsAdmin(admin.ModelAdmin):
    list_display=('parent_id','song_name','slug','writer_name','musician_name','discription','status')
    fieldsets = (
           
            ('parent_id info', {
                'fields': ('parent_id',)
                }),
            ('song_name info', {
                'fields': ('song_name',)
                }),
            ('slug info', {
                'fields': ('slug',)
                }),
            ('writer_name info', {
                'fields': ('writer_name',)
                }),
            ('musician_name info', {
                'fields': ('musician_name',)
                }),
            ('discription info', {
                'fields': ('discription',)
                }),
            ('status info', {
                'fields': ('status',)
                }),
            
        )

class LiteratureAdmin(admin.ModelAdmin):
    list_display=('parent_id','name','slug','writer_name','publication_name','discription','status')
    fieldsets = (
           
            ('parent_id info', {
                'fields': ('parent_id',)
                }),
            ('name info', {
                'fields': ('name',)
                }),
            ('slug info', {
                'fields': ('slug',)
                }),
            ('writer_name info', {
                'fields': ('writer_name',)
                }),
            ('publication_name info', {
                'fields': ('publication_name',)
                }),
            ('discription info', {
                'fields': ('discription',)
                }),
            ('status info', {
                'fields': ('status',)
                }),
            
        )

class DirectoryAdmin(admin.ModelAdmin):
    list_display=('parent_id','name','slug','discription','status')
    fieldsets = (
            
            ('parent_id info', {
                'fields': ('parent_id',)
                }),
            ('name info', {
                'fields': ('name',)
                }),
            ('slug info', {
                'fields': ('slug',)
                }),
            ('discription info', {
                'fields': ('discription',)
                }),
            ('status info', {
                'fields': ('status',)
                }),
        )