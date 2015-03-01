__author__ = 'lemonApple'

from django.contrib.admin import site as admin_site

from chairmanhwang import models


admin_site.site_header = "ProjectCH Admin"
admin_site.register(models.Query)
admin_site.register(models.Unit)