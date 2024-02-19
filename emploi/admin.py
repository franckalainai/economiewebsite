from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from . models import *

# Register your models here.
class EmploiAdmin(SummernoteModelAdmin):
    list_display = ('titre',)
    prepopulated_fields = {"slug": ("titre",)}
    summernote_fields = ('description',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(Category, CategoryAdmin)
admin.site.register(Emploi, EmploiAdmin)