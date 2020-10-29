from django.contrib import admin
from .models import DeliveryExcel, Cafe24Temp, Sample, NaverFarmTemp
from import_export.admin import ImportExportMixin

admin.site.register(DeliveryExcel)

class NaverFarmTempAdmin(ImportExportMixin, admin.ModelAdmin):
    pass

admin.site.register(NaverFarmTemp, NaverFarmTempAdmin)

class Cafe24TempAdmin(ImportExportMixin, admin.ModelAdmin):
    pass

admin.site.register(Cafe24Temp, Cafe24TempAdmin)

admin.site.register(Sample)