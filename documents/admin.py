from django.contrib import admin
from . models import *
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

class BudgetAdmin(admin.ModelAdmin):
    list_display = ('titre',)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Budget, BudgetAdmin)