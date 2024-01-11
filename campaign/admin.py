from django.contrib import admin
from app_1.models import campaign_product_table, campaign_table, campaign_categories_percentage
# Register your models here.
from import_export.admin import ImportExportModelAdmin
from .models import Order_notifications, Vendor_notifications


class Bran(ImportExportModelAdmin):
    pass

admin.site.register(campaign_table)
admin.site.register(campaign_categories_percentage)

admin.site.register(campaign_product_table)
admin.site.register(Order_notifications, Bran)
admin.site.register(Vendor_notifications, Bran)