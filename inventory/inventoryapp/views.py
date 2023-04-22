from django.shortcuts import render
from django.db.models import Sum
from .models import Goods, DeliveryNoteDetails


def merchandise_sales_report(request):
    sales = DeliveryNoteDetails.objects.values('goods__name').annotate(
        quantity=Sum('quantity'), revenue=Sum('price')).order_by('goods__name')
    return render(request, 'merchandise_sales_report.html', {'sales': sales})


def profits_report(request):
    profits = DeliveryNoteDetails.objects.values(
        'delivery_note__type').annotate(
        profit=Sum('price')).order_by('delivery_note__type')
    return render(request, 'profits_report.html', {'profits': profits})


def merchandise_balance_report(request):
    balances = Goods.objects.values('name', 'unit').annotate(
        balance=Sum('deliverynotedetails__quantity')).order_by('name')
    return render(
        request, 'merchandise_balance_report.html', {'balances': balances})
