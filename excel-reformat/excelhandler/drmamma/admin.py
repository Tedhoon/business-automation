from django.contrib import admin
from .models import DeliveryExcel, Cafe24Temp, Sample, NaverFarmTemp, ETCTemp
from import_export.admin import ImportExportMixin

admin.site.register(DeliveryExcel)

class NaverFarmTempAdmin(ImportExportMixin, admin.ModelAdmin):
    pass

admin.site.register(NaverFarmTemp, NaverFarmTempAdmin)

class Cafe24TempAdmin(ImportExportMixin, admin.ModelAdmin):
    pass

admin.site.register(Cafe24Temp, Cafe24TempAdmin)


class ETCTempAdmin(ImportExportMixin, admin.ModelAdmin):
    pass

admin.site.register(ETCTemp, ETCTempAdmin)



admin.site.register(Sample)
