from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.http import HttpResponse
from openpyxl import load_workbook
import pandas as pd
from django.db.models import F, Sum, Count, Case, When



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



def excel_convert_to_sebang(request, pk):
    print(pk)
    excel = DeliveryExcel.objects.get(id=pk)
    target_excel = pd.read_csv(excel.excel_file)
    #시트 이름으로 불러오기
    df = pd.DataFrame(target_excel)
    # print(df.loc[0][0])
    # print(len(df))
    # print(df.shape[1])
    # for series in df:
    #     print(series)
    #     print("-----------------")

    # for col in range(df.shape[1]-1):
    #     for row in range(df.shape[0]-1):
    #         print(df.loc[row][col])
    if Cafe24Temp.objects.filter(made_by_source=excel):
        print("있으니까 넘어갑시당")
    else:
        print("없으니까 생성")
        for index, row in df.iterrows():
            Cafe24Temp.objects.create(
                order_pk = row[0], 
                product_num = row[1], 
                product_order_num = row[2], 
                receiver = row[3], 
                address = row[4], 
                post_num = row[5], 
                phone_num = row[6], 
                phone_num2 = row[7], 
                message = row[8], 
                product_name = row[9], 
                product_code = row[10], 
                amount = row[11], 
                price = row[12], 
                discount = row[13], 
                total_price = 0,
                made_by_source = excel
            )
    cafe24 = Cafe24Temp.objects.filter(made_by_source=excel)
    for obj in cafe24:
        print(obj.id)
    # print(cafe24)
    
    total_price = Cafe24Temp.objects.values(
        'order_pk'
    ).annotate(
        total_price_sum = Sum('price'),
        total_discount_sum = Sum('discount')
    )

    for i in total_price:
        print(i)
        print(i['order_pk'])
        qs_for_update = Cafe24Temp.objects.filter(order_pk=i['order_pk'])
        for qs in qs_for_update:
            total_price = i['total_price_sum'] - i['total_discount_sum']
            qs.total_price = total_price
            qs.save()
            print(total_price)
            print("-----------")
            
        # print(i)
        print("_------------")
    
    
    return redirect('excel_manage')
    # print(df['상품별 추가할인 상세'])
    # df.to_csv('/media/sebang/sample.csv')
    # return HttpResponse("/media/sebang/sample.csv")
    
    # response = HttpResponse(content_type='text/csv')
    # response['Content-Disposition'] = 'attachment; filename=filename3.csv'

    # df.to_csv(path_or_buf=response, sep=';', encoding='utf-8')
    # df.to_csv(path_or_buf=response, sep=';',float_format='%.2f', index=False, decimal=",", encoding='cp949')
    # 한 열씩 for 문 돌리면서 모델하나 생성 후에 넣으면서 해결해볼까

    return response