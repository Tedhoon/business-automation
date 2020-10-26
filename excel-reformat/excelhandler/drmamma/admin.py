from django.contrib import admin
from .models import Cafe24, DeliveryExcel
from import_export.admin import ImportExportMixin


class Cafe24Admin(ImportExportMixin, admin.ModelAdmin):
    pass


admin.site.register(Cafe24, Cafe24Admin)


admin.site.register(DeliveryExcel)