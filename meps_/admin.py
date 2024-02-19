from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from . models import *

class MinistereAdmin(SummernoteModelAdmin):
    list_display = ('titre',)
    prepopulated_fields = {"slug": ("titre",)}
    summernote_fields = ('description',)

admin.site.register(Ministere, MinistereAdmin)