from django.db import models
from django.utils.translation import ugettext_lazy as _

from base.models import BaseModel

class categories(BaseModel):
    parent_id = models.IntegerField(unique=True,verbose_name=_('parent_id'), null=True, blank=True)
    name = models.CharField(verbose_name=_('name'),  max_length=255, null=True, blank=True)
    slug = models.CharField(verbose_name=_('slug'),  max_length=255, null=True, blank=True)
    discription = models.TextField(verbose_name=_('discription'), null=True, blank=True)
    status = models.BooleanField(verbose_name=_('status'), null=True, blank=True)
    
    def __str__(self):
        return str(self.id) + ' - ' + str(self.parent_id)  + ' - ' + str(self.name )