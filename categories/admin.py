from typing import List
from django.contrib import admin
from categories.models import Categories


admin.site.site_header='Khujle Dhashboard'

class CategoriesAdmin(admin.ModelAdmin):
    List='parent_id'

admin.site.register(Categories, CategoriesAdmin)



