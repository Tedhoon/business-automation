from .models import DeliveryExcel
from django import forms

class DeliveryExcelForm(forms.ModelForm):
    class Meta:
        model = DeliveryExcel
        fields = '__all__'