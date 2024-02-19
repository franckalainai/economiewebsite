from django.contrib import admin
from . models import *
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('nom',)

admin.site.register(Banner)
admin.site.register(PhotoMinistre)