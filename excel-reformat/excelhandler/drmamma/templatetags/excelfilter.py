from django import template
from ..models import PRODUCT_CODE, Sample

register = template.Library()

@register.filter(name="convert_code_to_name")
def convert_code_to_name(code): # Only one argument.
    if PRODUCT_CODE.objects.get(code=code):
        CODE_OBJ = PRODUCT_CODE.objects.get(code=code)
        return CODE_OBJ.name
    if Sample.objects.get(sample_dog_code=code):
        CODE_OBJ = Sample.objects.get(sample_dog_code=code)
        return CODE_OBJ.sample_dog_name
    if Sample.objects.get(sample_cat_code=code):
        CODE_OBJ = Sample.objects.get(sample_cat_code=code)
        return CODE_OBJ.sample_cat_name
    return code