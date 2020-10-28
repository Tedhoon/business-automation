from django.db import models
from datetime import datetime
class Cafe24(models.Model):
    extract_day = models.CharField('출고일자', max_length=10, default=datetime.today())
    # 출고일자 [오늘]
    order_num = models.TextField('주문번호')
    # 주문번호 
    truck = models.TextField('트럭출고', blank=True)
    # 트럭출고 [ ]
    bj_code = models.TextField('발주처코드', default="0001")
    # 발주처코드 [0001]
    bj_name= models.TextField('발주처명', blank=True)
    # 발주처명 [ ]
    bs = models.TextField('배송(주문)', default="0000")
    # 배송(주문) [0000]
    bs_name = models.TextField('배송(주문)처명', blank=True)
    # 배송(주문)처명 [ ]
    receiver = models.TextField('수령자')
    # 수령자
    bs_address = models.TextField('배송처')
    # 배송처 주소
    post_id = models.TextField('우편번호')
    # 우편번호
    phone = models.TextField('대표연락처')
    # 대표연락처
    phone2 = models.TextField('연락처2')
    # 연락처2
    bs_yogoo = models.TextField('배송요구사항', blank=True)
    # 배송요구사항 => blank True
    dp_code = models.TextField('대표코드', blank=True)
    # 대표코드 [ ] 
    product_code = models.TextField('제품코드', blank=True)
    # 제품코드 
    product = models.TextField('제품', blank=True)
    # 제품 [ ]
    amount = models.TextField('수량')
    # 수량
    is_normal = models.TextField('정상여부', blank=True)
    # 정상여부
    memo1 = models.TextField('메모1', blank=True)
    # 메모1 [ ] 
    memo2 = models.TextField('메모2', blank=True)
    # 메모2 [ ]
    memo3 = models.TextField('메모3', blank=True)
    # 메모3 [ ]


    class Meta:
        verbose_name = "카페24"
        verbose_name_plural = "카페24"  


TYPE_CHOICES = (
    ('CAFE 24', 'CAFE 24'),
    ('네이버 스토어팜', '네이버 스토어팜'),
    ('기타', '기타')
)

class DeliveryExcel(models.Model):
    uploaded_at = models.DateField('업로드 날짜', default=datetime.today())
    excel_file = models.FileField('송장 엑셀', upload_to="excel")
    source = models.CharField('송장 종류', choices=TYPE_CHOICES, max_length=100)
    
    class Meta:
        verbose_name = "송장 엑셀"
        verbose_name_plural = "송장 엑셀들"


class Cafe24Temp(models.Model):
    order_pk = models.TextField("주문번호", null=True, blank=True)
    product_num = models.TextField("품목번호", null=True, blank=True)
    product_order_num = models.TextField("품목별 주문번호", null=True, blank=True)
    receiver = models.TextField("수령인", null=True, blank=True)
    address = models.TextField("수령인 주소(전체)", null=True, blank=True)
    post_num = models.TextField("수령인 우편번호", null=True, blank=True)
    phone_num = models.TextField("수령인 휴대전화", null=True, blank=True)
    phone_num2 = models.TextField("수령인 전화번호", null=True, blank=True)
    message = models.TextField("배송메시지", null=True, blank=True)
    product_name = models.TextField("주문상품명(옵션포함)", null=True, blank=True)
    product_code = models.TextField("자체품목코드", null=True, blank=True)
    amount = models.TextField("수량", null=True, blank=True)
    price = models.TextField("상품구매금액(KRW)", null=True, blank=True)
    discount = models.TextField("상품별 추가할인금액", null=True, blank=True)
    total_price = models.TextField("총 주문 금액", null=True, blank=True)
    
    made_by_source = models.ForeignKey(DeliveryExcel, verbose_name="연관 엑셀", on_delete=models.CASCADE, null=True)
