from django.contrib import admin
from .models import *
# Register your models here.

class StockAdmin(admin.ModelAdmin):
    list_display = ('item_name','quantity')
    search_fields=('item_name',)
admin.site.register(Stock,StockAdmin)


class CatagoryAdmin(admin.ModelAdmin):
    list_display = ('cat_name',)
    search_fields=('cat_name',)
admin.site.register(Catagory,CatagoryAdmin)

