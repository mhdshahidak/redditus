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


class ClientAdmin(admin.ModelAdmin):
    list_display = ('client_name','phone_no',)
    search_fields = ('client_name',)
admin.site.register(Client, ClientAdmin)


class BillingAdmin(admin.ModelAdmin):
    list_display = ('billing_no','client','billing_date',)
    search_fields = ('billing_no',)
admin.site.register(Billing, BillingAdmin)


class BillingProductsAdmin(admin.ModelAdmin):
    list_display = ('billing','qty','billing_date',)
    search_fields = ('item',)
admin.site.register(BillingProducts, BillingProductsAdmin)


class expencecatagoryAdmin(admin.ModelAdmin):
    list_display = ('catagory',)
    search_fields = ('catagory',)
admin.site.register(expencecatagory, expencecatagoryAdmin)


class expenceAdmin(admin.ModelAdmin):
    list_display = ('amount','date','catagory',)
    search_fields = ('amount',)
admin.site.register(expence, expenceAdmin)
