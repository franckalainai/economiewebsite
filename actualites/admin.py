from django.contrib import admin

# Register your models here.
from . models import *

class ActualiteAdmin(admin.ModelAdmin):
    list_display = ('titre',)
    prepopulated_fields = {"slug": ("titre",)}

admin.site.register(Actualite, ActualiteAdmin)
