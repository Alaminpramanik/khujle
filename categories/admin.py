from atexit import register
import site
from django.contrib import admin

from categories.models import categories

admin.site.register(categories)
