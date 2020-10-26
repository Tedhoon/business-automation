from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.http import HttpResponse
from openpyxl import load_workbook
import pandas as pd

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
    # print(df.loc[0])
    # df.to_csv('/media/sebang/sample.csv')
    # return HttpResponse("/media/sebang/sample.csv")
    # return redirect('excel_manage')


    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=filename.csv'

    df.to_csv(path_or_buf=response, float_format='%.2f', index=False, encoding='UTF-8')
    # df.to_csv(path_or_buf=response, sep=';',float_format='%.2f', index=False, decimal=",", encoding='cp949')
    return response