from django.db import models
from django.utils.translation import ugettext_lazy as _

class OpenidProvider(models.Model):
    icon = models.CharField(_('icon'), max_length=255, unique=False)
    name = models.CharField(_('name'), max_length=80, unique=True)
    pattern = models.CharField(_('pattern'), max_length=200, unique=False)
