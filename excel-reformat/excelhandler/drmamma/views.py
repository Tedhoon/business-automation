from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.http import HttpResponse
from openpyxl import load_workbook


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
    load_wb = load_workbook(excel.excel_file, data_only=True)
    #시트 이름으로 불러오기
    load_ws = load_wb['Sheet1']
    
    #셀 주소로 값 출력
    print(load_ws['A1'].value)
    
    #셀 좌표로 값 출력
    print(load_ws.cell(1,2).value)

    return redirect('excel_manage')
