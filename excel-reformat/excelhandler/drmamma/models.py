from django.db import models
from django.utils import timezone

TYPE_CHOICES = (
    ('CAFE 24', 'CAFE 24'),
    ('네이버 스토어팜', '네이버 스토어팜'),
    ('기타', '기타')
)

class DeliveryExcel(models.Model):
    uploaded_at = models.DateField('업로드 날짜', default=timezone.now)
    excel_file = models.FileField('송장 엑셀', upload_to="excel")
    source = models.CharField('송장 종류', choices=TYPE_CHOICES, max_length=100)
    
    class Meta:
        verbose_name = "송장 엑셀"
        verbose_name_plural = "송장 엑셀들"


class Cafe24Temp(models.Model):
    store_code = models.TextField("발주처 코드", null=True, blank=True)
    order_pk = models.TextField("주문번호", null=True, blank=True)
    receiver = models.TextField("수령인", null=True, blank=True)
    address = models.TextField("수령인 주소(전체)", null=True, blank=True)
    post_num = models.TextField("수령인 우편번호", null=True, blank=True)
    phone_num = models.TextField("수령인 휴대전화", null=True, blank=True)
    phone_num2 = models.TextField("수령인 전화번호", null=True, blank=True)
    message = models.TextField("배송메시지", null=True, blank=True)
    product_code = models.TextField("자체품목코드", null=True, blank=True)
    amount = models.TextField("수량", null=True, blank=True)

    # -------- 위까지는 엑셀에 나와야함 -------- #

    total_price = models.TextField("총 주문 금액", null=True, blank=True)
    discount_product = models.TextField("상품별 추가할인금액", null=True, blank=True)
    discount_coupon = models.TextField("쿠폰 할인 금액", null=True, blank=True)
    used_reserves = models.TextField("사용한 적립금액", null=True, blank=True)

    # standard_for_gift = models.TextField("사은품 기준 금액", null=True, blank=True)

    made_by_source = models.ForeignKey(DeliveryExcel, verbose_name="연관 엑셀", on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = "Cafe24"
        verbose_name_plural = "Cafe24"



class NaverFarmTemp(models.Model):
    store_code = models.TextField("발주처 코드", null=True, blank=True)
    order_pk = models.TextField("주문번호", null=True, blank=True)
    receiver = models.TextField("수령인", null=True, blank=True)
    address = models.TextField("수령인 주소(전체)", null=True, blank=True)
    post_num = models.TextField("수령인 우편번호", null=True, blank=True)
    phone_num = models.TextField("수령인 휴대전화", null=True, blank=True)
    phone_num2 = models.TextField("수령인 전화번호", null=True, blank=True)
    message = models.TextField("배송메시지", null=True, blank=True)
    product_code = models.TextField("자체품목코드", null=True, blank=True)
    amount = models.TextField("수량", null=True, blank=True)


    # -------- 위까지는 엑셀에 나와야함 -------- #

    total_price = models.TextField("총 주문 금액", null=True, blank=True)
    order_price = models.TextField("배송비 합계", null=True, blank=True)

    made_by_source = models.ForeignKey(DeliveryExcel, verbose_name="연관 엑셀", on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = "네이버 스토어팜"
        verbose_name_plural = "네이버 스토어팜"









PRICE_STANDARD = [
    ('~3만원', '~3만원'),
    ('3만원~6만원', '3만원~6만원'),
    ('6만원~10만원', '6만원~10만원'),
    ('10만원~', '10만원~'),
]

class Sample(models.Model):
    sample_range = models.CharField('가격 범위', choices=PRICE_STANDARD, max_length=100)
    sample_dog_name = models.CharField('강아지 샘플 이름', max_length=100)
    sample_dog_code = models.CharField('강아지 샘플 코드', max_length=100)
    sample_cat_name = models.CharField('고양이 샘플 이름', max_length=100)
    sample_cat_code = models.CharField('고양이 샘플 코드', max_length=100)

    class Meta:
        verbose_name = "샘플"
        verbose_name_plural = "샘플"
        
    def __str__(self):
        return f'[{self.sample_range}] 범위의 샘플'

