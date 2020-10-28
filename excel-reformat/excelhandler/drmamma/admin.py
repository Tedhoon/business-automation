from django.contrib import admin
from .models import Cafe24, DeliveryExcel, Cafe24Temp, Sample
from import_export.admin import ImportExportMixin


class Cafe24Admin(ImportExportMixin, admin.ModelAdmin):
    pass


admin.site.register(Cafe24, Cafe24Admin)


admin.site.register(DeliveryExcel)



class Cafe24TempAdmin(ImportExportMixin, admin.ModelAdmin):
    pass


admin.site.register(Cafe24Temp, Cafe24TempAdmin)

admin.site.register(Sample)