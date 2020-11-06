from django import template
from ..models import PRODUCT_CODE, Sample

register = template.Library()

@register.filter(name="convert_code_to_name")
def convert_code_to_name(code): # Only one argument.
    if PRODUCT_CODE.objects.filter(code=code) is not None:
        CODE_OBJ = PRODUCT_CODE.objects.get(code=code)
        return CODE_OBJ.name
    if Sample.objects.filter(sample_dog_code=code) is not None:
        CODE_OBJ = Sample.objects.get(sample_dog_code=code)
        return CODE_OBJ.sample_dog_name
    if Sample.objects.filter(sample_cat_code=code) is not None:
        CODE_OBJ = Sample.objects.get(sample_cat_code=code)
        return CODE_OBJ.sample_cat_name
    return code