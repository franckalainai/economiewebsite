from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from . models import *

# Register your models here.
class MissionAdmin(SummernoteModelAdmin):
    list_display = ('titre',)
    prepopulated_fields = {"slug": ("titre",)}
    summernote_fields = ('description',)

class CabinetAdmin(SummernoteModelAdmin):
    list_display = ('titre',)
    prepopulated_fields = {"slug": ("titre",)}
    summernote_fields = ('description',)

class OrganigrammeAdmin(SummernoteModelAdmin):
    list_display = ('titre',)
    prepopulated_fields = {"slug": ("titre",)}
    summernote_fields = ('description',)

class TutelAdmin(SummernoteModelAdmin):
    list_display = ('titre',)
    prepopulated_fields = {"slug": ("titre",)}
    summernote_fields = ('description',)

class EcoleAdmin(SummernoteModelAdmin):
    list_display = ('titre',)
    prepopulated_fields = {"slug": ("titre",)}
    summernote_fields = ('description',)

class BiographieAdmin(SummernoteModelAdmin):
    list_display = ('titre',)
    prepopulated_fields = {"slug": ("titre",)}
    summernote_fields = ('description',)

admin.site.register(Mission, MissionAdmin)
admin.site.register(Cabinet, CabinetAdmin)
admin.site.register(Tutel, TutelAdmin)
admin.site.register(Ecole, EcoleAdmin)
admin.site.register(Biographie, BiographieAdmin)