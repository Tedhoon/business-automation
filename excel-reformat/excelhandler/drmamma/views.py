from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.http import HttpResponse
from openpyxl import load_workbook
import pandas as pd
import numpy as np
from django.db.models import F, Sum, Count, Case, When
from django.conf import settings


def today_sale(request):
    context = {}

    return render(request, 'today_sale.html', context)


def whole_sale(request):
    context = {}

    return render(request, 'whole_sale.html', context)


def excel_upload(request):
    if request.method == "GET":
        context = {}
        form = DeliveryExcelForm()
        context['form'] = form
        return render(request, 'excel_upload.html', context)
    
    received_form = DeliveryExcelForm(request.POST, request.FILES)
    if received_form.is_valid():
        received_form.save()
        return redirect('excel_manage')
    else:
        HttpResponse("잘못된 형식의 파일입니다.")
    return render(request, 'excel_upload.html', context)



def excel_manage(request):
    context = {}
    datas = DeliveryExcel.objects.all().order_by('-uploaded_at')
    context['datas'] = datas
    return render(request, 'excel_manage.html', context)






def cafe24_convert(excel):
    target_excel = pd.read_csv(excel.excel_file, encoding='utf-8')
    #시트 이름으로 불러오기
    df = pd.DataFrame(target_excel)
    df = df.replace(np.nan, '', regex=True) # nan 없애주고 갑시당

    if Cafe24Temp.objects.filter(made_by_source=excel):
        print("있으니까 넘어갑시당")
    else:
        print("없으니까 생성")
        for index, row in df.iterrows():
            Cafe24Temp.objects.create(
                store_code = "0001", # 발주처 코드
                order_pk = row[0], #주문번호
                receiver = row[3], #수령인
                address = row[4],
                post_num = row[5],
                phone_num = row[6],
                phone_num2 = row[7],
                message = row[9],
                product_code = row[10],
                amount = row[11],

                total_price = row[12],
                discount_product = row[13],
                discount_coupon = row[14],
                used_reserves = row[15],

                made_by_source = excel
            )

    cafe24 = Cafe24Temp.objects.filter(made_by_source=excel)

    price_calculate = cafe24.values(
        'order_pk'
    ).annotate(
        standard_for_gift = F('total_price') - Sum('discount_product') - F('discount_coupon') - F('used_reserves'),
    )


    for i in price_calculate:
        print(i)
        
        qs_for_update = cafe24.filter(order_pk=i['order_pk'])

        for qs in qs_for_update:
            total_price = i['standard_for_gift']
            qs.total_price = total_price
            qs.save()

        copy_qs = qs_for_update.first()

        sample_name = ''
        sample_code = ''
        is_cat = False
        CatFilterList = cafe24.filter(order_pk=i['order_pk'])
        for detected in CatFilterList:
            if detected.product_code in ["DM0030101", "DM0030102", "DM0030103", "DM0030104", "DM0030105B"]:
                is_cat = True
                print("냐옹이 감지")
                break
        
        if int(i['standard_for_gift']) >= 100000:  
            if is_cat:
                # sample_name = Sample.objects.get(sample_range = "10만원~").sample_cat_name
                sample_code = Sample.objects.get(sample_range = "10만원~").sample_cat_code
            else:
                # sample_name = Sample.objects.get(sample_range = "10만원~").sample_dog_name
                sample_code = Sample.objects.get(sample_range = "10만원~").sample_dog_code
        
        elif int(i['standard_for_gift']) >= 60000:
            if is_cat:
                # sample_name = Sample.objects.get(sample_range = "6만원~10만원").sample_cat_name
                sample_code = Sample.objects.get(sample_range = "6만원~10만원").sample_cat_code
            else:
                # sample_name = Sample.objects.get(sample_range = "6만원~10만원").sample_dog_name
                sample_code = Sample.objects.get(sample_range = "6만원~10만원").sample_dog_code
            
        elif int(i['standard_for_gift']) >= 30000:
            if is_cat:
                # sample_name = Sample.objects.get(sample_range = "3만원~6만원").sample_cat_name
                sample_code = Sample.objects.get(sample_range = "3만원~6만원").sample_cat_code
            else:
                # sample_name = Sample.objects.get(sample_range = "3만원~6만원").sample_dog_name
                sample_code = Sample.objects.get(sample_range = "3만원~6만원").sample_dog_code

        else:
            if is_cat:
                # sample_name = Sample.objects.get(sample_range = "~3만원").sample_cat_name
                sample_code = Sample.objects.get(sample_range = "~3만원").sample_cat_code
            else:
                # sample_name = Sample.objects.get(sample_range = "~3만원").sample_dog_name
                sample_code = Sample.objects.get(sample_range = "~3만원").sample_dog_code


        Cafe24Temp.objects.create(
                store_code = "0001", # 발주처 코드
                order_pk = copy_qs.order_pk, #주문번호
                receiver = copy_qs.receiver ,#수령인
                address = copy_qs.address,
                post_num = copy_qs.post_num,
                phone_num = copy_qs.phone_num,
                phone_num2 = copy_qs.phone_num2,
                message = copy_qs.message,
                product_code = sample_code,
                amount = "1",

                total_price = '',
                discount_product = '',
                discount_coupon = '',
                used_reserves = '',

                made_by_source = excel
            )

    # queryset = cafe24.values_list(
    #     "order_pk",
    #     "product_num",
    #     "product_order_num",
    #     "receiver",
    #     "address",
    #     "post_num",
    #     "phone_num",
    #     "phone_num2",
    #     "message",
    #     "product_name",
    #     "product_code",
    #     "amount",
    #     "price",
    #     "discount",
    #     "total_price"
    # )
    # converted_df = pd.DataFrame(list(queryset), columns=[
    #     "오더 피케이",
    #     "주문번호우",
    #     "product_order_num",
    #     "receiver",
    #     "address",
    #     "post_num",
    #     "phone_num",
    #     "phone_num2",
    #     "message",
    #     "product_name",
    #     "product_code",
    #     "amount",
    #     "price",
    #     "discount",
    #     "total_price"
    # ]) 
    # return converted_df
    return 0


def naver_farm_convert(excel):
    target_excel = pd.read_excel(excel.excel_file)
    #시트 이름으로 불러오기
    df = pd.DataFrame(target_excel)
    df = df.replace(np.nan, '', regex=True) # nan 없애주고 갑시당


    if NaverFarmTemp.objects.filter(made_by_source=excel):
        print("있으니까 넘어갑시당")
    else:
        print("없으니까 생성")
        for index, row in df.iterrows():
            NaverFarmTemp.objects.create(
                store_code = "0002",
                # order_pk = row[], 
                # product_num = row[], 
                # product_order_num = row[], 
                # receiver = row[], 
                # address = row[], 
                # post_num = row[], 
                # phone_num = row[], 
                # phone_num2 = row[], 
                # message = row[], 
                # product_name = row[], 
                # product_code = row[], 
                # amount = row[], 
                # price = row[], 
                # discount = row[], 
                total_price = 0,
                made_by_source = excel
            )

    naver_farm = NaverFarmTemp.objects.filter(made_by_source=excel)
    
    
    price_calculate = cafe24.values(
        'order_pk'
    ).annotate(
        standard_for_gift = F('total_price') - Sum('discount_product') - F('discount_coupon') - F('used_reserves'),
    )



    for i in price_calculate:
        print(i)
        
        qs_for_update = naver_farm.filter(order_pk=i['order_pk'])

        for qs in qs_for_update:
            total_price = i['standard_for_gift']
            qs.total_price = total_price
            qs.save()

        copy_qs = qs_for_update.first()

        sample_name = ''
        sample_code = ''
        is_cat = False
        CatFilterList = naver_farm.filter(order_pk=i['order_pk'])
        for detected in CatFilterList:
            if detected.product_code in ["DM0030101", "DM0030102", "DM0030103", "DM0030104", "DM0030105B"]:
                is_cat = True
                print("냐옹이 감지")
                break
        
        if int(i['standard_for_gift']) >= 100000:  
            if is_cat:
                # sample_name = Sample.objects.get(sample_range = "10만원~").sample_cat_name
                sample_code = Sample.objects.get(sample_range = "10만원~").sample_cat_code
            else:
                # sample_name = Sample.objects.get(sample_range = "10만원~").sample_dog_name
                sample_code = Sample.objects.get(sample_range = "10만원~").sample_dog_code
        
        elif int(i['standard_for_gift']) >= 60000:
            if is_cat:
                # sample_name = Sample.objects.get(sample_range = "6만원~10만원").sample_cat_name
                sample_code = Sample.objects.get(sample_range = "6만원~10만원").sample_cat_code
            else:
                # sample_name = Sample.objects.get(sample_range = "6만원~10만원").sample_dog_name
                sample_code = Sample.objects.get(sample_range = "6만원~10만원").sample_dog_code
            
        elif int(i['standard_for_gift']) >= 30000:
            if is_cat:
                # sample_name = Sample.objects.get(sample_range = "3만원~6만원").sample_cat_name
                sample_code = Sample.objects.get(sample_range = "3만원~6만원").sample_cat_code
            else:
                # sample_name = Sample.objects.get(sample_range = "3만원~6만원").sample_dog_name
                sample_code = Sample.objects.get(sample_range = "3만원~6만원").sample_dog_code

        else:
            if is_cat:
                # sample_name = Sample.objects.get(sample_range = "~3만원").sample_cat_name
                sample_code = Sample.objects.get(sample_range = "~3만원").sample_cat_code
            else:
                # sample_name = Sample.objects.get(sample_range = "~3만원").sample_dog_name
                sample_code = Sample.objects.get(sample_range = "~3만원").sample_dog_code


        NaverFarmTemp.objects.create(
                store_code = "0002", # 발주처 코드
                order_pk = copy_qs.order_pk, #주문번호
                receiver = copy_qs.receiver ,#수령인
                address = copy_qs.address,
                post_num = copy_qs.post_num,
                phone_num = copy_qs.phone_num,
                phone_num2 = copy_qs.phone_num2,
                message = copy_qs.message,
                product_code = sample_code,
                amount = "1",

                total_price = '',
                discount_product = '',
                discount_coupon = '',
                used_reserves = '',

                made_by_source = excel
            )




def excel_convert_to_sebang(request, pk):
    # converted_df = None
    excel = DeliveryExcel.objects.get(id=pk)

    if excel.source == 'CAFE 24':
        print("카페24꺼군")
        cafe24_convert(excel)

    elif excel.source == "네이버 스토어팜":
        print("스토어 팜이군!!!!")
        naver_farm_convert(excel)
    else: 
        pass

    return redirect('excel_manage')
    # response = HttpResponse(content_type='application/vnd.ms-excel') 
    # response['Content-Disposition'] = 'attachment; filename="test.xls"'
    # response = HttpResponse(content_type='text/csv')
    # response['Content-Disposition'] = 'attachment; filename = helloworld.csv'
    # writer = pd.ExcelWriter('test.xlsx')
    # converted_df.to_excel(writer)
    # writer.save()
    # converted_df.to_csv(path_or_buf=response,sep=',',float_format='%.2f',index=False,decimal=",")

    # converted_df.to_csv(path_or_buf=response, sep=';',float_format='%.2f', index=False, decimal=",", encoding='cp949')
    # 한 열씩 for 문 돌리면서 모델하나 생성 후에 넣으면서 해결해볼까

    return response
    