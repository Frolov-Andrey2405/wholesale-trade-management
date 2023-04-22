"""
URL configuration for inventory project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from inventoryapp.views import merchandise_sales_report, profits_report, merchandise_balance_report

urlpatterns = [
    path('admin/', admin.site.urls),
    path(
        'merchandise_sales_report/', merchandise_sales_report,
        name='merchandise_sales_report'),
    path('profits_report/', profits_report, name='profits_report'),
    path(
        'merchandise_balance_report/', merchandise_balance_report,
        name='merchandise_balance_report'),
]
