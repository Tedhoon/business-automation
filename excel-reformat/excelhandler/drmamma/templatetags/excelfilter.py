from django import template
from ..models import PRODUCT_CODE, Sample

register = template.Library()

@register.filter(name="convert_code_to_name")
def convert_code_to_name(code):
    # print(PRODUCT_CODE.objects.get(code=code))
    try: 
        CODE_OBJ = PRODUCT_CODE.objects.get(code=code)
        return CODE_OBJ.name
    except:
        pass
    try:
        CODE_OBJ = Sample.objects.get(sample_dog_code=code)
        return CODE_OBJ.sample_dog_name
    except:
        pass

    try:
        CODE_OBJ = Sample.objects.get(sample_cat_code=code)
        return CODE_OBJ.sample_cat_name
    except:
        pass
    return code