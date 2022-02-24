from django.db import models
from django.utils.translation import ugettext_lazy as _
from ckeditor.fields import RichTextField
from base.models import BaseModel

class Categories(BaseModel):
    parent_id = models.IntegerField(unique=True,verbose_name=_('parent_id'), null=True, blank=True)
    name = models.CharField(verbose_name=_('name'),  max_length=255, null=True, blank=True)
    slug = models.CharField(verbose_name=_('slug'),  max_length=255, null=True, blank=True)
    discription = RichTextField()
    status = models.BooleanField(verbose_name=_('status'),default=True, null=True, blank=True)
    
    def __str__(self):
        return str(self.id) + ' - ' + str(self.parent_id)  + ' - ' + str(self.name )