"""excelhandler URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from drmamma.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('today_sale/', today_sale, name="today_sale"),
    path('whole_sale/', whole_sale, name="whole_sale"),
    path('excel_upload/', excel_upload, name="excel_upload"),
    # path('excel_convert/', excel_convert, name="excel_convert"),
    path('excel_manage/', excel_manage, name="excel_manage"),
    path('excel_convert_to_sebang/<int:pk>', excel_convert_to_sebang, name="excel_convert_to_sebang")
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
