from django import template
from ..models import PRODUCT_CODE, Sample

register = template.Library()

@register.filter(name="convert_code_to_name")
def convert_code_to_name(code): # Only one argument.
    try:
        CODE_OBJ = PRODUCT_CODE.objects.get(code=code)
        return CODE_OBJ.name
    except:
        CODE_OBJ = Sample.objects.get(sample_dog_code=code)
        return CODE_OBJ.sample_dog_name
    else:
        CODE_OBJ = Sample.objects.get(sample_cat_code=code)
        return CODE_OBJ.sample_cat_name
